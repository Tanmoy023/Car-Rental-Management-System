# How to Set Up and Run the Car Rental System

This guide explains how to set up the Car Rental Management System on a new Windows laptop using Visual Studio Code (VS Code).

## Prerequisites

Before you begin, you need to install the following software:

1.  **Python**:
    *   Download from [python.org](https://www.python.org/downloads/).
    *   **IMPORTANT**: During installation, check the box **"Add Python to PATH"**.

2.  **Visual Studio Code (VS Code)**:
    *   Download and install from [code.visualstudio.com](https://code.visualstudio.com/).

## Step-by-Step Setup Guide

### 1. Extract the Project
1.  Unzip the `Car_rental_Management_system.zip` file to a location on your computer (e.g., `D:\Car_rental_Management_system` or your Desktop).

### 2. Open in VS Code
1.  Open **VS Code**.
2.  Go to **File** > **Open Folder...**.
3.  Select the extracted folder `Car_rental_Management_system`.

### 3. Setup Virtual Environment (Recommended)
Open the terminal in VS Code (**Terminal** > **New Terminal**) and run:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
```
*You should see `(venv)` appear at the beginning of your terminal line.*

### 4. Install Dependencies
In the same terminal, run:

```bash
pip install django psycopg2
# Or if a requirements.txt exists:
# pip install -r requirements.txt
```
*Note: This project uses Django. If you encounter errors with `psycopg2`, you can try `pip install psycopg2-binary`.*

### 5. Setup the Database
Initialize the database tables:

```bash
python manage.py migrate
```

### 6. Create Admin User (Optional)
To access the admin panel:

```bash
python manage.py createsuperuser
```
Follow the prompts to set a username and password.

### 7. Load Sample Data (Optional)
To populate the website with initial cars:

```bash
python setup_data.py
```

### 8. Run the Server
Start the application:

```bash
python manage.py runserver
```

You should see output saying:
`Starting development server at http://127.0.0.1:8000/`

### 9. Access the Application
1.  Open your web browser (Chrome, Edge, etc.).
2.  Go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**Congratulations! The software is now running.**

## Troubleshooting
*   **"Python was not found"**: Ensure you checked "Add Python to PATH" during installation. You may need to reinstall Python.
*   **"pip is not recognized"**: Restart VS Code after installing Python.
*   **Image Issues**: If images don't load, ensure the `media` folder exists and contains the car images.
