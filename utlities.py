import sqlite3
import pandas as pd
import json
from database import create_connection


def load_customer_data(csv_path):
    df = pd.read_csv(csv_path)
    conn = create_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            row['Customer_ID'], row['Age'], row['Gender'], row['Location'],
            json.dumps(row['Browsing_History'].split(',')), json.dumps(row['Purchase_History'].split(',')),
            row['Customer_Segment'], row['Avg_Order_Value'], row['Holiday'], row['Season']
        ))
    conn.commit()
    conn.close()


def load_product_data(csv_path):
    df = pd.read_csv(csv_path)
    conn = create_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        
        cursor.execute("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            row['Product_ID'], row['Category'], row['Subcategory'], row['Price'], row['Brand'],
            row['Average_Rating_of_Similar_Products'], row['Product_Rating'], row['Customer_Review_Sentiment_Score'],
            row['Holiday'], row['Season'], row['Geographical_Location'], row['Similar_Product_List'],
            row['Probability_of_Recommendation']
        ))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    load_customer_data('C:/Users/Anusha07/Desktop/Placements/Python in BioInfo/Accenture Hackathon/data/customer_data_collection.csv')
    load_product_data('C:/Users/Anusha07/Desktop/Placements/Python in BioInfo/Accenture Hackathon/data/product_recommendation_data.csv')
    print("Data loaded successfully!")
