import uuid
from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores


blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:    
            if store_id in stores:
                return stores[store_id]
        except KeyError:
            abort(404, message="Store not found!")
    
    def delete(self, store_id):
        try:    
            if store_id in stores:
                del stores[store_id]
                return {"message", "Store deleted."}
        except KeyError:
            abort(404, message="Store not found!")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}
    
    def post(self):
        # Todo: Add Validations
        store_data = request.get_json()
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store

        return store
