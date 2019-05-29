from datetime import datetime, time
import requests, smtplib


def readAfterEq(file_name):
    f = open(file_name, 'r')
    output_arr = []
    for x in f:
        x =  x.replace(' ','').replace('\n','')
        x = x[x.index('=')+1:]
        if ',' in x:
            x = x.split(',')
        output_arr.append(x)
    f.close()
    return output_arr



values = readAfterEq('env.txt')



API_KEY = values[0]
LAT = values[1]
LON = values[2]
RECIPIENTS = values[3]
current_minute = True

start = time(values[4],values[5])
finish = time(7, 31)


def sendEmail(recipient):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("sendertesting13@gmail.com", "1632PoPPsP")

    # message to be sent
    message = "Its gonna be raining today around the time you finish work. Grab an umbrella!"
    print('sending...')
    # sending the mail
    s.sendmail("sendertesting13@gmail.com", recipient, message)

    # terminating the session
    s.quit()
def sendMail():
    for r in RECIPIENTS:
        sendEmail(r)

def isRainingAt5(dates):
    for obj in dates:
        date = datetime.utcfromtimestamp(obj.get('time'))
        print(date,' p:',obj.get('precipProbability'))
        if date.day == datetime.now().day and (date.hour == 17 or date.hour == 18):
            probability = obj.get('precipProbability')
            if probability >= 0.5:
                return True
    return False

def getForecast():
    api = 'https://api.darksky.net/forecast/{}/{},{}'.format(API_KEY, LAT, LON)
    response = requests.get(api).json()
    hourly_forecast_array = response.get('hourly').get('data')
    print('Got forecast for today...')
    if isRainingAt5(hourly_forecast_array):
        sendMail()
    else:
        print('No rain today')


while True:
    current_time = datetime.now().time()
    if current_time.strftime('%H:%M') == start.strftime('%H:%M') and current_minute:
        print(current_time)
        getForecast()
        current_minute = False
    if current_time.strftime('%H:%M') == finish.strftime('%H:%M'):
        current_minute = True


