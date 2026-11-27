from database.connection import DatabaseConnection

def createTables():
    """Creation of Tables"""
    try:
        db_config = DatabaseConnection()
        cursor = db_config.cursor()
        users_table_query = """
        CREATE TABLE IF NOT EXISTS USERS(
            USERID BIGINT AUTO_INCREMENT PRIMARY KEY,
            USERNAME VARCHAR(50) NOT NULL,
            EMAIL VARCHAR(50) NOT NULL UNIQUE,
            HASHPASSWORD VARCHAR(255) NOT NULL,
            ROLE ENUM('ADMIN','USER') DEFAULT 'ADMIN',
            GENDER ENUM('MALE','FEMALE'),
            PHONE VARCHAR(20),
            DATEOFBIRTH DATE,
            PROFILENAME VARCHAR(255),
            PROFILEPATH VARCHAR(255),
            IS_ACTIVE BOOLEAN DEFAULT TRUE,
            IS_VERIFIED BOOLEAN DEFAULT FALSE,
            OTP_HASH CHAR(64) NULL,
            OTP_EXPIRES_AT DATETIME NULL,
            OTP_ATTEMPTS INT NOT NULL DEFAULT 0,
            CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );"""
        
        products_table_query = """
        CREATE TABLE IF NOT EXISTS PRODUCTS(
            PRODUCTID BIGINT AUTO_INCREMENT PRIMARY KEY,
            PRODUCTNAME VARCHAR(100) NOT NULL,
            DESCRIPTION TEXT,
            CATEGORY VARCHAR(50),
            QUANTITY INT UNSIGNED DEFAULT 0,
            BUYPRICE FLOAT(15, 2) DEFAULT 0.0,
            SALEPRICE FLOAT(15, 2) DEFAULT 0.0,
            IMGNAME VARCHAR(100),
            STOREDPATH VARCHAR(255),
            IS_ACTIVE BOOLEAN DEFAULT TRUE,
            CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );"""
        
        orders_table_query = """
        CREATE TABLE IF NOT EXISTS ORDERS(
            ORDERID BIGINT AUTO_INCREMENT PRIMARY KEY,
            USERID BIGINT,
            STATUS ENUM('PENDING','SHIPPED','DELIVERED','CANCELLED') DEFAULT 'PENDING',
            ADDRESS VARCHAR(255),
            CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (USERID) REFERENCES USERS(USERID)
        );"""
        
        orderdetails_table_query = """
        CREATE TABLE IF NOT EXISTS ORDER_DETAILS(
            ORDERID BIGINT,
            PRODUCTID BIGINT,
            QUANTITY INT UNSIGNED DEFAULT 1,
            PRICE FLOAT(15, 2) DEFAULT 0.0,
            SUBTOTAL FLOAT(15, 2) GENERATED ALWAYS AS (QUANTITY * PRICE) STORED,
            FOREIGN KEY (ORDERID) REFERENCES ORDERS(ORDERID),
            FOREIGN KEY (PRODUCTID) REFERENCES PRODUCTS(PRODUCTID)
        );"""
        
        payments_table_query = """
        CREATE TABLE IF NOT EXISTS PAYMENTS(
            PAYMENTID BIGINT AUTO_INCREMENT PRIMARY KEY,
            USERID BIGINT,
            ORDERID BIGINT,
            METHOD ENUM('CASH','CARD','UPI','NETBANKING'),
            AMOUNT FLOAT(20, 2) DEFAULT 0.0,
            CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (USERID) REFERENCES USERS(USERID),
            FOREIGN KEY (ORDERID) REFERENCES ORDERS(ORDERID)
        );"""
        
        cart_table_query = """
        CREATE TABLE IF NOT EXISTS CART(
            CARTID BIGINT AUTO_INCREMENT PRIMARY KEY,
            USERID BIGINT,
            PRODUCTID BIGINT,
            QUANTITY INT DEFAULT 1,
            FOREIGN KEY (USERID) REFERENCES USERS(USERID),
            FOREIGN KEY (PRODUCTID) REFERENCES PRODUCTS(PRODUCTID)
        );"""
        
        tables = [
            users_table_query, 
            products_table_query, 
            orders_table_query, 
            orderdetails_table_query, 
            payments_table_query, 
            cart_table_query
        ]
        
        for table_query in tables:
            cursor.execute(table_query)
        
        
        # CREATE TABLE IF NOT EXISTS never alters a table that already
        # exists, so add the OTP columns to an older USERS table here.
        otp_columns = {
            "OTP_HASH": "CHAR(64) NULL",
            "OTP_EXPIRES_AT": "DATETIME NULL",
            "OTP_ATTEMPTS": "INT NOT NULL DEFAULT 0",
        }
        cursor.execute(
            """SELECT COLUMN_NAME FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'USERS'"""
        )
        existing = {row[0].upper() for row in cursor.fetchall()}
        for column, definition in otp_columns.items():
            if column not in existing:
                cursor.execute(
                    f"ALTER TABLE USERS ADD COLUMN {column} {definition}"
                )
        
        
        db_config.commit()
        cursor.close()
        db_config.close()
        return "Tables created successfully."
        
    except Exception as e:
        return f"Something went wrong in Database/tables.py: {e}"