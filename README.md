# Blog
Simple blog, realized on Django. Html template is not mine, it is by [**plasticneko**](http://github.com/plasticneko "**plasticneko**")
## Installation 
For **Linux or MacOS** users you can use special prepared script. By using this script, to install use just 2 commands.
`sh setup.sh`
`pip install -r requirements.txt`

**Windows** users, should use 1 command more
`python manage.py makemigrations`
`python manage.py migrate`
`pip instal -r requirements.txt`

## Running sever

For all platforms use
`python manage.py runserver`
Server is availible on http://localhost:8000

## Adding admin account
To create admin account, please run this command
`python manage.py createsuperuser` and follow instructions.

## Add articles and categories
To add article, go to http://localhost:8000/admin url. Login with superuser credentials. You can add articles and categories from admin panel
