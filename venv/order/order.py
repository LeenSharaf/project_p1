from flask import Flask, jsonify
app = Flask(__name__)
from catalog.catalog import Book
###### URL #######
catalog = '../catalog/catalog.py'
front = "http://localhost:5000"

orderBook = {}
 ####### purchase ######
 #########POST: http://localhost:5002/purchase/item_number #######

@app.route('/purchase/<int:item_number>', methods=['POST'])
def purchase(item_number):
    if item_number not in orderBook:
        orderBook[item_number] = 0
    
    if Book[item_number]['stock'] > 0: ##### Existing ####
        Book[item_number]['stock'] -= 1  #### decrease ####
        orderBook[item_number] += 1  ### order ++ ###
        return jsonify({"message": "Successful"})
    else:
        return jsonify({"error": "Sold Out"}), 400

if __name__ == '__main__':
    app.run(port = 5002, debug = True)
