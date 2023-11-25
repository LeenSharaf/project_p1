
from flask import Flask, request, jsonify
import csv
from func_data import CatalogManager
app = Flask(__name__)
 ###### URL####
front = "http://localhost:5000"
order = "http://localhost:5002"
catalog_manager = CatalogManager()
catalog_data = catalog_manager.read()

### query-by-subject ######
####### GET http://localhost:5001/query-by-subject/TopicName #####

@app.route('/query-by-subject/<topic>', methods=['GET'])
def query_by_subject(topic):
    res = [Item for Item in catalog_data if topic.lower() in Item['topic'].lower()]
    return jsonify({"items": res})
    
###### query-by-item ######
####### GET http://localhost:5001/query-by-item/item_number #####
@app.route('/query-by-item/<int:item_id>', methods=['GET'])
def query_by_item(item_id):
    item = catalog_manager.get_item_by_id(item_id)

    if item is None:
        return jsonify({"Error": "Not found"}), 404

    return jsonify({
        "title": item['Title'],
        "stock": item['stock'],
        "cost": item['cost'],
        "topic": item['topic']
    })

####### Update #####
#### Put: http://localhost:5001/update-stock/item_number ####

@app.route('/update-stock/<int:item_id>', methods=['PUT'])
def update_stock(item_id):
    new_stock = request.json.get('new_stock')
    updated_item = catalog_manager.update_stock(item_id, new_stock)

    if updated_item:
        return jsonify({"Message": "Stock updated successfully","item": updated_item})
    else:
        return jsonify({"Error": "Not found"}), 404
    
####### Update #####
#### Put:  http://localhost:5001/update-cost/item_number ####

@app.route('/update-cost/<int:item_id>', methods=['PUT'])
def update_cost(item_id):
    new_cost = request.json.get('new_cost')
    updated_item = catalog_manager.update_cost(item_id, new_cost)

    if updated_item:
        return jsonify({"Message": "Cost updated successfully","item": updated_item})
    else:
        return jsonify({"Error": "Not found"}), 404
    
####### Update #####
#### Put:  http://localhost:5001/update-stock-and-cost/item_number ####

@app.route('/update-stock-and-cost/<int:item_id>', methods=['PUT'])
def update_stock_and_cost(item_id):
    new_stock = request.json.get('new_stock')
    new_cost = request.json.get('new_cost')
    updated_item = catalog_manager.update_stock_and_cost(item_id, new_stock, new_cost)

    if updated_item:
        return jsonify({"Message": "Stock and Cost updated successfully", "item": updated_item})
    else:
        return jsonify({"Error": "Not found"}), 404


if __name__ == '__main__':
    app.run(port = 5001, debug = True)
