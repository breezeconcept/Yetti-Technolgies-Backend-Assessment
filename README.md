# Django Authentication and Testing Project

This Django project demonstrates user authentication features and comprehensive testing using Django's testing framework.

## Project Setup

Follow these steps to set up and run the project:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/breezeconcept/Yetti-Technolgies-Backend-Assessment.git
   cd Yetti-Technolgies-Backend-Assessment


2. Create a virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows, use "venv\Scripts\activate"

3. Install project dependencies:

    pip install -r requirements.txt

4. Apply database migrations:

    python manage.py migrate

5. Create a superuser for admin access (optional):

    python manage.py createsuperuser

6. Start the development server:
 
    python manage.py runserver

7. Access the project in your web browser at 
    http://localhost:8000/



## Running Tests

To run the tests for this project, use Django's test runner: 
    
    python manage.py test

This command will execute all the unit tests, ensuring the correctness of user registration, login, logout, access control, and error handling.


## Additional Notes

This project uses Django's built-in authentication system. User registration, login, and logout functionality are provided out of the box.

User registration form validation and error handling are included in the project, along with unit tests to verify their correctness.

Access control is enforced using Django's @login_required decorator, which restricts access to authenticated users only.

The project includes unit tests for various scenarios, such as valid and invalid login credentials, user registration, and access control.

For security, the project should be further reviewed and tested for potential vulnerabilities like session fixation and CSRF attacks in a real-world scenario.

Feel free to customize and extend this project to meet your specific requirements.