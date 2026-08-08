# Flask Automation

This project simulates an automated web registration system built with Python. It uses technologies such as Flask, PyAutoGUI, webbrowser, mysql.connector, time, and csv. The Flask server handles the registration process; while the automation script performs the web interactions. Finally, the registration data is stored in a MySQL database.

## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![MySQL Workbench](https://img.shields.io/badge/MySQL%20Workbench-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)

### Python Libraries

* `Flask` — Web application framework
* `PyAutoGUI` — Browser and GUI automation
* `mysql.connector` — MySQL database connection
* `webbrowser` — Opens web pages automatically
* `time` — Execution timing and delays
* `csv` — CSV file handling

### Database

* **MySQL** — Database management system
* **MySQL Workbench** — Database design, administration, and SQL development

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install flask pyautogui mysql-connector-python
```

### 4. Configure the MySQL database

Create the database and the required tables in **MySQL Workbench**.

Then, configure the database connection in the Python application:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
```

### 5. Run the application

Start the Flask application with:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

### 6. Run the automation script
```bash
python automation.py
```

> **Note:** Make sure that the MySQL server is running before starting the application.

