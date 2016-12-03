# Scrapology : Social Media Data Scrapping 

![alt text](http://i.imgur.com/IkRpfaG.png "Social Media Data Scrapping")

A REST API build with Django 1.9.11 + Django REST Framework (Python 3.5.2). This API provide a set of JSON web services 
to scrap then store/fetch data from main social networks. 

## Twitter [In Progress]

1. *__User Profile__* [Done]
    * Scrap Profile public data whenever they're available using just the Twitter Username : Full name, Profile Picture URL, Bio, Location, Joining Date, 
Personal URL, Number of Tweets, Number of Followers, Number of Following', Number of Likes) <br><br>
URL: http://localhost:8000/twusers/Username [Method POST]<br><br>
    * Save User in the SQLite database<br><br>
    * Retrieve User by Username <br><br>
URL: http://localhost:8000/twusers/Username [Method GET]<br><br>
    * List all scrapped twitter users <br><br>
URL: http://localhost:8000/twusers/ [Method GET]<br><br>

2. *__User Tweets__* [In Progress]

## Instagram [ToDo]

