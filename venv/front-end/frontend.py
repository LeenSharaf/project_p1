from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

catalog = "http://localhost:5001"
order = "http://localhost:5002"

###### Search ######
#######  Get :  http://localhost:5000/search/TopicName #########

@app.route('/search/<topic>', methods=['GET'])
def search(topic):
    response = requests.get(f"{catalog}/query-by-subject/{topic}")
    ### ok ###
    if response.status_code == 200:
        catalogitem = response.json()["items"]
        return jsonify({"items": catalogitem})
    else:
        return jsonify({"error": "Not Found"}),response.status_code

######## info ########
########  Get : http://localhost:5000/info/item_number ##########

@app.route('/info/<int:item_number>', methods=['GET'])
def info(item_number):
    response = requests.get(f"{catalog}/query-by-item/{item_number}")
    #### if i found the book ####
    if response.status_code == 200:
        infoItem = response.json()
        return jsonify(infoItem)
    else:
        return jsonify({"error": "Not Found"}), response.status_code

###### purchase #######
##### Post http://localhost:5000/purchase/item_number

@app.route('/purchase/<int:item_number>', methods=['POST'])
def purchase(item_number):
    response = requests.get(f"{catalog}/query-by-item/{item_number}")
    
    if response.status_code == 200:
        infoItem = response.json()
        if infoItem['stock'] > 0:  ##### Exist #####
            purchaseitem = requests.post(f"{order}/purchase/{item_number}")
            ######## ok ###########
            if purchaseitem.status_code == 200:
                return jsonify({"message": "Successful"})
            else:
                return jsonify({"error": "Error"}), purchaseitem.status_code
        else:
            return jsonify({"error": "Sold Out"}), purchaseitem.status_code
    else:
        return jsonify({"error": "Error in purchase"}), response.status_code

if __name__ == '__main__':
    app.run(port=5000, debug=True)
