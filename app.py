from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Test Task. Maister Danylo"

def load_products():
    """Loads product data from the JSON file"""
    with open('products.json', 'r', encoding='utf-8') as f:
        return json.load(f)

products = load_products()

@app.route('/all_products/', methods=['GET'])
def get_all_products():
    """Returns all products"""
    return jsonify(products)

@app.route('/products/<string:product_name>', methods=['GET'])
def get_product(product_name):
    """Returns a specific product by name"""
    product_name_formatted = product_name.replace('_', ' ')
    for product in products:
        if product.get('name', '').lower() == product_name_formatted.lower():
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/<string:product_name>/<string:product_field>', methods=['GET'])
def get_product_field(product_name, product_field):
    """Returns a specific field of a specific product"""
    product_name_formatted = product_name.replace('_', ' ')
    for product in products:
        if product.get('name', '').lower() == product_name_formatted.lower():
            if product_field in product:
                return jsonify({product_field: product[product_field]})
            else:
                return jsonify({"error": f"Field '{product_field}' not found for this product"}), 404
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)