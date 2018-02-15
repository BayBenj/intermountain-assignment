
DROP TABLE customer;
DROP TABLE item;
DROP TABLE purchase;
DROP TABLE customer_purchases;

CREATE TABLE customer (
	id INT PRIMARY KEY NOT NULL,
	name VARCHAR(25),
	email VARCHAR(25)
);

CREATE TABLE item (
	id INT PRIMARY KEY NOT NULL,
	name VARCHAR(25),
	price FLOAT);

CREATE TABLE customer_purchases (
	purchaseID INT REFERENCES purchase(id),
	customerID INT REFERENCES customer(id),
	CONSTRAINT CustomerPurchases PRIMARY KEY (purchaseID, customerID)
);

CREATE TABLE purchase (
	id INT PRIMARY KEY NOT NULL,
	item_id INTEGER,
	the_time TIMESTAMP
);


















--
