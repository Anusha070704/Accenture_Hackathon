import sqlite3
from database import create_connection

class RecommendationEngineAgent:
    def __init__(self):
        pass

    def recommend(self, customer_profile):
        recommended_products = []
        conn = create_connection()
        cursor = conn.cursor()

        segment = customer_profile['Customer_Segment']
        browsing_history = customer_profile['Browsing_History']

        # Recommend products based on browsing history and segment
        for category in browsing_history:
            category=category.strip("[]' ")
            cursor.execute("SELECT Product_ID FROM products WHERE Category = ? ORDER BY Probability_of_Recommendation DESC LIMIT 5", (category,))
            recommended_products.extend([row[0] for row in cursor.fetchall()])

        # Fallback recommendation based on customer segment if browsing history is empty
        if not recommended_products:
            cursor.execute("SELECT Product_ID FROM products WHERE Category = ? ORDER BY Probability_of_Recommendation DESC LIMIT 5", (segment,))
            recommended_products.extend([row[0] for row in cursor.fetchall()])

        conn.close()
        return recommended_products

if __name__ == "__main__":
    from customer_agent import CustomerAgent
    customer_id = "C1000"
    customer_agent = CustomerAgent(customer_id)
    rec_engine = RecommendationEngineAgent()
    recommendations = rec_engine.recommend(customer_agent.profile)
    print(f"Recommendations for Customer {customer_id}: {recommendations}")
