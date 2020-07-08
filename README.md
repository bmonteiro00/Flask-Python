README

There are two endpoints:

    1 -) GET : /repository/user/<name> ; ex :  /repository/user/bruno-m-santos
    2 -) GET : /repository/user/<name>/<reponame>; ex : /repository/user/bruno-m-santos/lt

Instructions to run with docker :

    1) docker build --tag=flask_mongo:v0.0.1 .
    2) docker run -p 5000:5000 flask_mongo:v0.0.1
    
  OR 
  
    1) docker compose up
    
Running locally(You must have installed the MONGODB locally) :
    
    1) python run.py
    
    
To improve :
    
    1) Add new test cases.
 