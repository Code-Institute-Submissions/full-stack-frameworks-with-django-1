# Full Stack Frameworks with Django [![Build Status](https://travis-ci.org/STEPLADD3R/full-stack-frameworks-with-django.svg?branch=master)](https://travis-ci.org/STEPLADD3R/full-stack-frameworks-with-django)

## By Stuart Green 

### Project Overview

I was tasked with creating one of three things, I decided to go with the issue tracker as I believe it is something that I can use in my work currently as right now, we don't really have a solid solution on managing bugs/user requests just now. The goal of this project was to use all of the skills and technologies I've learned on the Code Institute course thus far and build a fully functional issue tracker from the ground up whilst utilising technologies such as Django and Stripe.

### User Stories

* As an anonymous user (a user who does not have an account) I can:
  * View tickets as a whole (mix of bugs/features) by visiting `/tickets/` or by clicking on the sidebar menu item titled `All Tickets`.
  * Filter tickets by clicking on the sidebar menu item titled `Filter Tickets` and filling out the form selecting the options you wish to filter by.
  * View tickets through a bug only filter (i.e. only show bugs) by clicking on the sidebar menu item titled `All Bugs` from here, you can also click `All Tickets` to view all tickets, same as above.
  * View tickets through a feature only filter (i.e. only show features) by clicking on the sidebar menu item titled `All  Features` from here you can also click `All Tickets` to view all tickets, same as above.
  * View bugs based on a specific priority. There are two ways to do this:
    * Using the homepage will pull back the two latest bugs of each category.
    * Using the links in the footer will allow you to filter all bugs that are in progress by priority in the order of most upvotes being first.
  * View more detail about a specific ticket by clicking anywhere on the individual ticket.
  * Register for an account by clicking on the sidebar menu item titled `Register` under the User Profile tab.
  * Read through the Terms & Conditions, Refund Policy and Privacy Policy of the web app.
* As a user who is logged in to the web app I can:
  * Do all the same things as the anonymous user can.
  * View a list of bugs which that specific user has submitted to the app by clicking the `Submitted Bugs` menu item in the sidebar.
    * If `Submitted Bugs` is empty, meaning they haven't yet added anything to the app, then it will offer them a quick link to add a bug.
  * View a list of features which that specific user has submitted to the app by clicking the `Submitted Features` menu item in the sidebar.
    * If `Submitted Features` is empty, meaning they haven't yet added anything to the app, then it will offer them a quick link to add a feature.
  * View a list of bugs which that specific user has saved by clicking the `Saved Bugs` menu item in the sidebar.
    * If `Saved Bugs` is empty, meaning they haven't saved any bugs yet, then it will offer them a quick link back to the view all bugs page.
  * View a list of features which that specific user has submitted by clicking the `Saved Features` menu item in the sidebar.
    * If `Saved Features` is empty, meaning they haven't saved any features yet, then it will offer them a quick link back to the view all features page.
  * Submit a new bug to the app by clicking the `Add New Bug` menu item in the sidebar.
    * You will be presented with a form.
    * Fill out at the very least the mandatory fields.
    * Click `Submit`.
  * Submit a new feature to the app by clicking the `Add New Feature` menu item in the sidebar.
    * You will be presented with a form.
    * Fill out the mandatory fields (this forms fields are all mandatory).
    * Click `Submit`.
  * Comment on a ticket.
    * Go to a ticket detail page by clicking on a bug or feature.
    * Click `Leave a Comment` and you will be taken to a page with a comment box.
    * Fill out the comment box and click `Submit`.
  * Save a ticket.
    * Go to a ticket detail page by clicking on a bug or feature.
    * In the sidebar where all the ticket info is, at the bottom is a save button, click this to add to `Saved Bugs` if on a bug page, or `Saved Features` if on a feature page.
    * **ONLY IF THE TICKET HAS NOT YET BEEN SAVED.**
  * Unsave a ticket.
    * Go to a ticket detail page by clicking on a bug or feature.
    * In the sidebar where all the ticket info is, at the bottom is a unsave button, click this to add to `Saved Bugs` if on a bug page, or `Saved Features` if on a feature page.
    * **ONLY IF THE TICKET HAS ALREADY BEEN SAVED.**
  * Upvote a **bug**.
    * Click on a bug that you wish to upvote to take you through to the ticket detail page of that bug.
    * In the sidebar where all the ticket info is, at the bottom is a upvote button, click on this to upvote the bug you are currently viewing.
    * Each user gets only one vote. Once you have voted, you will get an toast notification saying that you have already cast your vote.
  * Upvote a **feature**.
    * Click on a feature that you wish to upvote to take you through to the ticket detail page of that feature.
    * In the sidebar where all the ticket info is, at the bottom is a upvote button, click on this to upvote the feature you are currently viewing.
    * This will add the feature upvote to your basket.
    * Adjust the upvote count as necessary, on features you can add as many as you wish (changing the quantity of upvotes will automatically update the price).
    * Click on Checkout when you're satisfied.
    * Fill out your credit card details and click `Submit`.
    * Once a feature has been upvoted at least once, it will change from `Funding Required` to `In Progress`.
  * Edit a ticket.
    * Click on the ticket that you wish to edit to take you through to the ticket detail page.
    * If you own the ticket, you will see a pencil icon, clicking on this icon will take you to a form where you can update values as necessary.
    * If you do not own the ticket, but try to visit the URL you will be redirected back to the ticket page, and an error will state you don't have the required privileges.
  * Delete a ticket.
    * Click on the ticket that you wish to delete to take you through to the ticket detail page.
    * If you own the ticket, you will see a trash can icon, clicking on this icon will submit a POST request to delete the item.
    * If you do not own the ticket, but try to visit the URL you will be redirected back to the ticket page, and an error will state you don't have the required privileges.
  * Update User Details.
    * In the User Profile tab in the sidebar menu, you will have the option to either change email address, or change password.
    * Both will keep you logged in after updating either values.
