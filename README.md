# Overview

This is a web application that I made to start tracking goals. It allows you to register a user or login to the site. Once you are logged in you can create goals and track your progress. You can also see a list of all the goals that have been created. Everyone can look at the list of goals but only logged in users can create them. As part of each goal, you can add a title, details, and an optional image for motivation. From the list view you can click on a goal to see more details about it and the picture if there is one. 

My purpose for writing this software was to learn how to create a web application using Django and Python. My main goal was to learn how to manage users and enforce authentication for some pages. I also decided to use pillow to add and manage images for additional learning. 

# Software Demo

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

The pages I created are as follows:
* Home Page - This is the main page of the site. It has a welcome message and a link to the list of goals.
* Register Page - This page allows a user to register for the site. It has a form that takes a username, email, and password.
* Login Page - This page allows a user to login to the site. It has a form that takes a username and password.
* List of Goals Page - This page shows a list that dynamically shows all the goals that have been created. It has a link to the details of each goal.
* Goal Details Page - This page shows the details of a goal. It has a title, details, and an optional image. It also has a link back to the list of goals.
* Create Goal Page - This page allows a user to create a new goal. It has a form that takes a title, details, and an optional image.
* About Page - This page has a brief description of the site and the author. But it is currently hidden from navigation and not used.
* There is also a layout.html file that houses the global navigation bar and header for each page. This is used to keep the site looking consistent, make it easier to navigate the app, and to make it easier to add new pages in the future. It also has show/hide logic based on whether the user is logged in or not.

# Development Environment

I used Visual Studio Code as my IDE and the following tools and libraries:
* Python 3.9.6
* Django 3.2.6
* Pillow 8.3.1

# Useful Websites

* [Starter Tutorial](https://www.youtube.com/watch?v=Rp5vd34d-z4)
* [Django Documentation](https://docs.djangoproject.com/en/3.2/)
* [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
* [python Documentation](https://www.python.org/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [tutorialspoint](https://www.tutorialspoint.com/django/index.htm)
* [w3schools](https://www.w3schools.com/python/default.asp)
* [realpython](https://realpython.com/get-started-with-django-1/)

# Future Work

* I would like to create a form that allows me to add five to ten goals, an end date, and an accountability partner. From there I would create a checklist for each day by the end date that would allow me to check off the tasks that I have completed each day. If any box is missing any day before midnight, it would email the accountability partner.
* Show a view of every complete day and the tasks that were completed.
add an option to add an amount of money that would be incrementally lost (given to accountability partner) each day that a task is not completed.
*Update the about page to be more informative and add a contact form.
*Add a page that shows the user profile and allows them to update their information.
*Add a page that shows the accountability partner profile and allows the user to update their information.

# Helpful Commands

django-admin startproject djangoproject1 . # Create a new project
.venv\Scripts\activate # Activate the virtual environment
cd djangoproject1 # Change to the project directory
py manage.py startapp [app name] # Create a new app
python manage.py runserver # Run the server
python manage.py makemigrations # Create migrations
python manage.py migrate # Apply migrations
py manage.py createsuperuser # Create a superuser