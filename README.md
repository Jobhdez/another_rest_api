# api
A simple django rest api

# how to interact with the api
         git clone https://github.com/Jobhdez/another_rest_api.git
         
         cd another_rest_api
         
         python3 manage.py runserver
         
         http://127.0.0.1:8000/api/
         
to return the first post:

         http://127.0.0.1:8000/api/1

# testing
to test the model:

         pip3 install coverage
         
         cd another_rest_api
         
         coverage run --omit='*venv/*' manage.py test

         
         
         