* As a superuser / staff member I can:
  * Do all the same things as the regular logged in user can.
  * As well as:
    * Edit any users tickets from the front-end the same way as the specific user can.
    * Delete any users tickets from the front-end the same way as the specific user can.
    * View and manage tickets and orders from the Django admin panel.

### UX

I started by thinking about the user flow and how I want the user to use the application. I came to the conclusion that it would be good to use the homepage of the app to contain useful information so I went with the most recent bugs that have been added to the site in priority order i.e. Critical, High, Medium and Low.

I also planned what would require the user to be logged in, and subsequently made sure to make note of anything that would so that I could make sure that only things an anonymous user can do is displayed to them.

I then planned out the menus for my application choosing to separate bugs/feature in the menu for ease of use and single responsibility principle, rather than allowing the user to add a ticket and choose between bug/feature themselves.

Once I had finished planning out the user flow and such, I moved on to creating the mockups of my application using Balsamiq which can be found in '[project-supplements/user-experience](https://github.com/STEPLADD3R/full-stack-frameworks-with-django/tree/master/project-supplements/user-experience)'.

Looking at the homepage mockup you can see that I have tried to make the most important/urgent things sit up at the top (i.e. Critical/High priority bugs). I have also provided an easy to use navigation to the app that allows the user to quickly and easily navigate around the app. I also did a mobile version of the mockup, whereby the menu is not always visible and must be toggled via a menu button, this allows the user to fully utilise the amount of screen real estate they have on their mobile devices.

I then mocked up how a couple of pages would look, these would be the same layouts used for both bugs and features (so I only designed them once) and would include Add Bug/Feature, All Submitted Bugs/Features (Shows all the bugs or features that user has created), and All Saved Bugs/Features (Shows all the bugs or features a user has saved).

For these pages, I wanted them to be small and concise, I didn't want the user to do a lot of scrolling so I limited them to show only 4 per page, and then added pagination so the user can easily go back and forth. I designed a mobile version though for this specific layout it remains nearly identical, with the exception of the menu mentioned above, and the footer spanning full width.

I then moved on to the Add/Edit pages which again would look very much the same for both bugs and features with perhaps a few fields changing here and there, so I combined these into one mockup. This is quite simply just a form page, and I tried to just simplify it, making sure everything was clearly labelled and quite big/blocky as well as making sure to add the universally recognised * symbol for required fields.

Finally, I designed the ticket detail pages which would be what the user sees when they click through for more information regarding a bug/feature. For this page, I wanted again to keep things simple, but make sure the useful information was always in eye sight. I decided the best way to do this would to be split it up into 3 columns, sidebar, content and another kind of sidebar with bug/feature info such as priority, upvotes, etc. This way, all the useful and main information would always be visible to the user.

I also did a mobile mockup of this layout where I debated whether or not to move the sidebar up to the top on mobile, in the end I decided against it as I think the user would prefer to know exactly what the issue/feature is first, but this could be good to A/B test in the future.

