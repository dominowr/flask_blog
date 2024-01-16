
# Blog Application

Application is a platform that allows users to register, add comments to posts, and enables content management by administrators. It operates with a division of users into two main roles: admin and regular user.


## Features

- User account creation
- Role division: admin, regular user
- User with admin role is able to add posts
- Users with regular user role are able to create a comments



## Tech Stack

- Flask (Python)
- SQLAlchemy with ORM
- HTML, CSS

## Running

### Instructions

1. Clone this repository: `git clone https://github.com/dominowr/flask_blog.git`
2. Navigate to the project directory: `cd Blog_app`
3. Copy the `.env.example` file to `.env` and adjust the configuration as needed
4. Install requirements.txt:
```
pip install -r requirements.txt
```
5. Create user with admin role:
```
python -m flask create-admin frodo frodo@baggins.net secretpassword
```
6. Run application:
```
python -m flask run
```
7. The application will be available at [http://localhost:5000/](http://localhost:5000/)



## Authors

- [@dominowr](https://www.github.com/dominowr)

