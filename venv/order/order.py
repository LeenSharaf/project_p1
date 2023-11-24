from flask import Flask, jsonify,request
import requests
app = Flask(__name__)
from catalog.catalog import Book
###### URL #######
catalog = "http://localhost:5001"
front = "http://localhost:5000"

 ####### purchase ######
 ######### PUT: http://localhost:5002/purchase/item_number #######

@app.route('/purchase/<int:item_number>', methods=['PUT'])
def purchase(item_number):
    book_response = requests.get(f'{catalog}/query-by-item/{item_number}')
    if book_response.status_code == 404:
         return jsonify({"Error":'Book does not exist'}), 404
    elif book_response.status_code != 200:
        return book_response.content, book_response.status_code, book_response.headers.items()
    book = book_response.json()

    # If the stock is 0
    if book['stock'] <= 0:
        return jsonify({"Error": "Book Sold Out"})
    
    purchase_resp = requests.put(f'{catalog}/update/{item_number}', json={'stock': book['stock']-1})
    if purchase_resp.status_code != 200:
        return purchase_resp.text, purchase_resp.status_code, purchase_resp.headers.items()
    
    return jsonify({"Message": "Successful"})

if __name__ == '__main__':
    app.run(port = 5002, debug = True)

















