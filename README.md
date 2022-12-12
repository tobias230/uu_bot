# uu_bot
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was initiated to find student accomodation in Utrecht, the Netherlands. Available rooms provided by student housing organizations are usually sold out within seconds on a first-come-first-served base. In this project I built a web-scraping bot to immediatly send a notification as soon as an acoomodation becomes free. 

Disclaimer: For Researching purposes only.

![image](https://user-images.githubusercontent.com/81744567/207182675-641f405c-e097-4fee-bec3-51118fd90346.png)

## Technologies
Project is created with
* Python version: 3.8.5

### Dependencies
* selenium: 4.3.0

## Setup
To run this project, install it locally or on cloud service such as aws ec2 instance.
1. in main.py ; substitute "username" and "password" of ssh login credentials
2. in alert.py ; substitute "email" and "password" with email credentials to send notification. if email host different from gmx, adjust accordingly [25]