Images of the UX design process is available inside the '[project-supplements/user-experience](https://github.com/STEPLADD3R/full-stack-frameworks-with-django/tree/master/project-supplements/user-experience)' directory. This directory contains an array of documents that illustrate the UX design process in the form of wireframes.

### Database

After I finished creating the UI/UX design of the application, I moved on to the database design as I think it's just as important, if not more so to make sure hat the database architecture is on point, to ensure a scalable app in the future as well as ensuring the queries return results quickly.

I thought about the database tables and fields I would need and set about jotting them down using WordPad. This can be found in '[project-supplements/database-design](https://github.com/STEPLADD3R/full-stack-frameworks-with-django/tree/master/project-supplements/database-design)'. When doing this process, I just thought about it in terms of models I would need to create as Django has an ORM that converts the models into SQL and creates the database tables and fields.

**Database Schema in Balsamiq**
![alt text](https://github.com/STEPLADD3R/full-stack-frameworks-with-django/blob/master/project-supplements/database-design/database-schema.png "Database Schema")

**Example Django Model**

```python
class Ticket(models.Model):
    """
        Creating the Ticket Model that creates
        the ticket table in the MySQL Database.
    """
    TAGS = (
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature'),
    )
    PRIORITIES = (
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    STATUSES = (
        ('FR', 'Funding Required'),
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    )
    tag = models.CharField(max_length=7, choices=TAGS, default='BUG')
    title = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.CharField(
                                max_length=8,
                                choices=PRIORITIES,
                                default='LOW',
                                blank=True,
                                null=True)
    screenshot = models.ImageField(
                                    upload_to='ticket_screenshots',
                                    blank=True,
                                    null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUSES, default='IP')
    upvotes = models.IntegerField(default=0)
    upvote_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=19.99)
    earned = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} by {1}'.format(self.title, self.author)
```

### Existing Features

**Accounts**

* I used mostly the prebuilt Django user authentication for user accounts, I just modified some of the forms slightly from their defaults.
* User can register, login, logout, view their profile and, update their email or password.
* Thanks to Django's built in `from django.contrib.auth import update_session_auth_hash` updating the password also keeps the user logged in.

**Tickets**

* Tickets are free to create and voting will push it higher up the chain as tickets are ordered based on most upvotes.
  * Upvotes for bugs are completely free, but users may only upvote once.
  * Upvotes for features are paid for and users may buy as many as they like.
* Tickets can be viewed in three different ways:
  * View tickets as a whole (i.e. bugs and features)
  * View only bug tickets
  * View only feature tickets
* Tickets can also be filtered through, users have the option to use a filter form to search by either the title of the ticket or the name of the author (using Django's built in `from django.db.models import Q`), as well as by Tag (Bug or Feature), Priority or Status (i.e. in progress, or completed).
  * The form will then submit the parameters via a GET request and the values then filter the queryset.
  * The filter returns the count of tickets returned, if 0 it will ask you to search again.
* You can view all the tickets that you have submitted, separated into bugs/features so that you can keep an eye on their status. You get a visual indication of how many you have saved from the sidebar menu at all times.
* You can save/unsave tickets, and once saved they will appear in your `Saved Bugs` or `Saved Features`. You get a visual indication of how many you have saved from the sidebar menu at all times.

When I was creating the tickets, I tried to make use of Django Forms as much as possible, as well as ensuring that my CRUD operations were done using the Django Forms with the POST method, especially important on the delete operation and especially if the site were to be indexable by Google.

Ensuring that my operations could only be usable via the POST method means that you can't go to `tickets/1/save/` to save a ticket, you would have to submit the form by clicking the save button.

* Ticket Detail pages
  * If you are either a) the owner of the ticket or b) a member of staff you will have options to either edit or delete the ticket. This would allow the user to mark as complete, or simply amend a typo, or remove if the ticket is no longer valid.

**Comments**

* Users may post comments on tickets, these will be displayed under the ticket details.
* If you are either a) the owner of the comment or b) a member of staff you will have options to either edit or delete the comment.
* If no comment is shown, it will display that there are no comments.

**Basket**

* You can upvote features by adding the upvotes to your basket and buying them.
* When you click the upvote button on a feature ticket, it will take you to the basket.
  * Inside the basket you can straight up remove an item from the basket, from the remove column.
  * Add more upvotes inside the upvote column, the form will automatically update the value upon receiving a new value.
  * As well as these operations, you will notice the basket displays an itemised list, and again you can add/remove upvotes from here.
  * You'll also see a breakdown of the number of items, upvotes and total cost at  the bottom before heading off to the checkout page.

