import uuid
from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items


blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:    
            if item_id in items:
                return items[item_id]
        except KeyError:
            abort(404, message="Item not found!")
    
    def delete(self, item_id):
        try:    
            if item_id in items:
                del items[item_id]
                return {"message", "Item deleted."}
        except KeyError:
            abort(404, message="Item not found!")


    def put(self, item_id):
        # Todo: Add validation
        item_data = request.get_json()
        updated_item = {
            "name": item_data["name"],
            "price": item_data["price"]
        }
        items[item_id] = updated_item
        return updated_item


