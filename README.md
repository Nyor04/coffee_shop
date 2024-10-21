Coffee Shop
===========

Training repo, poking around django and django-rest-framework

Requirements
------------


*   **Python 3.11+**

Installation Guide
------------------

Follow these steps to get the project up and running on your local machine.

### 1\. Clone the Repository

Clone the project repository from GitHub to your local machine.

```bash
git clone [https://github.com/Nyor04/coffee_shop.git]
cd coffee_shop
```

### 2\. Set Up Virtual Environment

Create and activate a virtual environment.


```bash
python3 -m venv venv 
source venv/bin/activate 
```

### 3\. Install Dependencies

Install the required Python packages using `pip`.

`pip install -r requirements.txt`

### 4\. Configure Environment Variables

Create a `.env` file in the root of the project.

  1) Update the `.env` file with your database credentials(only if you're goin to use anything besides sqlite3
     here a quick reference of dbs you can use: https://docs.djangoproject.com/en/5.1/ref/settings/#databases )
     
  3) other necessary configurations like secrets keys and stuff.

### 5\. Set Up the Database (optional step, this goes just if you're using anything than sqlite3)
assuming youre going to use postgreSQL:

Create the PostgreSQL database and apply migrations.

```bash
psql -U postgres CREATE DATABASE coffeeshop;
```
Apply migrations 

```bash
python manage.py migrate
```

### 6\. Create a Superuser

Create a superuser to access the Django admin interface.


```
python manage.py createsuperuser
```

### 7\. Run the Development Server

Start the Django development server.

```
./manage.py runserver
```

Access the project by navigating to `http://127.0.0.1:8000` in your web browser.

Project Structure
-----------------

*   **products**: Handles everything related to coffee products.
*   **users**: Manages user authentication and profiles.
*   **orders**: Manages customer orders.

Kudos to #teamPlatzi who help me build this project
