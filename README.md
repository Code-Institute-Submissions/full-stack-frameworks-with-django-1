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
I started by thinking about the user flow and how I want the user to use the application. I figured that it would be good to use the homepage of the app to contain useful information so I went with the most recent bugs/features that have been added to the site.

I also planned what would require the user to be logged in, and subsequently made sure to make note of anything that would so that I could make sure that only things an anonymous user can do is displayed to them.

I then planned out the menus for my application choosing to separate bugs/feature for ease of use and single responsibility principle.

Once I had finished planning out the user flow and such, I moved on to creating the mockups of my application using Balsamiq which can be found in '[project-supplements/user-experience](https://github.com/STEPLADD3R/full-stack-frameworks-with-django/tree/master/project-supplements/user-experience)'.

Looking at the homepage mockup you can see that I have tried to make the most important/urgent things sit up at the top (i.e. Critical/High priority issues). I have also provided an easy to use navigation to the app that allows the user to quickly and easily navigate around the app. I also did a mobile version of the mockup, whereby the menu is not always visible and must be toggled via a menu button, this allows the user to fully utilise the amount of screen real estate they have on their mobile devices.

I then mocked up how a couple of pages would look, these would be the same layouts used for both bugs and features (so I only designed them once) and would include Add Bug/Feature, All Submitted Bugs/Features (Shows all the bugs or features that user has created), and All Saved Bugs/Features (Shows all the bugs or features a user has saved).

For these pages, I wanted them to be small and concise, I didn't want the user to do a lot of scrolling so I limited them to show only 4 per page, and then added pagination so the user can easily go back and forth. I designed a mobile version though for this specific layout it remains nearly identical, with the exception of the menu mentioned above, and the footer spanning full width.

I then moved on to the Add/Edit pages which again would look very much the same for both bugs and features with perhaps a few fields changing here and there, so I combined these into one mockup. This is quite simply just a form page, and I tried to just simplify it, making sure everything was clearly labelled and quite big/blocky as well as making sure to add the universally recognised * symbol for required fields.

Finally, I designed the bug detail pages which would be what the user sees when they click through for more information regarding a bug/feature. For this page, I wanted again to keep things simple, but make sure the useful information was always in eye sight. I decided the best way to do this would to be split it up into 3 columns, sidebar, content and another kind of sidebar with bug/feature info such as priority, upvotes, etc. This way, all the useful and main information would always be visible to the user.

I also did a mobile mockup of this layout where I debated whether or not to move the sidebar up to the top on mobile, in the end I decided against it as I think the user would prefer to know exactly what the issue/feature is first, but this could be good to A/B test in the future.

Images of the UX design process is available inside the '[project-supplements/user-experience](https://github.com/STEPLADD3R/full-stack-frameworks-with-django/tree/master/project-supplements/user-experience)' directory. This directory contains an array of documents that illustrate the UX design process in the form of wireframes.

### Database
After I finished creating the UI/UX design of the application, I moved on to the database design as I think it's just as important, if not more so to make sure hat the database architecture is on point, to ensure a scalable app in the future as well as ensuring the queries return results quickly.

I thought about the database tables and fields I would need and set about jotting them down using WordPad. This can be found in '[project-supplements/database-design](https://github.com/STEPLADD3R/full-stack-frameworks-with-django/tree/master/project-supplements/database-design)'. When doing this process, I just thought about it in terms of models I would need to create as Django has an ORM that converts the models into SQL and creates the database tables and fields.

** Database Schema in Balsamiq **
![alt text](https://github.com/STEPLADD3R/full-stack-frameworks-with-django/blob/master/project-supplements/database-design/database-schema.png "Database Schema")

** Example Django Model **
```
class Bug(models.Model):
    """
        Creating the Bug Model that creates
        the bug table in the MySQL Database.
    """
    PRIORITIES = (
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    STATUSES = (
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    )
    tag = models.CharField(max_length=3, default='bug')
    title = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.CharField(
                                max_length=8,
                                choices=PRIORITIES,
                                default='LOW')
    screenshot = models.ImageField(
                                    upload_to='bug_screenshots',
                                    blank=True,
                                    null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUSES, default='IP')
    upvotes = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

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