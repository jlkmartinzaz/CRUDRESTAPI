from flask import Flask, request, jsonify
from dataclasses import dataclass, asdict
from typing import List, Optional

app = Flask(__name__)

@dataclass
class Item:
    id: int
    name: str
    description: str

items: List[Item] = []
next_id: int = 1


def create_item(name: str, description: str) -> Item:
    global next_id
    item = Item(id=next_id, name=name, description=description)
    items.append(item)
    next_id += 1
    return item

def find_item(item_id: int) -> Optional[Item]:
    return next((item for item in items if item.id == item_id), None)


# CREATE (JSON en el body)
@app.route("/items", methods=["POST"])
def api_create_item():
    data = request.get_json(force=True)  # lee JSON del body
    name = data.get("name")
    description = data.get("description")

    if not name or not description:
        return jsonify({"error": "Both 'name' and 'description' are required"}), 400

    item = create_item(name, description)
    return jsonify(asdict(item)), 201


# READ ALL
@app.route("/items", methods=["GET"])
def api_read_items():
    return jsonify([asdict(item) for item in items])


# READ ONE
@app.route("/items/<int:item_id>", methods=["GET"])
def api_read_item(item_id: int):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(asdict(item))


# UPDATE (JSON en el body)
@app.route("/items/<int:item_id>", methods=["PUT"])
def api_update_item(item_id: int):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json(force=True)
    name = data.get("name")
    description = data.get("description")

    if name:
        item.name = name
    if description:
        item.description = description

    return jsonify(asdict(item))


# DELETE
@app.route("/items/<int:item_id>", methods=["DELETE"])
def api_delete_item(item_id: int):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    items.remove(item)
    return jsonify({"message": f"Item {item_id} deleted"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
