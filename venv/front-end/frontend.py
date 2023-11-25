from flask import Flask, jsonify
import requests

app = Flask(__name__)

catalog = "http://localhost:5001"
order = "http://localhost:5002"

###### Search ######
#######  GET:  http://localhost:5000/search/TopicName #########

@app.route('/search/<topic>', methods=['GET'])
def search(topic):
    response = requests.get(f"{catalog}/query-by-subject/{topic}")
    ### ok ###
    if response.status_code == 200:
        catalogitem = response.json()["items"]
        return jsonify({"Items": catalogitem})
    else:
        return jsonify({"Error": "Not Found"}),response.status_code

######## info ########
########  GET : http://localhost:5000/info/item_number ##########

@app.route('/info/<int:item_number>', methods=['GET'])
def info(item_number):
    response = requests.get(f"{catalog}/query-by-item/{item_number}")
    #### if i found the book ####
    if response.status_code == 200:
        infoItem = response.json()
        return jsonify(infoItem)
    else:
        return jsonify({"Error": "Not Found"}), response.status_code

###### purchase #######
##### POST http://localhost:5000/purchase/item_number

@app.route('/purchase/<int:item_number>', methods=['POST'])
def purchase(item_number):
     #### go to order server #####
    response = requests.post(f'{order}/purchase/{item_number}')

    return response.text, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(port=5000, debug=True)


