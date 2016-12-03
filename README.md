# Scrapology : Social Media Data Scrapping 

![alt text](http://i.imgur.com/IkRpfaG.png "Social Media Data Scrapping")

A REST API build with Django 1.9.11 + Django REST Framework (Python 3.5.2). This API provide a set of JSON web services 
to scrap then store/fetch data from main social networks. 

## Twitter [In Progress]

1. *__User Profile__* [Done]
    * Scrap Profile public data whenever they're available using just the Twitter Username : Full name, Profile Picture URL, Bio, Location, Joining Date, Personal URL, Number of Tweets, Number of Followers, Number of Following', Number of Likes) <br><br>
URL: http://localhost:8000/twusers/Username [Method POST]<br><br>
    * Save User in the SQLite database<br><br>
    * Retrieve User by Username <br><br>
URL: http://localhost:8000/twusers/Username [Method GET]<br><br>
    * List all scrapped twitter users <br><br>
URL: http://localhost:8000/twusers/ [Method GET]<br><br>

2. *__User Tweets__* [Done]
   * Download the latest 3420 tweets of a given Twitter user identified by his username (handle). Twitter only allows access to a users most recent 3240 tweets through its API. I used [Tweepy]: http://www.tweepy.org which is Python wrapper for Twitter API.<br><br>
   * Require that the user profile is scrapped and saved in the DB first, deletes the corresponding tweets in the DB if they exist, scrap the latest ones and save in the DB.<br><br>
URL: http://localhost:8000/twusers/Username/tweets [Method POST]<br><br>   
   * Retrieve the user tweets from the DB if they exist<br><br>
URL: http://localhost:8000/twusers/Username/tweets [Method GET]<br><br> 
   

## Instagram [ToDo]

