# Overview

This is a simple prototype of a Django web app called GeoRF. I wrote this as a way to become familiar with Django.

The app is a listing of various radio stations and frequencies that are displayed on a map.

To run this app, type `python3 manage.py runserver` if you are on a Mac and `python manage.py runserver` on windows. At this point, go to http://127.0.0.1:8000/freq/ if all the settings are left as default. The url will also be output on the terminal, minus the slug.

[Software Demo Video](https://youtu.be/E5nc4P0chsI)

## Web Pages

The app has to web pages or views. The page to list the radio frequencies is http://127.0.0.1:8000/freq/ . The page to view the details of the frequency and location on a map is http://127.0.0.1:8000/freq/num/ , where num is the id number of the frequency.

## Development Environment

This web app was developed using Visual Studio Code. It uses Django, and Python3

## Useful Websites

* [Official Django Website](https://www.djangoproject.com/)
* [W3 Schools - Django](https://www.w3schools.com/django/index.php)

## Future Work

There is a lot that can still be done with this prototype.

* User authentication
* The ability to add new stations
* Search capabilities
