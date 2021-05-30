# django-rest-framework

it is deployed on https://cruddrf.herokuapp.com/
1.For registrations 
POST request:
https://cruddrf.herokuapp.com/api/v1/register

eg. 
{
"username":"sanket",
"password":1234
}

2. To get jwt token it will expire in 5 minutes
POST Request:
https://cruddrf.herokuapp.com/api/token/

3. to get registered students
a. GET to view all the students
https://cruddrf.herokuapp.com/api/v1/students

b. POST : in body need to pass parameters
eg:
{
"name": "sanket",
"age":24,
"father_name": "mk jain"
}
c. PUT
use same way
