-- Active: 1735506937735@@127.0.0.1@3306
CREATE DATABASE IF NOT EXISTS `family-finances`;
USE `family-finances`;

CREATE TABLE IF NOT EXISTS `Frequency` (
    `FrequencyId` INT AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Budget` (
    `BudgetId` INT AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL,
    `Reference` VARCHAR(255),
    `FrequencyId` INT,
    `CreatedAt` TIMESTAMP DEFAULT NULL,
    `UpdatedAt` TIMESTAMP DEFAULT NULL,
    `DeletedAt` TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (`FrequencyId`) REFERENCES `Frequency`(`FrequencyId`)
);
CREATE TABLE IF NOT EXISTS `Transaction` (
    `TransactionId` INT AUTO_INCREMENT PRIMARY KEY,
    `Date` DATE NOT NULL,
    `Reference` VARCHAR(255),
    `Amount` DECIMAL(10, 2) NOT NULL
);