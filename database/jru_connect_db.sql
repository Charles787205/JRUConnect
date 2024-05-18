
DROP DATABASE jru_connect_db;

CREATE DATABASE jru_connect_db;
USE jru_connect_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    user_type enum('STUDENT', 'ADMIN') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE students (
    id INT NOT NULL PRIMARY KEY,
    student_number VARCHAR(255) NOT NULL,
    course VARCHAR(255) NOT NULL,
    year_level INT NOT NULL,
    FOREIGN KEY (id) REFERENCES users(id)
);
CREATE TABLE facilities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    seating_capacity INT NOT NULL,
    location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    facility_id INT NOT NULL,
    user_id INT NOT NULL,
    date_reserved DATE NOT NULL,
    time_from TIME NOT NULL,
    time_to TIME NOT NULL,
    notes TEXT,
    status enum('PENDING', 'APPROVED', 'REJECTED') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (facility_id) REFERENCES facilities(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);





INSERT INTO facilities (name, image_url, seating_capacity, location) VALUES ('New Auditorium', 'new_auditorium.png', 500, 'Centennial Building 9th Floor'), ('Old Auditorium', 'old_auditorium.png', 1000, 
'Main Campus'), ('Learning Commons', 'learning_commons.png', 2000, 'Main Campus'), ('Information Commons', 'information_commons.png', 200,'Centennial Building 2nd Floor');

INSERT INTO users (first_name, middle_name, last_name, email, password, user_type) VALUES ('John', 'Doe', 'Smith', 'johndoe@gmail.com', SHA2('password',256), 'ADMIN');