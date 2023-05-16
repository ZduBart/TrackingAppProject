# Tracking App Project

This repository contains a tracking app project developed by ZduBart. The app is a tool for monitoring and managing fleet of construction vehicles.
It uses data logs provided by devices mounted in machines to present real time information about vehicle status and selected parameters.

## Table of Contents
- [Site](#site)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Site

### Landing Page for signed user

![](https://github.com/ZduBart/TrackingAppProject/assets/108027175/995aa102-99f4-4f0c-af4f-6e404e6064f2)

### Vehicle list
![](https://github.com/ZduBart/TrackingAppProject/assets/108027175/bf9bca40-df0a-49fc-91f4-790f15b16c80)

### Charts
![](https://github.com/ZduBart/TrackingAppProject/assets/108027175/49ed816b-10c9-4a03-8c3a-639c222ac97f)

## Features

- User authentication
- Essential CRUD operations for vehicles and devices
- Logs preview and history
- Vehicle analytics
- Simple GUI

## Requirements

The `requirements.txt` file lists all Python libraries used:

- Django==4.2
- djangorestframework==3.14.0
- pusher==3.3.2
- python-decouple==3.8
- django-crispy-forms==2.0
- crispy-bootstrap4==2022.1
- psycopg2-binary==2.9.6


## Installation

1. Clone the repository:
```
git clone https://github.com/ZduBart/TrackingAppProject.git
```
2. Change into the project directory:
```
cd TrackingAppProject
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
1. Run the application:
```
python manage.py runserver
```
2. Open a web browser and navigate to http://localhost:8000.
3. You should now be able to use the tracking application and access its features through the web interface.

## Contact
If you have any questions or suggestions, feel free to contact the project author at barol3211@gmail.com
