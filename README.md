# Flask School System

This project is a basic school management system developed with Flask, enabling the management of students, teachers, disciplines, and courses. It demonstrates best practices in using Flask with SQLAlchemy, Flask-WTF forms, and an organized project structure.

---

## Technologies Used

- Python 3.10+
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- SQLite (as the default database)

---

## Features

- Registration of students, teachers, disciplines, and courses.
- Relationships between entities, including:
  - Many-to-many between teachers and disciplines.
  - Direct associations with courses.
- Simple interface for registering and viewing the data.

---

## Installation and Setup

### 1. Clone the Repository

```bash
$ git clone https://github.com/LuUuFe/Flask-School-System.git
$ cd Flask-School-System
```

### 2. Create a Virtual Environment

It is highly recommended to create a virtual environment to avoid dependency conflicts.

```bash
# On Linux or macOS
$ python3 -m venv venv
$ source venv/bin/activate

# On Windows
$ python -m venv venv
$ venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the dependencies listed in the `requirements.txt` file.

```bash
$ pip install -r requirements.txt
```

### 4. Run the Application

Start the local server:

```bash
$ flask run
```

The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## Project Structure

```
Flask-School-System/
|
|-- app/
|   |-- __init__.py       # Flask application configuration
|   |-- models.py         # Database models definition
|   |-- forms.py          # Flask-WTF forms
|   |-- routes.py         # Application routes
|   |-- templates/        # HTML files
|   |-- static/           # Static files (CSS, JS, images)
|   |-- config.py             # Application configuration
|
|-- requirements.txt      # Project dependencies
|-- run.py                # Application entry point
```

---

## Contribution

If you want to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit your changes with a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE).

