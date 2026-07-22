import os
from typing import Dict

from flask import Flask, jsonify, request

app = Flask(__name__)

config_store: Dict[str, str] = {}


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/version")
def version():
    return jsonify({"version": "1.0.0"})


@app.get("/env")
def env():
    return jsonify({"environment": os.getenv("ENVIRONMENT", "dev")})


@app.post("/config")
def create_config():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    value = payload.get("value")

    if not name or not value:
        return jsonify({"error": "name and value are required"}), 400

    config_store[name] = value
    return jsonify({"name": name, "value": value})


@app.get("/config/<name>")
def get_config(name: str):
    value = config_store.get(name)
    if value is None:
        return jsonify({"error": "config not found"}), 404
    return jsonify({"name": name, "value": value})


@app.delete("/config/<name>")
def delete_config(name: str):
    if name in config_store:
        del config_store[name]
    return jsonify({"deleted": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
