import sqlite3
import json
from database import create_connection

class CustomerAgent:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.profile = self.load_profile()

    def load_profile(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE Customer_ID = ?", (self.customer_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return {
                'Customer_ID': result[0],
                'Age': result[1],
                'Gender': result[2],
                'Location': result[3],
                'Browsing_History': json.loads(result[4]),
                'Purchase_History': json.loads(result[5]),
                'Customer_Segment': result[6],
                'Avg_Order_Value': result[7],
                'Holiday': result[8],
                'Season': result[9]
            }
        return None

    def update_browsing_history(self, new_browsing_data):
        if self.profile:
            self.profile['Browsing_History'].append(new_browsing_data)
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE customers SET Browsing_History = ? WHERE Customer_ID = ?", 
                           (json.dumps(self.profile['Browsing_History']), self.customer_id))
            conn.commit()
            conn.close()

    def update_purchase_history(self, new_purchase_data):
        if self.profile:
            self.profile['Purchase_History'].append(new_purchase_data)
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE customers SET Purchase_History = ? WHERE Customer_ID = ?", 
                           (json.dumps(self.profile['Purchase_History']), self.customer_id))
            conn.commit()
            conn.close()

if __name__ == "__main__":
    agent = CustomerAgent("C1000")
    print("Customer Profile:", agent.profile)
