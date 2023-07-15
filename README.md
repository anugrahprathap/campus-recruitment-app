
# Campus Recruitment System

The Campus Recruitment System is a web application built using Python, Django, HTML, MySQL, JavaScript, and Bootstrap. It provides a platform for managing and handling campus recruitments at an educational institution. The system includes a Placement Officer who is responsible for organizing placement events and facilitating communication between companies and students. Companies can view student details and submit the details of selected students to the Placement Officer for further processing.

## Features

1. **Authentication**: The system allows users to create accounts and log in securely. Different roles are available, including Placement Officer and Company Representative.

2. **Placement Officer Dashboard**: The Placement Officer has access to a dashboard where they can manage placement events, student data, and communication with companies.

3. **Placement Events**: The Placement Officer can create and manage placement events, providing details such as date, time, location, and participating companies.

4. **Student Profiles**: Students can create and update their profiles, including personal information, academic details, and skills.

5. **Company Profiles**: Companies can view student profiles and search for suitable candidates based on criteria such as academic qualifications and skills.

6. **Selection Process**: Companies can shortlist students and send their details to the Placement Officer. The Placement Officer can review the selected students and take further action, such as arranging interviews or notifying students.

## Technologies Used

- **Python**: The core programming language used for the back-end development.
- **Django**: A powerful web framework for building web applications using Python.
- **HTML**: The standard markup language for creating web pages.
- **MySQL**: A popular relational database management system for storing and retrieving data.
- **JavaScript**: A programming language used for adding interactivity and dynamic behavior to web pages.
- **Bootstrap**: A front-end framework that provides pre-designed templates and components for building responsive and mobile-first web pages.

## Installation

To run the Campus Recruitment System locally on your machine, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/campus-recruitment-system.git
```

2. Change to the project directory:

```bash
cd campus-recruitment-system
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

4. Set up the database by configuring the MySQL settings in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Apply the database migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Open your web browser and access the application at `http://localhost:8000`.

## Usage

1. Access the application through a web browser.

2. If you are a new user, sign up for an account and choose the appropriate role (Placement Officer or Company Representative).

3. If you are a Placement Officer, log in and navigate to the dashboard.

4. As a Placement Officer, you can manage placement events, student profiles, and communication with companies.

5. If you are a Company Representative, log in and search for suitable candidates based on your requirements.

6. Company Representatives can shortlist students and submit their details to the Placement Officer for further processing.

## Contributing

Contributions to the Campus Recruitment System are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
```

3. Make the necessary changes and commit them:

```bash
git commit -m "Add your commit message here"
```

4. Push your changes to your fork:

```bash
git push origin feature/your-feature-name
```

5. Open a pull request on the main repository.

Please ensure that your code follows the project's coding conventions and includes appropriate tests.

## License

The Campus Recruitment System is open-source software licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code.
