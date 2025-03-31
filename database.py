import sqlite3

DB_PATH = './Accenture Hackathon.db'


def create_connection():
    """Creates a database connection."""
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Create customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        Customer_ID TEXT PRIMARY KEY,
        Age INTEGER,
        Gender TEXT,
        Location TEXT,
        Browsing_History TEXT,
        Purchase_History TEXT,
        Customer_Segment TEXT,
        Avg_Order_Value REAL,
        Holiday TEXT,
        Season TEXT
    )
    ''')

    # Create products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        Product_ID TEXT PRIMARY KEY,
        Category TEXT,
        Subcategory TEXT,
        Price INTEGER,
        Brand TEXT,
        Average_Rating_of_Similar_Products REAL,
        Product_Rating REAL,
        Customer_Review_Sentiment_Score REAL,
        Holiday TEXT,
        Season TEXT,
        Geographical_Location TEXT,
        Similar_Product_List TEXT,
        Probability_of_Recommendation REAL
    )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully!")
