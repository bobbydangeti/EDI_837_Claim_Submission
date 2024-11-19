import mysql.connector

def get_connection():
    db_config = {
        'user': 'Bobby',
        'password': 'Djnvsbobby2022',
        'host': 'edi-837.cvoqeya8em6h.us-east-2.rds.amazonaws.com',
        'database': 'Edi-837schema',
    }

    try:
        connection = mysql.connector.connect(**db_config)
        print("Database connection successful!")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