**Checkout / Stripe**

* Providing you have a basket that isn't empty, you'll be able to get to the checkout page.
* Once here, you'll see the basket one last time as well as the grand total of the order.
* Then, using Stripe API v2 the form performs validation and lookup to ensure details are correct before taking payment.
  * Upon successful payment you'll be notified via a Toast and the upvotes will be added, as well as adding an 'earned' price to the matching feature to.
  * Upon failing the form, you'll also be notified and have a chance to try again.

### Features for the Future

* I think it would be really helpful to send admins of the app an email once a feature has either a) been submitted or b) had it's first upvote (i.e. first payment) so that the admins don't have to check the app every day to realise any new paid feature requests have been submitted/upvoted.
  * I could do this by using Djangos built in django.core.mail module in conjunction with a email service such as SendGrid.
* Going forward, I think it would be good to use user friendly slugs instead of the id as using the id isn't a perfect solution for the user, and is far from perfect for making good use of SEO practices.
* It may be worth in the future updating the Stripe API to version 3 to make use of their prebuilt payment forms.

### Technologies

Here's a list of the main technologies used:

**General Development Tools**

* [Sublime Text 3](https://www.sublimetext.com/3)
  * I used Sublime Text to develop the project.
  * I also made good use of some very helpful packages such as Emmet for marking up content quickly and efficiently, and Sublime Text Anaconda which is a very useful user friendly Python linter.
* [Git](https://git-scm.com/)
  * I used Git to handle all my version control for this project.
* [NPM](https://www.npmjs.com/)
  * I used NPM to pull packages into my project, such as Bootstrap for easy SCSS control.
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)
  * I used virtualenv as my virtual environment whilst developing my project to ensure proper separation of packages.
* [Browserstack](https://www.browserstack.com/)
  * I used Browserstack to build a portfolio of screenshots testing multiple devices from mobile through desktop. See testing for more info.

**Front-end**

* HTML5 / [Bootstrap 4](https://getbootstrap.com/)
  * I used HTML5 to mark up the DOM and keep my code semantic.
  * I also used the Bootstrap 4 framework as a boilerplate and customised as needed.
* [SCSS](https://sass-lang.com/documentation/syntax)
  * I used SCSS using the [Django SASS](https://github.com/coderedcorp/django-sass) package as it was a simple way to add SCSS to Django.
* [jQuery](https://jquery.com/)
  * I used jQuery to make the app more interactive by utilising jQuery to create Toast notifications, popup modals, etc.

**Back-end**

* [Python](https://www.python.org/)
  * I used Python as the back-end language paired with the Django framework.
* [Django](https://www.djangoproject.com/)
  * I used the Django framework following the MVC (Model View Controller) architectural pattern.
* [MySQL](https://www.mysql.com/)
  * I set up MySQL on my local machine and MySQL is also used on the production version on Heroku as well.
    * I did this as I developed the project on my local Linux machine and wanted to ensure I could correctly set up a proper development environment. Next time I'd probably use sqlite as my development database.

**API**

* [Stripe](https://stripe.com/)
  * I used Stripe as the payment processor.

### Testing

**Automated Testing**

I have tested my tickets quite extensively, as evidenced [here](#!) I have tested the following:

* test_urls.py
  * I tested all of my ticket URLs to ensure that all the URLs resolve correctly, using Django SimpleTestCase.

* test_views.py
  * I first created a setup function that creates a user, logs the user in and creates two test tickets, a bug and a feature.
  * I then tested my functions being sure to test both the GET and POST request variants where necessary, as well as testing 404s where necessary as well.
  * For GET requests, I tested that the correct status code was returned, as well as the correct template was being used.
  * For POST requests, I tested that objects can indeed be created, updated and deleted as well as testing that the correct status code was returned.
  * For some POST requests I also checked to make sure that the value was there, and then again after it had been deleted to ensure it was indeed there, before being deleted.
  * For 404s I checked to make sure that the 404 status code was returned.

* test_models.py
  * I tested my models by first creating a test ticket, and then ensuring that the defaults were indeed being passed in.
  * I then tested that it was possible to override the defaults.
  * And finally I tested to make sure the required fields were not blank.

* test_forms.py
  * I also tested my forms to make test what would happen if a form is valid and what would happen if it was invalid.


I chose to only test the tickets, I think this was adequete according to the Pareto principle (known as the 80/20 rule). Most of the core functionality of the web app is within the tickets app, and I made sure to test everything thoroughly myself where necessary.

**Manual Testing**

Manual testing was also undertaken alongside the automated testing to ensure that the application looked good no matter what device the user was viewing the application on, as well as to check that all links across the site are in good working order.

Below are some of the manual tests undertaken:

* Tested the navigation hyperlinks e.g. Header, Footer and Sidebar menus to ensure they were all working.
* Tested all of the views to ensure that the appropriate meta data is being pulled through.
* Tested front-end CRUD functionality by creating, reading, editing and deleting tickets (both bugs and features).
* Tested validation on the forms is working as intended.
* Tested GET/POST requests to ensure appropriate error/success message shows.
* Tested the responsiveness of the application using a tool called Browserstack. Using this tool, I tested my website on multiple browsers, devices and operating systems such as:
  * iPhone (5 through to X)
  * iPad
  * iPad Pro
  * Huawei P20
  * Samsung Galaxy S10
  * Samsung Galaxy Tab
  * Google Chrome, Safari, Firefox, Microsoft Edge and IE11

**User Testing**

I asked multiple friends of mine to test the project for me after I had done my checks to ensure that I could test the application as thoroughly as possible, I received positive feedback, and as such would be happy to push it out to the general population. 

### Deployment

**Deploying to Heroku**

Requirements:

* A Heroku account (Free or Paid)
* ClearDB MySQL (Free or Paid)
* ALLOWED_HOSTS - Must contain the Heroku URL
* Procfile - Tells Heroku what kind of app it is `web: gunicorn issue_tracker.wsgi`
* requirements.txt file - Containing all of the required dependencies `guinicorn must be in requirements.txt for Heroku`

To deploy my project, I decided to go with [Heroku](https://www.heroku.com/). It was relatively straight forward and only took a matter of minutes before I had the project pushed from my local machine to a live production ready server. Although, if the project got more than a few users I would have to pay for ClearDB using Heroku as the free tier is very limited.

I have broken my deployment process up into several simple steps:

**$ notes a terminal command**

* Login to access the Heroku Dashboard
* On the dashboard, create a new app, choosing a name and region.
* Set up my Django project for hosting with Heroku:
  * Added my Heroku app URL to ALLOWED_HOSTS in settings.py
  * Created a Procfile `web: gunicorn issue_tracker.wsgi`
  * Installed guinicorn `$ pip install guinicorn` 
  * Updated dependencies `$ pip freeze --local > requirements.txt`
* Click on the newly created app to bring up more information- select `Resources`.
* I then added ClearDB MySQL as a resource and made note of the SQL database details it provided:
  * Database Name
  * Username
  * Password
  * Host
* I then added in all of my Config Vars by going to `Settings` in the Heroku top navigation bar.
  * SECRET_KEY - random Django secret key
  * DB_NAME - Provided by ClearDB MySQL
  * DB_USER - Provided by ClearDB MySQL
  * DB_PASSWORD - Provided by ClearDB MySQL
  * DB_HOST - Provided by ClearDB MySQL
  * DB_PORT - Usual 3306
  * AWS_ACCESS_KEY_ID - Provided by AWS
  * AWS_SECRET_ACCESS_KEY - Provided by AWS
  * STRIPE_PUBLISHABLE - Provided by Stripe
  * STRIPE_SECRET - Provided by Stripe
* I also added `DISABLE_COLLECTSTATIC` with a value of `1` to my config vars as I collected my static files manually later.
* I then moved on to the `Deploy` tab in the Heroku top navigation bar.
* I opted to install the Heroku CLI as I'd need to run commands later such as migrate, collectstatic etc.
* I then ran the following commands in my terminal ensuring I was in the correct directory (my project directory):
  * `$ heroku login`
  * `$ git add .`
  * `$ git commit -m 'added Heroku Procfile and requirements`
  * `$ git push heroku master`
  * `$ heroku run python manage.py makemigrations`
  * `$ heroku run python manage.py migrate`
  * `$ heroku run python manage.py collectstatic`
  * `$ heroku run python manage.py createsuperuser`
* I then restarted all dynos to restart the app.
* The application was then live, and I began to populate it.

**Deploying on a local machine for testing**

Requirements:

* Terminal
* Python 3.6+
* PIP
* MySQL (Unless you change the Database Default to sqlite in settings.py)

I would highly recommend installing some kind of virtual environment to ensure that each project has it's own dependencies. I recommend [virtualenv](https://virtualenv.pypa.io/en/stable/).

Please also note that these commands may differ from OS to OS, as I use an Ubuntu based operating system the commands I put below will refer to most Linux distributions.

**$ notes a terminal command**

* Firstly, with MySQL installed on your local machine, open up a terminal and enter:
  * `$ mysql -u <USERNAME> -p`
  * Type in your password, it will display as blank.
  * `$ create database <DATABASE_NAME>;`
  * `$ exit;`
* Now, create a directory somewhere on your hard drive.
* Open up a terminal in the designated directory by either right clicking and pressing `Open in Terminal` or using your keyboard shortcut to open terminal (in my case, `Super + T`).
* Now, if you have gone ahead and installed virtualenv you can enter into the terminal:
  * `$ virtualenv -p python3 .`
  * Note: there are other methods of doing this, so please see the documentation for more info.
  * Once the virtual environment has completed setup:
  * `$ source bin/activate` to activate the virtual environment.
  * I suggest making a directory now called `src` or similar, to host the project files, and then change directory into there.
  * Now, clone the project.
  * `$ git clone git@github.com:STEPLADD3R/full-stack-frameworks-with-django.git .` if using SSH.
  * `git clone https://github.com/STEPLADD3R/full-stack-frameworks-with-django.git .` if using HTTPS.
  * This will unpack the files into the src file.
* Now run the following command:
  * `$ pip install -r requirements.txt` to install all the project requirements.
* Once everything is installed, open up the project inside your code editor of choice.
* Head over to `issue_tracker/settings.py` in here be sure to do two things:
  * Change `DEBUG = False` to `DEBUG = True` to ensure static/media files are served correctly.
  * Either change the database none environment vars to match your own database or move to the next step.
* Adding in environment variables:
  * Open up your file manager, go to your root directory `~/` and show hidden files, however you do it on your OS. For me, there is a hamburger menu with the option to show hidden files.
  * From there, open up .bashrc in your editor of choice.
  * Here is a list of all the environment variables
    * SECRET_KEY - Optional, as you can enter a local string after the os.environ.get if you prefer.
    * DB_NAME - Optional, as you can enter a local string after the os.environ.get if you prefer.
    * DB_USER - Optional, as you can enter a local string after the os.environ.get if you prefer.
    * DB_PASSWORD - Optional, as you can enter a local string after the os.environ.get if you prefer.
    * DB_HOST - Optional, as you can enter a local string after the os.environ.get if you prefer.
    * DB_PORT - Optional, as you can enter a local string after the os.environ.get if you prefer.
    * AWS_ACCESS_KEY_ID - As long as you set `DEBUG = True` you should not need this.
    * AWS_SECRET_ACCESS_KEY - As long as you set `DEBUG = True` you should not need this.
    * STRIPE_PUBLISHABLE - Get it from your Stripe account.
    * STRIPE_SECRET - Get it from  your Stripe account.
* Now everything is set up, go back to the terminal window with the virtualenv running.
* Then run the following:
  * `$ python manage.py makemigrations`
  * `$ python manage.py migrate`
  * `$ python manage.py createsuperuser`
  * `$python manage.py runserver`
* And then you're ready to go!

### Demo

A demo of the application can be found here: [Demo](https://ua-issue-tracker-fsf-ci.herokuapp.com/)

### Credits

__Stuart Green__ - This project was created and built as a part of the Code Institute Full Stack Development course.

[Django Documentation](https://docs.djangoproject.com/en/2.2/) - The Django Documentation was really helpful during this project.

[Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Improved Bootstrap Forms in Django.

[Django Testing](https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM) - I found this extremely helpful when learning how to do testing in Django. Alongside the Django Documentation on Testing.

#### Content & Media

Most of the content on the app is lorem ipsum, for example the T&Cs and policies are lorem ipsum but with real headings just to show that on an app of this calibre (ecommerce) these would be required for the go live.

Media is mostly just placeholder content e.g. bug screenshots and as such have come from [placeholder.com](https://placeholder.com/).

### Notes

I would just like to state that the reason as to why in my tickets.views I have `mandatory_tags` and `mandatory_priorities` is because there are links to these in both the sidebar and footer menus, and if there was no tickets with a priority, yet it was still linked up, it would 404, and this is not good. I chose instead to display a message to the user, so for example instead of 404ing, if you went to `/tickets/bugs/` or `/tickets/features` when they're empty (i.e. none submitted) it would display a nice message stating such, and the same if you went to `/tickets/bugs/priority/critical` and there were no critical bugs, it would 404 when instead, not taking the user away from the app and stating that there are no critical bugs at this time, is a much better UX in my opinion.