** PLEASE NOTE
I am using the "djoser" library so the authentication and registration endpoints are provided by the djoser library.

# Endpoints and APIs TO TEST:
/menu/
/menu-item/<int:pk>
/book/
/reservations/

# APIs
/api/bookings
/api/menu
/api/menu-item/<int:pk>

# USER REGISTRATION - Using Browsable API, Postman or Insomnia
/auth/users/ 

# USER AUTHENTICATION - Using Postman or Insomnia
/auth/registration/token/login/
/auth/registration/token/logout/


# UNIT TESTS
RUN $ python manage.py test

# Project is hosted on github link -> https://github.com/aliitani/littlelemon
# settings.py has the MySQL database connection set up