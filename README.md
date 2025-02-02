# Vehicle Sales and Service Management System - TVS Motors

## Overview
The **Vehicle Sales and Service Management System** is a software solution designed to streamline the operations of a vehicle dealership. It enhances sales tracking, inventory management, service scheduling, and customer relationship management (CRM). This system integrates a **Database Management System (DBMS)** to efficiently handle dealership operations, ensuring smooth workflow and improved customer experience.

## Features
### 1. Inventory Management
- Track vehicle availability, new arrivals, and sold units.
- Maintain records of different vehicle models and specifications.

### 2. Sales Process Automation
- Manage customer inquiries, vehicle demonstrations, and transactions.
- Generate invoices and maintain purchase records.

### 3. Service Scheduling
- Schedule service appointments and assign technicians.
- Maintain detailed service history for each vehicle.

### 4. Customer Relationship Management (CRM)
- Store and manage customer details, preferences, and purchase history.
- Send service reminders and promotional offers.

### 5. Data Security & Compliance
- Ensure regulatory compliance and secure sensitive information.
- Implement user authentication and role-based access control.

## Technologies Used
- **Database:** MySQL
- **Programming Language:** Python
- **User Interface:** Tkinter
- **SQL Features:** Transaction handling, concurrency control, normalization techniques

## System Architecture
- **ER Modeling:** Entity-Relationship diagrams to define system entities.
- **Relational Schema Design:** Database schema optimized for relational queries.
- **Normalization:** Ensuring data integrity and reducing redundancy.
- **SQL Queries:** Optimized queries for fast and reliable data retrieval.

## Installation Guide
### Prerequisites
Ensure you have the following installed:
- Python (3.x)
- MySQL Database Server
- MySQL Connector for Python
- Tkinter (included with Python)

### Steps to Install
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/Vehicle-Sales-and-Service-Management-System.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Vehicle-Sales-and-Service-Management-System
   ```
3. Install dependencies:
   ```sh
   pip install mysql-connector-python
   ```
4. Set up the MySQL database:
   - Open MySQL and execute the provided **database.sql** script to create tables.
5. Run the application:
   ```sh
   python main.py
   ```

## Usage
1. **Login** using dealership credentials.
2. **Manage inventory** by adding or updating vehicle records.
3. **Process sales transactions** and generate invoices.
4. **Schedule services** for customers and assign technicians.
5. **View customer details** and maintain a relationship database.

## Database Schema
The database follows a structured relational schema including tables for:
- Vehicles
- Customers
- Sales
- Service Records
- Technicians

## Contributors
- Developed as part of the **DBMS Course Project** at **SRM Institute of Science and Technology**.
- Specifically designed for **Shivalaya Motors - An Authorized TVS Dealer**.
