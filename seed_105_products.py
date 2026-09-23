from pathlib import Path
from backend.app import app
from backend.database import db
from backend.models.product import Product
from backend.models.user import User
from backend.models.category import Category
from backend.models.entrepreneur import Entrepreneur

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "frontend" / "images"

CATEGORY_CONFIG = {
    "Tailor": {
        "folder": "tailor",
        "count": 20,
        "products": [
            ("Custom Blouse", "Custom stitched blouse with neat finishing."),
            ("Designer Blouse", "Elegant designer blouse for special occasions."),
            ("Cotton Kurta", "Comfortable cotton kurta with custom fitting."),
            ("Salwar Suit", "Traditional salwar suit with customized stitching."),
            ("Ladies Churidar", "Comfortable churidar with accurate measurements."),
            ("Kids Frock", "Beautiful custom stitched frock for children."),
            ("Wedding Blouse", "Special blouse stitching for wedding functions."),
            ("Casual Kurti", "Simple and comfortable daily wear kurti."),
            ("Embroidered Blouse", "Blouse with decorative embroidery work."),
            ("Party Wear Dress", "Custom party wear dress with elegant finishing."),
            ("School Uniform", "Neatly stitched school uniform."),
            ("Traditional Skirt", "Traditional skirt with customized measurements."),
            ("Cotton Saree Blouse", "Comfortable cotton saree blouse."),
            ("Silk Blouse", "Premium stitching for silk saree blouses."),
            ("Anarkali Dress", "Custom stitched Anarkali dress."),
            ("Kids Kurta", "Traditional kurta designed for children."),
            ("Office Kurti", "Simple professional kurti for office wear."),
            ("Bridal Blouse", "Detailed bridal blouse stitching."),
            ("Alteration Service", "Professional clothing alteration service."),
            ("Custom Dress", "Custom dress made according to customer measurements.")
        ]
    },
    "Potter": {
        "folder": "potter",
        "count": 20,
        "products": [
            ("Clay Pot", "Handcrafted traditional clay pot."),
            ("Decorative Pot", "Decorative handmade pottery for home interiors."),
            ("Water Pot", "Traditional clay water storage pot."),
            ("Clay Vase", "Handmade clay vase with artistic finishing."),
            ("Flower Pot", "Natural clay flower pot."),
            ("Terracotta Bowl", "Handcrafted terracotta serving bowl."),
            ("Clay Cup", "Traditional handmade clay cup."),
            ("Pottery Plate", "Handcrafted pottery plate."),
            ("Serving Bowl", "Decorative handmade serving bowl."),
            ("Terracotta Lamp", "Traditional terracotta decorative lamp."),
            ("Clay Diya Set", "Handmade clay diya collection."),
            ("Storage Pot", "Traditional clay storage container."),
            ("Mini Clay Pot", "Small decorative clay pot."),
            ("Handmade Mug", "Unique handmade pottery mug."),
            ("Terracotta Planter", "Natural terracotta planter for plants."),
            ("Clay Jar", "Traditional handmade clay jar."),
            ("Pottery Candle Holder", "Decorative pottery candle holder."),
            ("Decorative Terracotta", "Handcrafted terracotta decoration."),
            ("Clay Serving Set", "Handmade clay serving set."),
            ("Art Pottery", "Artistic handcrafted pottery piece.")
        ]
    },
    "Cobbler": {
        "folder": "cobbler",
        "count": 15,
        "products": [
            ("Leather Sandals", "Handcrafted leather sandals."),
            ("Leather Shoes", "Durable handmade leather shoes."),
            ("Traditional Chappals", "Traditional handcrafted chappals."),
            ("Casual Sandals", "Comfortable handmade casual sandals."),
            ("School Shoes", "Durable school shoes with quality finishing."),
            ("Formal Shoes", "Handcrafted formal footwear."),
            ("Leather Slippers", "Comfortable leather slippers."),
            ("Kolhapuri Chappals", "Traditional handcrafted Kolhapuri-style footwear."),
            ("Custom Footwear", "Footwear customized according to customer requirements."),
            ("Shoe Repair Service", "Professional shoe repair and maintenance."),
            ("Sandal Repair", "Repair and restoration of sandals."),
            ("Leather Belt", "Handcrafted leather belt."),
            ("Traditional Footwear", "Traditional handmade footwear."),
            ("Kids Sandals", "Comfortable handmade sandals for children."),
            ("Handmade Boots", "Durable handcrafted leather boots.")
        ]
    },
    "Artisan": {
        "folder": "artisan",
        "count": 20,
        "products": [
            ("Handmade Wall Art", "Decorative handmade wall art."),
            ("Wooden Craft", "Handcrafted wooden decorative item."),
            ("Bamboo Basket", "Traditional handmade bamboo basket."),
            ("Decorative Craft", "Unique handcrafted decorative piece."),
            ("Handmade Key Holder", "Decorative handmade key holder."),
            ("Wooden Decoration", "Artistic wooden home decoration."),
            ("Bamboo Craft", "Traditional bamboo handicraft."),
            ("Handmade Frame", "Decorative handmade photo frame."),
            ("Craft Gift Box", "Handcrafted gift box for special occasions."),
            ("Traditional Craft", "Traditional locally crafted decorative item."),
            ("Handmade Toy", "Handcrafted traditional toy."),
            ("Wooden Bowl", "Handcrafted wooden serving bowl."),
            ("Bamboo Organizer", "Useful handmade bamboo organizer."),
            ("Artisan Sculpture", "Decorative handcrafted sculpture."),
            ("Handmade Tray", "Artistic handmade serving tray."),
            ("Wooden Lamp", "Handcrafted decorative wooden lamp."),
            ("Craft Basket", "Handmade storage basket."),
            ("Decorative Sculpture", "Unique handcrafted decorative sculpture."),
            ("Handmade Mirror Frame", "Decorative handcrafted mirror frame."),
            ("Local Handicraft", "Locally made traditional handicraft.")
        ]
    },
    "Handmade Products": {
        "folder": "handmade",
        "count": 15,
        "products": [
            ("Handmade Gift", "Unique handmade gift item."),
            ("Handmade Candle", "Decorative handmade candle."),
            ("Handmade Soap", "Locally crafted handmade soap."),
            ("Decorative Basket", "Handmade basket for home decoration."),
            ("Handmade Notebook", "Crafted notebook with handmade finishing."),
            ("Gift Hamper", "Handcrafted gift hamper."),
            ("Handmade Jewelry", "Unique handmade jewelry item."),
            ("Crafted Earrings", "Beautiful handmade earrings."),
            ("Handmade Bracelet", "Handcrafted bracelet."),
            ("Decorative Flower", "Handmade decorative flower."),
            ("Fabric Craft", "Creative handmade fabric craft."),
            ("Handmade Doll", "Traditional handmade doll."),
            ("Craft Gift Item", "Unique handcrafted gift item."),
            ("Handmade Home Decor", "Decorative handmade home accessory."),
            ("Local Handmade Collection", "Collection of locally handcrafted products.")
        ]
    },
    "Local Vendor": {
        "folder": "local-vendor",
        "count": 15,
        "products": [
            ("Fresh Local Produce", "Fresh products supplied by a local vendor."),
            ("Homemade Snacks", "Locally prepared homemade snacks."),
            ("Traditional Snacks", "Traditional locally prepared snack items."),
            ("Local Food Pack", "Selection of locally prepared food products."),
            ("Fresh Fruits", "Fresh locally sourced fruits."),
            ("Fresh Vegetables", "Fresh locally sourced vegetables."),
            ("Homemade Pickle", "Traditional homemade pickle."),
            ("Local Spice Pack", "Locally prepared spice collection."),
            ("Homemade Sweets", "Traditional homemade sweets."),
            ("Local Breakfast Pack", "Fresh local breakfast items."),
            ("Traditional Food", "Locally prepared traditional food."),
            ("Homemade Flour", "Locally prepared flour product."),
            ("Local Grocery Pack", "Selection of essential local grocery products."),
            ("Village Products", "Collection of locally sourced products."),
            ("Local Speciality Pack", "Special collection of local specialty products.")
        ]
    }
}

