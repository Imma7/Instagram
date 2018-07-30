# INSTAGRAM

## Description
An Instagram clone web app

## User Requirements
1. Sign in to the application to start using it.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

# Features
* User authentication with email confirmation.
* Public user profiles
* Following and Follow feature features
* Photo feed displaying user photos along with those users follows.
* Commenting on images.
* search functionality for users.
* Django admin dashboard for adding & managing posts and user accounts.

## Getting started

### Requirements
This project was created on a linux platform but should work on other unix based[not limited to] sytems.
* Python3

### Cloning the repository
```bash
git clone https://github.com/Imma7/Instagram.git && cd Instagram
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
For this project you will need the following configurations plus email setup for email registration hmac verification.
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running the server 
```bash
python manage.py runserver
```

### Admin Dashboard
Use django admin to manage the different users and posts.

### Deploying to heroku
. Deploying to heroku

## Running the tests
```bash
python manage.py test
```
Still in the process of writing tests

## Live Demo

The web app can be accessed from the following link: 
[Instagram](https://instaclonewars.herokuapp.com/)

## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)

## Contributing

- Git clone [https://github.com/Imma7/Instagram.git](https://github.com/Imma7/Instagram.git) 
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license, (c) [Immanuel Mugambi](https://github.com/Imma7)