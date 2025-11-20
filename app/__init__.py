from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return jsonify(message="Hello from Flask sample app")

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    return app