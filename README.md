# FastAPI Cuisine & Coupon Service

## Overview
A lightweight, high-performance REST API microservice built with **FastAPI** and Python. This service provides endpoints to retrieve cuisine-specific restaurant menus and validate discount coupon codes using rigorous `Enum` data validation. 

This project demonstrates core backend engineering principles, including RESTful routing, type hinting, automatic interactive documentation, and robust data validation.

## Features
* **Cuisine Menu Routing:** Fetch categorized food items by cuisine type.
* **Dynamic Coupon Validation:** Process and retrieve discount percentages based on valid coupon IDs.
* **Enum Validation:** Strict request parameter validation ensuring only supported cuisines are queried.
* **Interactive Documentation:** Auto-generated Swagger UI and ReDoc for seamless API testing and client integration.

## Tech Stack
* **Language:** Python 3.x
* **Framework:** FastAPI
* **Server:** Uvicorn

## API Endpoints

### 1. Get Menu Items
Retrieves a list of menu items for a specified cuisine.
* **URL:** `/get_items/{cuisine}`
* **Method:** `GET`
* **Parameters:** `cuisine` (Available options: `italian`, `mexican`, `indian`)
* **Response Example:**
```json
[
  "Pizza",
  "Pasta",
  "Gelato"
]
```

### 2. Get Coupon Discount
Retrieves the discount percentage for a provided coupon ID.
* **URL:** `/get_coupon/{coupon_id}`
* **Method:** `GET`
* **Parameters:** `coupon_id` (Integer)
* **Response Example:**
```json
{
  "discount_amount": "20%"
}
```

## Local Setup & Installation

Follow these steps to run the service locally from your terminal:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Devanshibhargava/fastapi-cuisine-coupon-service.git](https://github.com/Devanshibhargava/fastapi-cuisine-coupon-service.git)
   cd fastapi-cuisine-coupon-service
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **View Interactive API Docs:**
   Once the server is running, open your browser and navigate to the built-in Swagger UI at: `http://127.0.0.1:8000/docs`

## Author
**Devanshi Bhargava**