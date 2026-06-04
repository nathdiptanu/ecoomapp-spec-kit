from app.models import Order, Product


def test_wishlist_add_and_view(client, app):
    with app.app_context():
        product = Product.query.first()
        product_id = product.id

    response = client.post(f"/wishlist/add/{product_id}", follow_redirects=True)
    assert response.status_code == 200
    assert b"Product added to wishlist" in response.data

    response = client.get("/wishlist")
    assert response.status_code == 200
    assert product.name.encode() in response.data


def test_wishlist_duplicate_add_does_not_duplicate_item(client, app):
    with app.app_context():
        product = Product.query.first()
        product_id = product.id

    client.post(f"/wishlist/add/{product_id}")
    client.post(f"/wishlist/add/{product_id}")

    with client.session_transaction() as session:
        assert session["wishlist"] == [str(product_id)]


def test_wishlist_remove_item(client, app):
    with app.app_context():
        product = Product.query.first()
        product_id = product.id

    client.post(f"/wishlist/add/{product_id}")
    response = client.post(f"/wishlist/remove/{product_id}", follow_redirects=True)

    assert response.status_code == 200
    assert b"Product removed from wishlist" in response.data
    with client.session_transaction() as session:
        assert session.get("wishlist") == []


def test_wishlist_move_to_cart(client, app):
    with app.app_context():
        product = Product.query.first()
        product_id = product.id

    client.post(f"/wishlist/add/{product_id}")
    response = client.post(f"/wishlist/move-to-cart/{product_id}", follow_redirects=True)

    assert response.status_code == 200
    assert b"Product moved to cart" in response.data
    with client.session_transaction() as session:
        assert session.get("wishlist") == []
        assert session["cart"][str(product_id)] == 1


def test_wishlist_route_is_available_without_auth(client, app):
    response = client.get("/wishlist")
    assert response.status_code == 200


def test_seed_data_loads(app):
    with app.app_context():
        assert Product.query.count() >= 50


def test_catalog_search_finds_seeded_product(client):
    response = client.get("/?q=iPhone")
    assert response.status_code == 200
    assert b"iPhone 15" in response.data


def test_cart_add_update_remove(client, app):
    with app.app_context():
        product = Product.query.first()
        product_id = product.id

    response = client.post(f"/cart/add/{product_id}", data={"quantity": 2}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Product added to cart" in response.data

    response = client.post(f"/cart/update/{product_id}", data={"quantity": 3}, follow_redirects=True)
    assert b"Cart updated" in response.data
    assert b"value=\"3\"" in response.data

    response = client.post(f"/cart/remove/{product_id}", follow_redirects=True)
    assert b"Your cart is empty" in response.data


def test_checkout_creates_order_and_clears_cart(client, app):
    with app.app_context():
        product = Product.query.first()
        product_id = product.id

    client.post(f"/cart/add/{product_id}", data={"quantity": 1})
    response = client.post(
        "/checkout",
        data={
            "customer_name": "Test Shopper",
            "email": "shopper@example.com",
            "address": "123 Test Street",
            "city": "Testville",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Order Confirmed" in response.data
    with app.app_context():
        order = Order.query.first()
        assert order is not None
        assert order.customer_name == "Test Shopper"
        assert len(order.items) == 1

    cart_response = client.get("/cart")
    assert b"Your cart is empty" in cart_response.data


def test_admin_pages_available(client):
    assert client.get("/admin").status_code == 200
    assert client.get("/admin/products").status_code == 200
    assert client.get("/admin/orders").status_code == 200
