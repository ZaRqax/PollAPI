# PollAPI app

Simple API app for Polls service

# How to run

* Clone or download app from github

`git clone https://github.com/ZaRqax/pollsAPI.git`

* Create new virtual environment

`python -m venv <your venv name>`

* Activate your venv

`source <your venv name>/bin/activate `

* Install dependents 
 
`pip install requirement.txt`

* Create new django project 

`django-admin startproject <your project name>`

* Configure settings.py 
```python
    INSTALLED_APPS = [
    ...
    'rest_framework',
    'polls',
]
```
* Configure url.py
```python
urlpatterns = [
    ...
    path('',include("polls.urls")),
]
```
* Make migrations 

`python manage.py makemigrations `

`python manage.py migrate`

* Create Superuser

`python manage.py createsuperuser`

* Run serever 
```bash
python manage.py runserver 
```



# Api entry points

## Get list of questions

### Request

`GET api/questions/`

### Response 
```bash
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "url": "http://127.0.0.1:8000/api/questions/1/",
        "text": "Question1",
        "type": "S",
        "poll": "http://127.0.0.1:8000/api/polls/1/"
    },
  
]
```
## Get a specific question

### Request

`GET api/questions/<pk>`

### Response 
```bash
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "url": "http://127.0.0.1:8000/api/questions/1/",
    "text": "Question1",
    "type": "S",
    "poll": "http://127.0.0.1:8000/api/polls/1/"
}
```
## Create a new question

### Request

`POST api/questions/`

### Response 
```bash
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Location: http://127.0.0.1:8000/api/questions/3/
Vary: Accept

{
    "id": 2,
    "url": "http://127.0.0.1:8000/api/questions/2/",
    "text": "Question2",
    "type": "M",
    "poll": "http://127.0.0.1:8000/api/polls/1/"
}
```
## Delete question

### Request

`DELETE api/question/<pk>`

### Response 
```bash
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
## Update question

### Request

``PUT /api/questions/<pk>/``

### Response 
```bash
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Location: http://127.0.0.1:8000/api/questions/3/
Vary: Accept

{
    "id": 2,
    "url": "http://127.0.0.1:8000/api/questions/2/",
    "text": "Question2",
    "type": "M",
    "poll": "http://127.0.0.1:8000/api/polls/1/"
}
```
## Get list of polls

### Request

`GET api/polls/`

### Response 
```bash
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "url": "http://127.0.0.1:8000/api/polls/1/",
        "id": 1,
        "name": "Poll1",
        "start_date": "2021-07-27",
        "end_date": "2021-07-30",
        "description": "loremipsum"
    },
    
]
```
## Delete poll

### Request

`DELETE api/polls/<pk>`

### Response 
```bash
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
## Get a specific poll

### Request

`GET api/polls/<pk>`

### Response 
```bash
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

 {
        "url": "http://127.0.0.1:8000/api/polls/1/",
        "id": 1,
        "name": "Poll1",
        "start_date": "2021-07-27",
        "end_date": "2021-07-30",
        "description": "loremipsum"
    }
```
## Create a new polls

### Request

`POST api/polls/`

### Response 
```bash
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Location: http://127.0.0.1:8000/api/polls/3/
Vary: Accept

{
    "url": "http://127.0.0.1:8000/api/polls/3/",
    "id": 3,
    "name": "Poll3",
    "start_date": "2021-07-27",
    "end_date": "2021-07-31",
    "description": "polls"
}
```
## Update polls

### Request

``PUT /api/polls/<pk>``

### Response 
```bash
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "url": "http://127.0.0.1:8000/api/polls/1/",
    "id": 1,
    "name": "Poll3",
    "start_date": "2021-07-27",
    "end_date": "2021-07-31",
    "description": "q"
}
```
You cant change start_date field
## Get list of answer for current user
##### if user non authinticated automatical created new user with unicle id

### Request

`GET api/answers/`

### Response 
```bash
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "url": "http://127.0.0.1:8000/api/answers/2/",
        "id": 2,
        "answer": "Answer1",
        "user": 1,
        "question": 1
    },
   
]
```
## Delete answer

### Request

`DELETE api/answers/<pk>`

### Response 
```bash
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
## Get a specific poll

### Request

`GET api/answers/<pk>`

### Response 
```bash
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "url": "http://127.0.0.1:8000/api/answers/2/",
    "id": 2,
    "answer": "Answer2",
    "user": 1,
    "question": 1
}
```
## Create a new answer

### Request

`POST api/answers/`

### Response 
```bash
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "url": "http://127.0.0.1:8000/api/answers/12/",
    "id": 12,
    "answer": "Answer12",
    "user": 1,
    "question": 2
}
```
## Update answer only admin

### Request

``PUT /api/answers/<pk>``

### Response 
```bash
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "url": "http://127.0.0.1:8000/api/answers/12/",
    "id": 12,
    "answer": "Answer13",
    "user": 1,
    "question": 2
}
```
## Get answers for current user

### Request

``PUT /api/my-answers``

### Response 
```bash
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "questions": [
        {
            "id": 1,
            "url": "http://127.0.0.1:8000/api/questions/1/",
            "text": "Question1",
            "type": "S",
            "poll": "http://127.0.0.1:8000/api/polls/1/"
        },
        {
            "id": 2,
            "url": "http://127.0.0.1:8000/api/questions/2/",
            "text": "Question2",
            "type": "M",
            "poll": "http://127.0.0.1:8000/api/polls/2/"
        },
        {
            "id": 3,
            "url": "http://127.0.0.1:8000/api/questions/3/",
            "text": "Question2",
            "type": "M",
            "poll": "http://127.0.0.1:8000/api/polls/1/"
        }
    ],
    "1": [
        "Question1",
        [
            {
                "url": "http://127.0.0.1:8000/api/answers/13/",
                "id": 13,
                "answer": "Answer1",
                "user": 2,
                "question": 1
            }
        ]
    ],
    "2": [
        "Question2",
        []
    ],
    "3": [
        "Question3",
        [
            {
                "url": "http://127.0.0.1:8000/api/answers/14/",
                "id": 14,
                "answer": "Answer12",
                "user": 2,
                "question": 3
            }
        ]
    ]
}
```

