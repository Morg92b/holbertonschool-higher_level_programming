from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data():
    try:
        with open('products.json') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: products.json file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: JSON data is malformed.")
        return []

def read_csv_data():
    products = []
    try:
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
                products.append(product)
    except FileNotFoundError:
        print("Error: products.csv file not found.")
    except csv.Error:
        print("Error: CSV data is malformed.")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == "json":
        products = read_json_data()
    elif source == "csv":
        products = read_csv_data()
    else:
        return render_template('product_display.html', error_message="Wrong source specified.")

    if product_id is not None:
        products = [product for product in products if product["id"] == product_id]
        if not products:
            return render_template('product_display.html', error_message="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)