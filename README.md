# Skincare E-Commerce Platform

A full-stack skincare e-commerce web application built with **Python, Flask, SQLite, HTML, CSS, and JavaScript**, complemented by a modern **UI/UX homepage design created in Figma**.

## Overview

Skincare Heaven is a full-stack web application designed to provide an interactive skincare shopping experience.

The platform allows users to explore skincare products, discover products suited to different skin types, manage accounts, and interact with shopping features such as carts and wishlists.

Administrators can manage products and users through a dedicated administrative dashboard.

In addition to the functional Flask application, the project includes a Figma homepage design concept focused on improving visual consistency, navigation, product discovery, and overall user experience.

---

## Features

### User Features

- User registration and login
- Secure authentication
- Password reset via email
- User profile management
- Product browsing and product details
- Shopping cart functionality
- Wishlist management
- Product search functionality
- Product categories
- New arrivals and best-selling products
- Special offers and skincare bundles
- Interactive skin type quiz
- Skincare educational content
- Morning and evening skincare routine guides

### Admin Features

- Admin authentication
- Product management
- Add, edit, and delete products
- User management
- Role-based access control
- Database administration

---

## UI/UX Design — Figma

A desktop homepage concept was created using **Figma** to explore a cleaner and more modern interface for Skincare Heaven.

### Design Objectives

- Create a visually appealing skincare shopping experience
- Establish consistent typography and colors
- Improve navigation clarity
- Highlight important calls to action
- Make product discovery more intuitive
- Maintain a clean and organized page layout

### Homepage Design Elements

- Minimal navigation bar with essential links
- Hero section with a prominent headline
- Skincare-inspired product photography
- Consistent neutral and green color palette
- Clear "Explore Products" call-to-action button
- Structured spacing and visual hierarchy

### Design Specifications

| Element | Specification |
|---|---|
| Design Tool | Figma |
| Desktop Frame | 1440 × 900 px |
| Primary Color | #607764 |
| Heading Color | #26352B |
| Background | Warm off-white |
| Typography | Inter |
| Button Style | Rounded corners |
| Design Approach | Clean, minimal, skincare-inspired |

### Figma Homepage Preview

![Skincare Heaven Figma Homepage](design/skincare-homepage.png)

The Figma design is a UI/UX concept and is not presented as a fully implemented replacement for the existing Flask frontend.

---

## Technologies Used

### Backend

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Flask-Mail
- Flask-WTF
- Flask-Migrate

### Database

- SQLite

### Frontend

- HTML
- CSS
- JavaScript

### UI/UX Design

- Figma
- Wireframing
- Visual hierarchy
- Typography and color selection
- Interface layout design
- User-centered design principles

### Development Tools

- Git
- GitHub
- Visual Studio Code

---

## Security Features

- Password hashing
- User authentication
- Session management
- Secure password reset tokens
- Role-based authorization

---

## Project Architecture

```text
app/
├── models/
├── routes/
├── templates/
├── static/
├── forms/
├── email/
└── database/

design/
└── skincare-homepage.png

run.py
config.py
requirements.txt
README.md
```

The `design/` directory stores the Figma homepage preview separately from the Flask application source code.

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sarahassaad140/flask-skincare-webapp.git
cd flask-skincare-webapp
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Application

Configure the required application settings, including the database connection, secret key, and email credentials, using the project's configuration file or supported environment variables.

Do not commit passwords, secret keys, or email credentials to GitHub.

### 5. Run the Application

```bash
python run.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

Additional database initialization or migration steps may be required depending on the local configuration.

---

## Skills Demonstrated

### Software Development

- Full-Stack Web Development
- Flask Application Development
- Database Design and Management
- Authentication Systems
- Role-Based Access Control
- Email Integration
- SQL Database Management
- Frontend Development

### UI/UX Design

- Figma Interface Design
- Homepage Layout Design
- Visual Hierarchy
- Color Palette Selection
- Typography
- Navigation Design
- Call-to-Action Design
- Wireframing and Visual Prototyping

### Project Management

- Git Version Control
- GitHub Repository Management
- Technical Documentation
- Application Architecture

---

## Future Improvements

- AI-powered skincare recommendations
- Product review and rating system
- Online payment integration
- Machine learning recommendation engine
- Personalized product suggestions based on skin quiz results
- Responsive implementation of the Figma homepage concept
- Mobile UI/UX design
- Accessibility improvements
- Usability testing
- Improved product filtering and search

---

## Author

**Sarah Assaad**

Master's Student in Data Science & Artificial Intelligence

**GitHub:** [sarahassaad140](https://github.com/sarahassaad140)

---

*Skincare Heaven combines full-stack web development with an evolving focus on user interface design and personalized skincare experiences.*
