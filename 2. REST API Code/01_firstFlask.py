from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores =[
    {
    'name': "thucphamsach",
    'items': [
            {
            'name': "Rau Muong",
            'price': 2
            }
        ]
    },
    {
    'name': "thegioididong",
    'items': [
            {
            'name': "Iphone 13",
            'price': 500
            }
        ]
    },
]



@app.route('/')
def home():
    return render_template('index.html')


#POST /store data:{name:}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route("/store/<string:name>") #.../store/some_name
def get_store(name): #name = some_name
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return jsonify({'message:':'store not found'})        

#GET /store
@app.route("/store") 
def get_stores():
    return jsonify({'stores': stores})


#POST /store/<string:name>/item {name: , price: }
@app.route("/store/<string:name>/items", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if name == store['name']:   
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message:':'store not found'}) 
    


#GET /store/<string:name>/item
@app.route("/store/<string:name>/items")
def get_items_in_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify({'items': store['items']})
    return jsonify({'message:':'store not found'})      




app.run(port = 5000)