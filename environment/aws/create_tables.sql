-- Use the appropriate database
USE foodsharehub;

CREATE TABLE FoodItemCategories (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE Attachments (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    FileName VARCHAR(255) NOT NULL,
    ContentType VARCHAR(255) NOT NULL,
    FileSize INT NOT NULL,
    FilePath VARCHAR(255) NOT NULL,
    PublicAccessURL VARCHAR(255) NOT NULL
);

CREATE TABLE FoodItems (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Description TEXT NOT NULL,
    CategoryID INT NOT NULL,
    ExpiryDate DATETIME NOT NULL,
    AttachmentID INT NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES FoodItemCategories(Id),
    FOREIGN KEY (AttachmentID) REFERENCES Attachments(Id)
);

CREATE TABLE Donations (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Status VARCHAR(255) NOT NULL,
    CreatedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UpdatedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    MeetUpLocation VARCHAR(255) NOT NULL,
    UserId VARCHAR(255) NOT NULL,
    Username VARCHAR(255) NOT NULL,
    FoodItemID INT,
    FOREIGN KEY (FoodItemID) REFERENCES FoodItems(Id)
);

CREATE TABLE NotificationSubscribers (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Category VARCHAR(255) NOT NULL
);

-- Optionally, you can insert some initial data into the FoodItemCategories table
INSERT INTO FoodItemCategories (Name) VALUES
('Milks & Dairies'),
('Fresh Fruits'),
('Vegetables'),
('Wine & Drinks'),
('Baking Material'),
('Pet Foods'),
('Noodles & Rice'),
('Snacks'),
('Others');

-- Run this to create tables
-- mysql -u cadadmin -p foodsharehub -h foodsharehub.c1wc4i62kq5k.us-east-1.rds.amazonaws.com < create_tables.sql
-- Password: cadpassword

-- To Check RDS Tables Design
-- mysql -h foodsharehub.c1wc4i62kq5k.us-east-1.rds.amazonaws.com -u cadadmin -p foodsharehub
-- DESCRIBE Attachments;
-- DESCRIBE Donations;
-- DESCRIBE FoodItemCategories;
-- DESCRIBE FoodItems;
