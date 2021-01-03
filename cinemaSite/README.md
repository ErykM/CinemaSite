To initialize project

1. git clone repository
2. move to the projects root directory
3. create new virtualenv
4. pip install -r requirements.txt
5. python manage.py runserver

To initialize tests

1. Use virtualenv used to initialize project
2. use 'pytest' command to run  

NOTES
- djangorestframework installed outside of virtualenviroment causes issues while running the tests


AUTHORIZATION  
- To register new user use /users/register/ endpoint with form data fields(name, email, password)

- To login use /users/login/ endpoint with form data(email, password), endpoint returns access and refresh jwt token

- To refresh token use /users/login/refresh/ token with form data(refresh=(refresh token returned from login endpoint))

PROJECT USAGE
- To use protected endpoints you have to use login endpoint and then add {Authorization: Bearer {access_token}} header to every request

ENDPOINTS
- /admin/ email and password protected admin panel only for superusers
- /api/movies/ lists all movies in the database
- /api/movies/id displays details about chosen movie
- /api/tickets/ lists all tickets for logged in user