def get_images(folder):
    folder_path = IMAGE_DIR / folder
    allowed = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
    return sorted(
        [
            p for p in folder_path.iterdir()
            if p.is_file() and p.suffix.lower() in allowed
        ],
        key=lambda p: p.name.lower()
    )

def main():
    with app.app_context():
        print("\nHunarHub product image seeding started...\n")

        entrepreneurs = Entrepreneur.query.all()

        if not entrepreneurs:
            print("ERROR: No entrepreneur records found.")
            print("Create at least one entrepreneur account first.")
            return

        print(f"Entrepreneurs found: {len(entrepreneurs)}")

        entrepreneur = entrepreneurs[0]

        print(
            f"Using entrepreneur ID: {entrepreneur.id}"
        )

        existing_demo = Product.query.filter(
            Product.name.like("HH Demo - %")
        ).count()

        if existing_demo > 0:
            print(
                f"\nFound {existing_demo} existing HH Demo products."
            )
            print("No new demo products were inserted.")
            print("This prevents duplicate products.")
            return

        total_inserted = 0

        for category_name, config in CATEGORY_CONFIG.items():

            category = Category.query.filter_by(
                name=category_name
            ).first()

            if not category:
                print(
                    f"\nERROR: Category not found: {category_name}"
                )
                print("Check your categories table before continuing.")
                return

            images = get_images(config["folder"])

            required = config["count"]

            if len(images) < required:
                print(
                    f"\nERROR: {category_name} needs "
                    f"{required} images but only {len(images)} found."
                )
                print(
                    f"Folder: {IMAGE_DIR / config['folder']}"
                )
                return

            print(
                f"{category_name}: {len(images)} images found. "
                f"Using first {required}."
            )

            for index in range(required):

                product_name, description = config["products"][index]

                image_file = images[index]

                relative_image = (
                    f"images/{config['folder']}/{image_file.name}"
                )

                product = Product(
                    entrepreneur_id=entrepreneur.id,
                    category_id=category.id,
                    name=f"HH Demo - {product_name}",
                    description=description,
                    price=round(150 + ((index + 1) * 75), 2),
                    stock=10 + index,
                    image_url=relative_image,
                    status="ACTIVE"
                )

                db.session.add(product)
                total_inserted += 1

        db.session.commit()

        print("\n========================================")
        print("PRODUCT SEEDING COMPLETED")
        print("========================================")
        print(f"Products inserted: {total_inserted}")
        print("Expected products: 105")
        print("Images assigned: 105")
        print("========================================\n")

if __name__ == "__main__":
    main()
