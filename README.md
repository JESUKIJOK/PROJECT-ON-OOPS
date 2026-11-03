# Python OOP Library Management System

A Python console application demonstrating core Object-Oriented Programming (OOP) principles through a library item tracking system.

## Features

- **Base Class Abstraction:** Encapsulates shared attributes like `title`, `item_id`, and availability status (`__is_available`).
- **Encapsulation & State Management:** Protects item availability status using private attributes and exposes methods for checking out and returning items.
- **Inheritance & Specialty Types:** 
  - `Book` subclass with author and page count details.
  - `DVD` subclass with run time duration details.
- **Polymorphism:** Method overriding (`get_info()`) allowing generic interaction across diverse library item types.

---

## OOP Concepts Demonstrated

| Concept | Implementation Details |
| :--- | :--- |
| **Encapsulation** | Private attribute `__is_available` restricts direct state modification, requiring callers to use `check_out()` and `return_item()`. |
| **Inheritance** | `Book` and `DVD` inherit properties and methods from the `LibraryItem` base class using `super().__init__()`. |
| **Polymorphism** | Both derived classes override `get_info()` to append type-specific properties while maintaining a common call interface. |

---

## Project Structure

```text
.
├── ASSESMENT.py    # Main implementation script containing OOP models and execution demo
└── README.md       # Project documentation
