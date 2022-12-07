import uuid
from flask import Flask, request

app = Flask(__name__)

stores = {}
items = {}


@app.post("/store")
def create_store():
    requestData = request.get_json()
    newStoreId = uuid.uuid4().hex
    new_store = {"id": newStoreId, "name": requestData["name"]}
    stores[newStoreId] = new_store
    return new_store, 201


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.get("/item/<string:id>")
def get_item(id):
    try:
        return items[id]
    except KeyError:
        return {"message": "Item not found"}, 404


@app.post("/item")
def create_item():
    request_data = request.get_json()
    new_item_id = uuid.uuid4().hex
    new_item = {
        "name": request_data["name"],
        "price": request_data["price"],
        "store_id": request_data["store_id"],
    }
    items[new_item_id] = new_item
    return new_item


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/store_item/<string:store_id>")
def get_store_items(store_id):
    try:
        store_items = []
        for item in items:
            if items[item]['store_id'] == store_id:
                store_items.append(items[item])
        return store_items
    except KeyError:
        return {"message": "Store items not found"}, 404


@app.get("/store/<string:id>")
def get_store(id):
    try:
        return stores[id]
    except KeyError:
        return {"message": "Store not found"}, 404

