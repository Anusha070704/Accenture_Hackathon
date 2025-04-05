from flask import Flask, jsonify
from flask_cors import CORS
from customer_agent import CustomerAgent
from product_agent import ProductAgent
from recommendation_engine import RecommendationEngineAgent

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests from your frontend

@app.route("/customer/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer_agent = CustomerAgent(customer_id)
    if not customer_agent.profile:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify(customer_agent.profile)

@app.route("/recommend/<customer_id>", methods=["GET"])
def get_recommendations(customer_id):
    customer_agent = CustomerAgent(customer_id)
    if not customer_agent.profile:
        return jsonify({"error": "Customer not found"}), 404

    rec_engine = RecommendationEngineAgent()
    recommendations = rec_engine.recommend(customer_agent.profile)

    products = []
    for product_id in recommendations:
        product_agent = ProductAgent(product_id)
        details = product_agent.details
        products.append({
            "Product_ID": details["Product_ID"],
            "Category": details["Category"],
            "Brand": details["Brand"],
            "Price": details["Price"]
        })

    return jsonify({"recommendations": products})

if __name__ == "__main__":
    app.run(debug=True)
