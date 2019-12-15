# Full Stack Frameworks with Django [![Build Status](https://travis-ci.org/STEPLADD3R/full-stack-frameworks-with-django.svg?branch=master)](https://travis-ci.org/STEPLADD3R/full-stack-frameworks-with-django)
## By Stuart Green 

### Project Overview
I was tasked with creating one of three things, I decided to go with the issue tracker as I believe it is something that I can use in my work currently as right now, we don't really have a solid solution on managing bugs/user requests just now. The goal of this project was to use all of the skills and technologies I've learned on the Code Institute course thus far and build a fully functional issue tracker from the ground up whilst utilising technologies such as Django and Stripe.

### User Stories
* A user wants to be able to notify the developer of the Unicorn Attractor app that they have found an issue on the app so that it can be fixed, or suggest a feature that would make the app better for themselves, and other users.

* A user would like to be able to do more than simply view bugs/features. They must first create an account. To do this, they can use the sidebar menu to register to the Issue Tracker app.

* A user would like to log in to the website, they can do this by using the sidebar menu to login, using the account they have just created. If they click the login link before registering, they will be given a chance to register first by following the link in the golden bar.

* A user has found a bug on the app, they want to notify the creator of the app. To do so, they must be logged in and then they will gain access to the 'Add new bug' link in the sidebar menu. They must fill out all fields marked with * and validation is carried out on the front-end and back-end.

* A user would like to edit a bug. To do so, they must be logged in and as long as the bug belongs to them they will have the option to edit the bug by clicking the edit icon (pencil) next to the title on the individual bug page i.e. /bugs/1.
    * The form will be prepopulated with the current values, and again validation is carried out on the front and back-end.

* A user would like to delete a bug. To do so, they must be logged in and as long as the bug belongs to them they will have the option to delete the bug by clicking the delete icon (trashcan) next to the title on the individual bug page i.e. /bugs/1.

* A user would like to upvote a bug. To do so, they must be logged in, on the bug detail page in the right side sidebar there is a link titled 'Upvote', clicking on this will allow the user to vote, but you can only vote once, clicking it again will result in an error message saying you have already voted.

* A user would like to save a bug for later. To do so, they must be logged in, on the bug detail page in the right side sidebar there is a link titled 'Save'. This will then become available in the 'Saved Bugs' tab on the sidebar.

* A user would like to remove a saved bug. To do so, they must be logged in and have already saved the bug before. On the bug detail page in the right side sidebar there is a link titled 'Unsave'. This will then remove the bug from the users 'Saved Bugs'.

* A user would like to leave a comment on a bug/feature. To do so, they must be logged in, on the bug/feature detail page the user should click on the 'Leave a Comment' button and fill out the form.
    * The form will be prepopulated with the current values, and again validation is carried out on the front and back-end.

* A user would like to edit a comment. To do so, they must be logged in and as long as the bug/feature belongs to them they will have the option to edit the comment by clicking the edit icon (pencil) next to the title on the individual bug/feature page.
    * The form will be prepopulated with the current values, and again validation is carried out on the front and back-end.

* A user would like to delete a comment. To do so, they must be logged in and as long as the bug/feature belongs to them they will have the option to delete the comment by clicking the delete icon (trashcan) next to the title on the individual bug/feature page.

* Features to come soon.

### UX
Details of the UX design process is available inside the 'project-supplements/user-experience' directory. This directory contains an array of documents that illustrate the UX design process in the form of wireframes.

### Database
Details of the Database design process is available inside the 'project-supplements/database-design' directory. This directory contains an array of documnents that illustrate how I came to decide on the database collections and fields.

### Features
#### Existing Features

#### Features for the Future

### Technologies
Here's a list of technologies used:

1. HTML5 - Used for marking up the DOM.
2. SCSS (CSS Pre Processor) - Used to create the styling.
3. jQuery - Used to provide some neat functionalities such as accordions, toast notifications and more.
4. NPM - Used to pull in packages, such as Bootstrap so that I could control the SCSS more easily.
5. Git - Used to handle version control
6. Python & Django - Python Framework to handle config, routes and more.
7. MySQL - Database of choice

### Testing
Details of the project testing process is available inside the 'project-supplements/testing' directory.

### Deployment

### Demo
A demo of the application can be found here: [Demo](#!)

### Credits
__Stuart Green__ - This project was created and built as a part of the Code Institute Full Stack Development course.

[Django Documentation](https://docs.djangoproject.com/en/2.2/) - The Django Documentation was really helpful during this project.

[Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Improved Bootstrap Forms in Django.

#### Content & Media