DROP DATABASE IF EXISTS user_data;
CREATE DATABASE user_data;
use user_data;

-- Create tables and insert data here
CREATE TABLE users (
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- inserting values in the users table 
insert into users(username, password) 
    values('user1', 'pass1'),
    ('user2', 'pass2'),
    ('user3', 'pass3');