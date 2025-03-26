	CREATE TABLE users (
	    id SERIAL PRIMARY KEY,
	    username VARCHAR(50) UNIQUE NOT NULL,
	    password TEXT NOT NULL,  -- Store hashed passwords for security
	    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);
	
	CREATE TABLE categories (
	    id SERIAL PRIMARY KEY,
	    name VARCHAR(50) UNIQUE NOT NULL
	);
	
	INSERT INTO categories (name) VALUES 
	('Food'), 
	('Transport'), 
	('Entertainment'), 
	('Health'), 
	('Utilities'), 
	('Others');
	
	CREATE TABLE expenses (
	    id SERIAL PRIMARY KEY,
	    user_id INT REFERENCES users(id) ON DELETE CASCADE,
	    amount DECIMAL(10,2) NOT NULL,
	    category_id INT REFERENCES categories(id) ON DELETE SET NULL,
	    description TEXT,
	    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);
	
	INSERT INTO users (username, password) VALUES ('siddharth', 'hashed_password');
	SELECT id FROM users WHERE username = 'siddharth';
	
	INSERT INTO expenses (user_id, amount, category_id, description) 
	VALUES (1, 500.00, 1, 'Dinner at a restaurant');
	
	SELECT column_name, data_type
	FROM information_schema.columns
	WHERE table_name = 'expenses';
	
	
	SELECT * FROM expenses;
