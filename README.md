# SmartMart – AI Powered E-Commerce Platform

## Overview

SmartMart is a modern AI-powered e-commerce platform developed using React, Vite, Django REST Framework, and MySQL. The application provides a seamless online shopping experience across multiple categories, including Grocery, Fashion, Furniture, and Hardware.

The platform integrates Artificial Intelligence features such as room visualization for furniture placement and hardware product detection to enhance customer experience.

## Features

### User Features

* User Registration and Login
* Browse Products by Categories
* Product Search and Filtering
* Add to Cart
* Wishlist Management
* Order Placement
* Order History
* Responsive User Interface

### Admin Features

* Admin Dashboard
* Product Management (Add, Update, Delete)
* Category Management
* Inventory Management
* Order Management
* Customer Management

### AI Features

#### Furniture Room Visualization

* Upload room image
* Select room type
* Generate furniture placement preview
* Product recommendations

#### Hardware Detection

* Upload hardware image
* AI-based object detection
* Product identification
* Specification analysis

## Technology Stack

### Frontend

* React.js
* Vite
* Bootstrap
* CSS
* Axios

### Backend

* Python
* Django
* Django REST Framework

### Database

* MySQL

### AI/ML

* OpenCV
* YOLOv8

## Project Structure

Frontend:

* React
* Vite
* Bootstrap

Backend:

* Django REST Framework
* MySQL Database
* AI Modules

## Installation

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## Main Modules

### Grocery Module

Provides daily grocery products with stock and price management.

### Fashion Module

Displays fashion products and recommendations.

### Furniture Module

Allows users to visualize furniture placement in uploaded room images.

### Hardware Module

Detects hardware components and provides related product suggestions.

## Future Enhancements

* AI Chatbot Support
* Voice Search
* Online Payment Gateway
* Product Recommendation Engine
* Mobile Application

## Author

Developed as an academic and internship project using React, Vite, Django REST Framework, MySQL, and AI technologies.
