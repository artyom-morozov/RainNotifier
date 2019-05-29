# Rain Notifier

Small script which sends an email  specified to specified recipiends when it is going to be raining at 6 or 6 on a given weekday.

I use this to decide whether or not to grab my umbrella when going to work.

## Setup
Add your own data to the following lines in the ```env.txt``` file 

* ```API_KEY``` comes from https://darksky.net/dev/register
* ```LAT``` and ```LON``` are the coordinates of where you would like to receive weather from
* ```RECIPIENTS``` put email addresses of people who want to recieve notifications separated by ```,```
* ```START_HOUR``` is the start hour of the time when the email should be sent
* ```START_MINUTE``` is the minute 

Simply run the script in the same directory as env.txt, it will send the notification when the time comes

## Deployment
I run this using Custom Clock Processes with APScheduler on Heroku. 

(more information here https://devcenter.heroku.com/articles/clock-processes-python)

You can add this to existing Heroku repository or create a new instance, using their CLI:

```
heroku create YOUR-NAME
heroku git:remote -a YOUR-NAME
git push heroku master
```

and run the clock process in the background.

```
heroku ps:scale clock=1
```

