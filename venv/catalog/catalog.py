from flask import Flask, request, jsonify

app = Flask(__name__)
 ###### URL####
front = "http://localhost:5000"
order = "http://localhost:5002"

Book = {
    1: {"title": "How to get a good grade in DOS in 40 minutes a day", "stock": 10, "cost": 70, "topic": "distributed systems"},
    2: {"title": "RPCs for Noobs", "stock": 15, "cost": 80, "topic": "distributed systems"},
    3: {"title": "Xen and the Art of Surviving Undergraduate School", "stock": 35, "cost": 75, "topic": "undergraduate school"},
    4: {"title": "Cooking for the Impatient Undergrad", "stock": 18, "cost": 60, "topic": "undergraduate school"},
}
###### query-by-subject ######
####### GET http://localhost:5001/query-by-subject/TopicName #####

@app.route('/query-by-subject/<topic>', methods=['GET'])
def query_by_subject(topic):
    res = [Item for Item in Book.values() if topic.lower() in Item['topic'].lower()]
    return jsonify({"items": res})

###### query-by-item ######
####### GET http://localhost:5001/query-by-item/item_number #####

@app.route('/query-by-item/<int:item_number>', methods=['GET'])
def query_by_item(item_number):

    if item_number not in Book:
        return jsonify({"error": "Not found"}), 404
    
### I found book #####
    Item = Book[item_number]
    return jsonify({"title": Item['title'], "stock": Item['stock'], "cost": Item['cost'], 
                    "topic": Item['topic']})

####### Update #####
#### Put: http://localhost:5001/update/item_number ####

@app.route('/update/<int:item_number>', methods=['PUT'])
def update(item_number):
    if item_number not in Book:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()

    if 'cost' in data:
        Book[item_number]['cost'] = data['cost']
    if 'stock' in data:
        Book[item_number]['stock'] += data['stock']
    return jsonify({"message": "Successful"})

if __name__ == '__main__':
    app.run(port = 5001, debug = True)
