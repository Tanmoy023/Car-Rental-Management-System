# 🚗 Car Rental Management System

A full-stack **Car Rental Management System** built using **Django** that allows users to browse available cars, check availability for specific dates, make bookings, and manage reservations through a simple and responsive web interface.

---

## 📌 Project Overview
This web application simulates a real-world **car rental platform** where customers can register, explore a fleet of vehicles, book cars, and manage their reservations.  
The system includes booking workflows, mock payment processing, and a user dashboard to track booking history.

---

## ✨ Features

### 🔐 User Authentication
- User registration
- Login and logout functionality
- Secure authentication using Django

### 🚘 Car Inventory
- Browse available cars
- View detailed vehicle information
- Display images and pricing

### 📅 Booking System
- Check car availability by date
- Real-time rental price calculation
- Booking status workflow (Pending → Confirmed)
- Cancel pending bookings

### 💳 Payments & Receipts
- Mock credit card payment processing
- Printable booking receipts

### 👤 User Dashboard
- View booking history
- Track reservation status
- Manage bookings

### 📱 Responsive Design
- Built with **Bootstrap 5**
- Works across mobile, tablet, and desktop devices

---

## 🛠️ Tech Stack

**Backend**
- Python
- Django

**Frontend**
- HTML
- CSS
- JavaScript
- Bootstrap 5

**Database**
- SQLite (default)
- PostgreSQL (optional configuration)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/car-rental-management-system.git
cd car-rental-management-system
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run migrations
```bash
python manage.py migrate
```

### 6️⃣ Start the development server
```bash
python manage.py runserver
```

Open your browser and go to:

```
http://127.0.0.1:8000
```

---

## 📂 Project Structure

```
car-rental-management-system
│
├── rentals/
├── templates/
├── static/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 📷 Screenshots
*(Add screenshots of your project here)*

Example:
```
![Home Page](screenshots/home.png)
![Booking Page](screenshots/booking.png)
```

---

## 🚀 Future Improvements

- Online payment gateway integration
- Admin analytics dashboard
- Email booking confirmation
- REST API support
- Car filtering and search functionality

---

## 👨‍💻 Author

**Tanmoy Patra**

📧 tanmoypatra369@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/tanmoy-patra-00b756236  
🐙 GitHub: https://github.com/Tanmoy023

---

⭐ If you like this project, consider giving it a **star** on GitHub!
