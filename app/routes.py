from flask import Blueprint, abort, flash, redirect, render_template, request, session, url_for

from app import db
from app.models import Category, Order, OrderItem, Product


bp = Blueprint("main", __name__)


def _cart():
    return session.setdefault("cart", {})


def _cart_items():
    cart = _cart()
    ids = [int(product_id) for product_id in cart.keys()]
    products = Product.query.filter(Product.id.in_(ids)).all() if ids else []
    items = []
    for product in products:
        quantity = int(cart.get(str(product.id), 0))
        if quantity > 0:
            items.append(
                {
                    "product": product,
                    "quantity": quantity,
                    "line_total": float(product.price) * quantity,
                }
            )
    return items


def _cart_count():
    return sum(int(quantity) for quantity in _cart().values())


@bp.context_processor
def inject_globals():
    return {"cart_count": _cart_count(), "categories": Category.query.order_by(Category.name).all()}


@bp.route("/")
def catalog():
    search = request.args.get("q", "").strip()
    category_id = request.args.get("category", type=int)
    query = Product.query

    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))
    if category_id:
        query = query.filter(Product.category_id == category_id)

    products = query.order_by(Product.name).all()
    selected_category = db.session.get(Category, category_id) if category_id else None
    return render_template("catalog.html", products=products, search=search, selected_category=selected_category)


@bp.route("/products/<int:product_id>")
def product_detail(product_id):
    product = db.session.get(Product, product_id) or abort(404)
    return render_template("product_detail.html", product=product)


@bp.route("/cart")
def view_cart():
    items = _cart_items()
    total = sum(item["line_total"] for item in items)
    return render_template("cart.html", items=items, total=total)


@bp.post("/cart/add/<int:product_id>")
def add_to_cart(product_id):
    db.session.get(Product, product_id) or abort(404)
    quantity = max(request.form.get("quantity", 1, type=int), 1)
    cart = _cart()
    cart[str(product_id)] = int(cart.get(str(product_id), 0)) + quantity
    session.modified = True
    flash("Product added to cart.", "success")
    return redirect(request.referrer or url_for("main.view_cart"))


@bp.post("/cart/update/<int:product_id>")
def update_cart(product_id):
    quantity = request.form.get("quantity", 1, type=int)
    cart = _cart()
    if quantity <= 0:
        cart.pop(str(product_id), None)
    else:
        cart[str(product_id)] = quantity
    session.modified = True
    flash("Cart updated.", "info")
    return redirect(url_for("main.view_cart"))


@bp.post("/cart/remove/<int:product_id>")
def remove_from_cart(product_id):
    _cart().pop(str(product_id), None)
    session.modified = True
    flash("Product removed from cart.", "warning")
    return redirect(url_for("main.view_cart"))


@bp.route("/checkout", methods=["GET", "POST"])
def checkout():
    items = _cart_items()
    if not items:
        flash("Your cart is empty.", "warning")
        return redirect(url_for("main.catalog"))

    if request.method == "POST":
        order = Order(
            customer_name=request.form["customer_name"],
            email=request.form["email"],
            address=request.form["address"],
            city=request.form["city"],
        )
        for item in items:
            order.items.append(
                OrderItem(
                    product=item["product"],
                    quantity=item["quantity"],
                    unit_price=item["product"].price,
                )
            )
        db.session.add(order)
        db.session.commit()
        session["cart"] = {}
        flash("Payment simulated successfully. Your order has been placed.", "success")
        return redirect(url_for("main.order_success", order_id=order.id))

    total = sum(item["line_total"] for item in items)
    return render_template("checkout.html", items=items, total=total)


@bp.route("/orders/<int:order_id>/success")
def order_success(order_id):
    order = db.session.get(Order, order_id) or abort(404)
    return render_template("order_success.html", order=order)


@bp.route("/admin")
def admin_dashboard():
    product_count = Product.query.count()
    order_count = Order.query.count()
    return render_template("admin/dashboard.html", product_count=product_count, order_count=order_count)


@bp.route("/admin/products")
def admin_products():
    products = Product.query.order_by(Product.name).all()
    return render_template("admin/products.html", products=products)


@bp.route("/admin/products/new", methods=["GET", "POST"])
def admin_product_new():
    if request.method == "POST":
        product = Product(
            name=request.form["name"],
            description=request.form["description"],
            price=request.form["price"],
            stock=request.form["stock"],
            image_url=request.form["image_url"],
            category_id=request.form["category_id"],
        )
        db.session.add(product)
        db.session.commit()
        flash("Product created.", "success")
        return redirect(url_for("main.admin_products"))
    return render_template("admin/product_form.html", product=None)


@bp.route("/admin/products/<int:product_id>/edit", methods=["GET", "POST"])
def admin_product_edit(product_id):
    product = db.session.get(Product, product_id) or abort(404)
    if request.method == "POST":
        product.name = request.form["name"]
        product.description = request.form["description"]
        product.price = request.form["price"]
        product.stock = request.form["stock"]
        product.image_url = request.form["image_url"]
        product.category_id = request.form["category_id"]
        db.session.commit()
        flash("Product updated.", "success")
        return redirect(url_for("main.admin_products"))
    return render_template("admin/product_form.html", product=product)


@bp.post("/admin/products/<int:product_id>/delete")
def admin_product_delete(product_id):
    product = db.session.get(Product, product_id) or abort(404)
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted.", "warning")
    return redirect(url_for("main.admin_products"))


@bp.route("/admin/orders")
def admin_orders():
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template("admin/orders.html", orders=orders)


@bp.route("/admin/orders/<int:order_id>")
def admin_order_detail(order_id):
    order = db.session.get(Order, order_id) or abort(404)
    return render_template("admin/order_detail.html", order=order)
