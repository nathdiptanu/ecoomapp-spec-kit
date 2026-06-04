from app import db
from app.models import Category, Product


CATEGORY_DESCRIPTIONS = {
    "Electronics": "Everyday electronics, audio, and smart devices.",
    "Mobile Phones": "Flagship, mid-range, and value smartphones.",
    "Laptops": "Portable computers for work, study, and gaming.",
    "Fashion": "Apparel, shoes, and accessories.",
    "Home & Kitchen": "Appliances and practical home essentials.",
    "Books": "Programming, business, fiction, and personal growth titles.",
    "Sports": "Fitness, outdoor, and team sport equipment.",
    "Toys": "Games, STEM kits, and creative play products.",
}


PRODUCT_NAMES = {
    "Electronics": [
        "Sony Noise Cancelling Headphones",
        "Apple Watch Series 10",
        "Kindle Paperwhite",
        "JBL Bluetooth Speaker",
        "Canon Mirrorless Camera",
        "Samsung 4K Smart TV",
        "Logitech Wireless Keyboard",
    ],
    "Mobile Phones": [
        "iPhone 15",
        "Samsung Galaxy S25",
        "OnePlus 14",
        "Google Pixel 9",
        "Motorola Edge Pro",
        "Nothing Phone 3",
        "Xiaomi Redmi Note 14",
    ],
    "Laptops": [
        "MacBook Air",
        "Dell XPS",
        "Lenovo ThinkPad",
        "HP Spectre x360",
        "Asus Zenbook",
        "Acer Swift Go",
        "Microsoft Surface Laptop",
    ],
    "Fashion": [
        "Men's T-Shirt",
        "Women's Jacket",
        "Running Shoes",
        "Slim Fit Jeans",
        "Leather Wallet",
        "Cotton Hoodie",
        "Classic Sneakers",
    ],
    "Home & Kitchen": [
        "Instant Pot Cooker",
        "Air Fryer",
        "Robot Vacuum",
        "Stainless Steel Cookware Set",
        "Memory Foam Pillow",
        "Coffee Maker",
        "Water Purifier",
    ],
    "Books": [
        "Python Programming",
        "Flask Web Development",
        "Clean Code",
        "The Pragmatic Programmer",
        "Designing Data-Intensive Applications",
        "Atomic Habits",
        "The Lean Startup",
    ],
    "Sports": [
        "Yoga Mat",
        "Adjustable Dumbbells",
        "Football",
        "Cricket Bat",
        "Mountain Bike Helmet",
        "Resistance Bands",
        "Tennis Racket",
    ],
    "Toys": [
        "LEGO City Set",
        "STEM Robot Kit",
        "Remote Control Car",
        "Wooden Puzzle",
        "Art Craft Box",
        "Board Game Collection",
        "Plush Bear",
    ],
}


def seed_database():
    if Product.query.first():
        return

    categories = {}
    for name, description in CATEGORY_DESCRIPTIONS.items():
        category = Category(name=name, description=description)
        db.session.add(category)
        categories[name] = category

    db.session.flush()

    product_index = 1
    for category_name, product_names in PRODUCT_NAMES.items():
        for offset, product_name in enumerate(product_names, start=1):
            price = 19.99 + (product_index * 8.75) + (offset * 3.5)
            product = Product(
                name=product_name,
                description=f"{product_name} with dependable quality, fast local checkout, and demo-ready inventory.",
                price=round(price, 2),
                stock=10 + (product_index % 35),
                image_url=f"https://placehold.co/600x400?text={product_name.replace(' ', '+')}",
                category=categories[category_name],
            )
            db.session.add(product)
            product_index += 1

    db.session.commit()
