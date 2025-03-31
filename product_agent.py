import sqlite3
from database import create_connection

class ProductAgent:
    def __init__(self, product_id):
        self.product_id = product_id
        self.details = self.load_details()

    def load_details(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE Product_ID = ?", (self.product_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return {
                'Product_ID': result[0],
                'Category': result[1],
                'Subcategory': result[2],
                'Price': result[3],
                'Brand': result[4],
                'Average_Rating': result[5],
                'Product_Rating': result[6],
                'Sentiment_Score': result[7],
                'Holiday': result[8],
                'Season': result[9],
                'Location': result[10],
                'Similar_Products': result[11],
                'Recommendation_Probability': result[12]
            }
        return None

    def update_rating(self, new_rating):
        if self.details:
            self.details['Product_Rating'] = new_rating
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET Product_Rating = ? WHERE Product_ID = ?", 
                           (new_rating, self.product_id))
            conn.commit()
            conn.close()

if __name__ == "__main__":
    product_agent = ProductAgent("P1000")
    print("Product Details:", product_agent.details)
