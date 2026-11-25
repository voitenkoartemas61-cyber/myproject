from flask import Flask, request, jsonify
import storage
import logic

app = Flask(__name__)
storage.init()


@app.get("/items")
def list_items():
    category = request.args.get("category")
    return jsonify(storage.load(category))


@app.post("/items")
def add_item():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "очікується JSON"}), 400

    for field in ("date", "category", "amount"):
        if field not in data or str(data[field]).strip() == "":
            return jsonify({"error": f"немає або порожнє поле {field}"}), 400

    try:
        amount = float(data["amount"])
    except (ValueError, TypeError):
        return jsonify({"error": "amount має бути числом"}), 400

    new_id = storage.add(
        str(data["date"]).strip(),
        str(data["category"]).strip(),
        amount,
        str(data.get("note", "")).strip()
    )
    return jsonify({"id": new_id}), 201


@app.delete("/items/<int:item_id>")
def delete_item(item_id):
    if storage.delete(item_id):
        return jsonify({"deleted": item_id})
    return jsonify({"error": "не знайдено"}), 404


@app.get("/report")
def report():
    return jsonify(logic.total_by_category(storage.load()))


if __name__ == "__main__":
    app.run(debug=True)
