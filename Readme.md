# 🛒 Shopping Cart GUI Application

A modern and user-friendly Shopping Cart application built with **Python** and **Tkinter**. This project provides a graphical interface for managing shopping cart items, updating quantities, calculating totals, and simulating the checkout process.

## 📌 Overview

The Shopping Cart GUI Application allows users to add products, manage item quantities, remove items, and view the total cost in real time. The application features a clean and responsive interface designed using Python's Tkinter library, making it an excellent project for learning GUI development, object-oriented programming, and data management in Python.

## ✨ Features

### 🛍️ Cart Management

* Add new items with custom prices
* Automatically increase quantity when the same item is added again
* Remove individual items from the cart
* Clear the entire cart with confirmation

### 🔢 Quantity Controls

* Increase item quantity with a single click
* Decrease item quantity dynamically
* Automatic item removal when quantity reaches zero

### 💰 Real-Time Billing

* Automatic subtotal calculation for each item
* Real-time cart total updates
* Item count tracking and display

### ✅ Input Validation

* Prevents empty item names
* Validates numeric price input
* Restricts negative prices
* Displays user-friendly error messages

### 🛒 Checkout System

* Order summary before confirmation
* Displays purchased items, quantities, and subtotals
* Order placement confirmation dialog
* Cart reset after successful checkout

### 🎨 Modern User Interface

* Clean and responsive Tkinter design
* Scrollable cart view
* Interactive buttons with hover effects
* Professional color scheme and layout
* Dynamic item count badge

---

## 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python 3.x   | Core Programming Language |
| Tkinter      | GUI Development           |
| Dataclasses  | Data Modeling             |
| OOP Concepts | Application Structure     |

---

## 📂 Project Structure

```text
shopping_cart.py
│
├── CartItem Class
├── Cart Class
├── ShoppingCartApp Class
├── GUI Components
├── Cart Management Functions
└── Checkout System
```

---

## 🚀 Installation

### Prerequisites

* Python 3.8 or higher
* Tkinter (included with standard Python installation)

### Clone the Repository

```bash
git clone https://github.com/your-username/shopping-cart-gui.git
cd shopping-cart-gui
```

### Run the Application

```bash
python shopping_cart.py
```

---

## 📖 How to Use

### Adding Items

1. Enter an item name.
2. Enter the item price.
3. Click **Add +**.

### Managing Quantities

* Click **+** to increase quantity.
* Click **−** to decrease quantity.
* Quantity updates automatically.

### Removing Items

* Click the **✕** button beside any item.

### Checkout

1. Click **Checkout →**
2. Review the order summary.
3. Confirm the purchase.

---

## 🧪 Testing

### Test Item Addition

* Add multiple products with different prices.
* Verify they appear correctly in the cart.

### Test Quantity Updates

* Increase and decrease item quantities.
* Confirm subtotal calculations update correctly.

### Test Validation

* Leave fields empty.
* Enter invalid prices.
* Verify appropriate error messages appear.

### Test Checkout

* Add multiple items.
* Confirm order summary accuracy.
* Complete checkout and verify cart reset.

---

## 📚 Learning Outcomes

This project demonstrates:

* Object-Oriented Programming (OOP)
* Python Dataclasses
* GUI Development with Tkinter
* Event Handling
* Data Validation
* Dynamic User Interface Updates
* Real-Time Calculations

---

## 🔮 Future Enhancements

* Product categories
* Search functionality
* Inventory management
* Discount and coupon system
* Database integration
* User authentication
* Receipt generation (PDF)
* Dark mode support

---

## 👨‍💻 Author

**Lakshya Sharma**

B.Tech CSE Core Student
Python Developer | Software Engineering Enthusiast | Open Source Learner

---

⭐ If you found this project useful, consider giving it a star on GitHub!
