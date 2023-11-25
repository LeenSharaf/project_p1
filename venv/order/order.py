from flask import Flask, jsonify
import csv
import requests
from datetime import datetime

app = Flask(__name__)

catalog = "http://localhost:5001"
order_url= "order_log.csv"

def update_order_log(order):
    fieldnames = ['ItemNumber', 'Title', 'Status','Time']
    # order['Time'] = datetime.now().strftime("%H:%M:%S")

    try:
        with open(order_url, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(order)

    except Exception as e:
        print(f"Error writing : {e}")

@app.route('/purchase/<int:item_number>', methods=['POST'])
def purchase(item_number):
    try:
        #### Query by item to catalog server #####
        catalog_response = requests.get(f"{catalog}/query-by-item/{item_number}")
        ### Error ###
        if catalog_response.status_code == 404:
            return jsonify({"Error": "Not found"}), 404

        catalog_data = catalog_response.json()
        current_stock = int(catalog_data.get('stock', 0))
        title = catalog_data.get('title', '')
        ######## Exist Book "book not sold out" ######
        if current_stock > 0:
            updated_stock = current_stock - 1 ##### Decrease stock ######
            ######### Query update-stock to catalog server #######
            update_response = requests.put(f"{catalog}/update-stock/{item_number}",
                                           json={"new_stock": updated_stock})
            #### Ok #####
            if update_response.status_code == 200:
                time = datetime.now().strftime("%H:%M:%S")
                # Successfull update stock ####
                order = {'ItemNumber': item_number, 'Title': title, 'Status': 'Purchase Successful', 'Time': time }   
                ## update ##
                update_order_log(order)
                return jsonify(order), 200
            else:
                # Failed update stock
                return jsonify({"Error": "Failed to update stock"}), 500
        else:
            time = datetime.now().strftime("%H:%M:%S")
            order = {'ItemNumber': item_number, 'Title': title, 'Status': 'Sold out', 'Time': time } 
            update_order_log(order)
            ##### Item sold out ####
            return jsonify({"Error": "Item sold out "}), 400
        
    except Exception as e:
        return jsonify({"Error": "Error"}), 500



if __name__ == '__main__':
    app.run(port=5002,debug=True)  # Adjust the port as needed
