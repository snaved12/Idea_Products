import os
from flask import Flask, render_template, abort
from flask import send_from_directory

app = Flask(__name__)

# Product data as a list of dictionaries
products = [
    {"id": "1", "name": "iPhone 14", "category": "Mobile Phones & Accessories", "image": "iphone_14.jpeg", "price": "999"},
    {"id": "2", "name": "Samsung Galaxy S23", "category": "Mobile Phones & Accessories", "image": "samsung_galaxy_s23.jpg", "price": "899"},
    {"id": "3", "name": "OnePlus 11 Pro", "category": "Mobile Phones & Accessories", "image": "oneplus_11_pro.jpeg", "price": "799"},
    {"id": "4", "name": "iPhone 14 Case", "category": "Mobile Phones & Accessories", "image": "iphone_14_case.jpeg", "price": "20"},
    {"id": "5", "name": "Samsung Galaxy S23 Screen Guard", "category": "Mobile Phones & Accessories", "image": "samsung_s23_glass.jpeg", "price": "15"},
    {"id": "6", "name": "OnePlus 11 Pro Case", "category": "Mobile Phones & Accessories", "image": "oneplus_11_pro_case.jpeg", "price": "25"},
    {"id": "7", "name": "AirPods Pro", "category": "Mobile Phones & Accessories", "image": "airpods_pro.jpeg", "price": "249"},
    {"id": "8", "name": "Samsung Galaxy Buds 2", "category": "Mobile Phones & Accessories", "image": "samsung_buds_2.jpeg", "price": "199"},
    {"id": "9", "name": "20W Fast Charger", "category": "Mobile Phones & Accessories", "image": "20w_charger.jpeg", "price": "30"},
    {"id": "10", "name": "Wireless Charging Pad", "category": "Mobile Phones & Accessories", "image": "wireless_charge.jpg", "price": "40"},
    {"id": "11", "name": "iPhone 13", "category": "Mobile Phones & Accessories", "image": "iphone_13.jpeg", "price": "899"},
    {"id": "12", "name": "Samsung Galaxy A54", "category": "Mobile Phones & Accessories", "image": "samsung_a54.jpeg", "price": "499"},
    {"id": "13", "name": "OnePlus Nord 3", "category": "Mobile Phones & Accessories", "image": "oneplus_nord3.jpeg", "price": "399"},
    {"id": "14", "name": "Google Pixel 7", "category": "Mobile Phones & Accessories", "image": "google_7.jpeg", "price": "599"},
    {"id": "15", "name": "Apple MagSafe Charger", "category": "Mobile Phones & Accessories", "image": "apple_magsafe.jpeg", "price": "45"},
    {"id": "16", "name": "Samsung 25W Super Fast Charger", "category": "Mobile Phones & Accessories", "image": "samsung_fast.jpeg", "price": "35"},
    {"id": "17", "name": "OnePlus Warp Charger 65W", "category": "Mobile Phones & Accessories", "image": "oneplus_fast.jpeg", "price": "50"},
    {"id": "18", "name": "Sony WH-1000XM5 Headphones", "category": "Mobile Phones & Accessories", "image": "sony_wh.jpeg", "price": "350"},
    {"id": "19", "name": "Bose QuietComfort Earbuds", "category": "Mobile Phones & Accessories", "image": "bose_ear.jpeg", "price": "299"},
    {"id": "20", "name": "iPhone 14 Pro Max", "category": "Mobile Phones & Accessories", "image": "iphone_14_promax.jpeg", "price": "1099"},
    {"id": "21", "name": "Samsung Galaxy Z Fold 5", "category": "Mobile Phones & Accessories", "image": "samsung_fold.jpeg", "price": "1799"},
    {"id": "22", "name": "OnePlus 10R", "category": "Mobile Phones & Accessories", "image": "oneplus_10r.jpeg", "price": "449"},
    {"id": "23", "name": "iPhone 12 Mini", "category": "Mobile Phones & Accessories", "image": "iphone_12_mini.jpg", "price": "699"},
    {"id": "24", "name": "Google Pixel Buds Pro", "category": "Mobile Phones & Accessories", "image": "pixel_ear.jpeg", "price": "199"},
    {"id": "25", "name": "Apple Watch Series 8", "category": "Mobile Phones & Accessories", "image": "apple_watch8.jpeg", "price": "429"},
    {"id": "51", "name": "Nike Air Max", "category": "Shoes & Accessories", "image": "nike_air_max.jpeg", "price": "150"},
    {"id": "52", "name": "Adidas Ultraboost", "category": "Shoes & Accessories", "image": "ultraboost.jpeg", "price": "180"},
    {"id": "53", "name": "Puma Sneakers", "category": "Shoes & Accessories", "image": "puma_snks.jpeg", "price": "120"},
    {"id": "54", "name": "Shoe Cleaning Kit", "category": "Shoes & Accessories", "image": "shoe_clean.jpeg", "price": "25"},
    {"id": "55", "name": "Nike Ankle Socks (Pack of 3)", "category": "Shoes & Accessories", "image": "nike_socks3.jpeg", "price": "15"},
    {"id": "56", "name": "Adidas Crew Socks", "category": "Shoes & Accessories", "image": "adidas_crew.jpeg", "price": "18"},
    {"id": "57", "name": "Shoe Deodorizer Spray", "category": "Shoes & Accessories", "image": "feet_spray.jpeg", "price": "12"},
    {"id": "58", "name": "Memory Foam Insoles", "category": "Shoes & Accessories", "image": "memory_foam.jpg", "price": "20"},
    {"id": "59", "name": "Shoe Laces (White, Black)", "category": "Shoes & Accessories", "image": "laces.jpeg", "price": "10"},
    {"id": "60", "name": "Waterproof Shoe Cover", "category": "Shoes & Accessories", "image": "shoes_cover.jpeg", "price": "30"},
    {"id": "61", "name": "Reebok Running Shoes", "category": "Shoes & Accessories", "image": "reebok_run.jpeg", "price": "110"},
    {"id": "62", "name": "Skechers Walking Shoes", "category": "Shoes & Accessories", "image": "skechers_walk.jpeg", "price": "140"},
    {"id": "63", "name": "Fila Sports Shoes", "category": "Shoes & Accessories", "image": "fila_shoes.jpeg", "price": "100"},
    {"id": "64", "name": "Nike Basketball Shoes", "category": "Shoes & Accessories", "image": "nike_basket.jpeg", "price": "200"},
    {"id": "65", "name": "Adidas Football Cleats", "category": "Shoes & Accessories", "image": "adidas_football.jpeg", "price": "220"},
    {"id": "66", "name": "Puma Gym Shoes", "category": "Shoes & Accessories", "image": "puma_gym.jpeg", "price": "130"},
    {"id": "67", "name": "Shoe Polish Kit", "category": "Shoes & Accessories", "image": "polish.jpeg", "price": "20"},
    {"id": "68", "name": "Shoe Freshener Balls", "category": "Shoes & Accessories", "image": "ded_ball.jpeg", "price": "15"},
    {"id": "69", "name": "High-Performance Shoe Insoles", "category": "Shoes & Accessories", "image": "insoles.jpeg", "price": "35"},
    {"id": "70", "name": "Premium Leather Shoe Laces", "category": "Shoes & Accessories", "image": "leather_lace.jpeg", "price": "18"},
    {"id": "71", "name": "Boot Socks (Wool Blend)", "category": "Shoes & Accessories", "image": "wool_socks.jpeg", "price": "25"},
    {"id": "72", "name": "Casual Slip-On Sneakers", "category": "Shoes & Accessories", "image": "slipon.jpeg", "price": "85"},
    {"id": "73", "name": "Orthopedic Shoe Inserts", "category": "Shoes & Accessories", "image": "ortho_ins.jpeg", "price": "40"},
    {"id": "74", "name": "UltraGrip Football Socks", "category": "Shoes & Accessories", "image": "football_socks.jpeg", "price": "22"},
    {"id": "75", "name": "Shoe Storage Organizer", "category": "Shoes & Accessories", "image": "shoe_box.jpeg", "price": "50"}

]


@app.route('/product/<string:id>')
def get_product_page(id):
    # Find the product with the matching ID
    product = next((product for product in products if product['id'] == id), None)
    
    # If product not found, return a 404 error
    if product is None:
        abort(404)
    
    # Render the product page with the found product details
    return render_template('product_page.html', 
                           id=product['id'], 
                           name=product['name'], 
                           category=product['category'], 
                           image=product['image'], 
                           price=product['price'])

@app.route('/')
def index():
    return render_template('index.html', products=products)

# @app.route('/images/<filename>')
# def serve_image(filename):
#     return send_from_directory('static/images', filename)

@app.route('/images/<filename>')
def serve_image(filename):
    image_path = os.path.join(app.root_path, 'static/images', filename)
    print(f"Serving image from: {image_path}")

    if not os.path.exists(image_path):
        print("File not found!")
        abort(404)

    return send_from_directory('static/images', filename)



if __name__ == '__main__':
    app.run(debug=True)