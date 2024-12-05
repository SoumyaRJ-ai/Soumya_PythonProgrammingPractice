### 1. What's flask?
Flask is a micro web framework for developing APIs to serve web applications. The main components behind Flask's service id WSGI(Web Server Gateway Interface) toolkit and Jinja2 templates which helps in creating web pages 

### 2. What is WSGI toolkit?
WSGI stands for Web Server Gateway Interface which provides interface between webservers and python frameworks like Flask allowing Python to communicate with the web server. 

### 3. What is Jinja 2 template engine?
Jinja 2 template helps developers to create dynamic HTML uisng the Python framwwork like Flask and Django. Some of the key features of Jinja templates are - 
    - **Template Syntax:** Control structures are represented as *% for %* and *% if %*
    - **Variable Substitution:** Insert variable into templates using *{{ variable }}*
    - **Filters:** Modify the display of variables by using in-built filters. E.g. *{{ variable|capitalize }}*
    - **Template inheritance:** Create base templates and inherit them from the existing ones. 

### 4. Difference between Flask and Django?
| Flask | Django |
|----------|----------|
| Flask is WSGI Framework   | Django is a full-stack web framework   |
| Uses SQL Alchemy as it's ORM  | Built-in own ORM   |
| Admin panel is not available  | Built-in Admin panel |
| Best for small, light weight APIs | Well suited with Large scale feature rich APIs |
| Arbitrary code development structure | Follows conventional project structure |

### 5. Default host and port of Flask?
Local host at 127.0.0.1 and the default port at 5000

### 6. Which databases are Flask compatible?
Flask is compatible with MySQL and SQLite. Flask also comes with SQLDbAdapter which allows you to connect the variety of databases using Flask-SQLAlchemy, including MySQL, Oracle, PostgreSQL, Sybase etc.. Flask also had MongoDbAdapter that allows you to connect to MongoDB databases using Flask-MongoEngine.

### 7. Why we use Flask(__name__)?
When we create a new Flask application, we initialize it using this line of code. Flask is the main class here which we use to create the instance and __ __name__ __ is the variable that is passed inside the class is a special variable which holds the name of current module (the file being executed)
    
        app = Flask(__name__)

### 8. Routing in Flask?
App Routing menas mapping the URLs to a specific function that will handle the logic for that URL. 

### 9. Template Inheritance in Flask.
A lot of times we need our footer, header, navigation bar to stay the same for all our web pages. So we use this template inheritance mechanism to create this base template with all those details and we keep on inheriting that page in our other web pages so that they will be visible in all the web pages for our app. 

        {% extends "base.html" %}
    
### 10. What is url_for() is used?
url_for() is used for generating URLs dynamically for specific views or endpoints in your application. It is particularly useful because it allows you to avoid hardcoding URLs, making your code more reliable and robust. 

        url_for(endpoint/view_name, **args)
        - endpoint: The name of the function that defines the view. It is same as the name used in the @app.route() decorator 
        - values: Any parameters or arguments required by route

    e.g. : 

        from flask import Flask, render_template, redirect, url_for

        app = Flask(__name__)

        @app.route('/')
        def home():
            return "Welcome to the Home Page!"

        @app.route('/redirect-home')
        def redirect_home():
            return redirect(url_for('home'))  # Redirect to the 'home' endpoint

        if __name__ == "__main__":
            app.run(debug=True)

_Leaving this here as need to focus on Python programming. You can check the below link when you comeback later_
https://www.geeksforgeeks.org/flask-interview-questions-and-answers/