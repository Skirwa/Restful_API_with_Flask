from flask import Flask, jsonify, request, render_template

app = Flask(__name__) #Creating an application. __name__ gives the app a unique name

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]
@app.route('/')         #Tell the app what request it's going to understand
def home():
    return render_template('index.html')

#Post is used to receive data (the user receives data)
#GET is used to send data back only (the user is requested to send data)

#the end points are;
#POST /store data: {name:}   - creates a new store with a given name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>    - get a store for a given name and it will return data about it
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:             # Iterate over stores
        if store['name'] == name:    # If the store name matches, return it
            return jsonify(store)
    return jsonify({'message': 'store not found'}) # If there is no match, return an error message

#GET /store                  - returns a list of all the stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

#POST /store/<string:name>/item  {name:, price:} - create an item inside a specific store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({'message': 'store not found'})

#GET /store/<string:name>/item   - get all the items in a specific store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})

app.run(port=5000) #import flask, create an object of flask, create a route, assign a method to the route which returns something which goes to the bropwser, then run the app
  