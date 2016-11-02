#Utilizing Python 3
import requests
import datetime
import json

API_TOKEN = '9e46e028f978939349e3fcd8d8a8c283'
ENDPOINT1 = 'http://challenge.code2040.org/api/dating'
ENDPOINT2 = 'http://challenge.code2040.org/api/dating/validate'


r = requests.post(ENDPOINT1, data = {'token':API_TOKEN})
data = json.loads(r.text)
datestamp = data['datestamp']
num_of_seconds = data['interval']

date_stamp_array = datestamp.split('T') #excluding 'T' in the ISO format
date = date_stamp_array[0]
time = date_stamp_array[1]
time = time.split('Z')[0] #Excluding 'Z'
new_datestamp = date + ' ' + time

#formatting

format = '%Y-%m-%d %H:%M:%S' 
new_datetime_date = datetime.datetime.strptime(new_datestamp, format)


mod_datestamp = new_datetime_date + datetime.timedelta(seconds = num_of_seconds) #sum of new datetime
mod_datestamp = mod_datestamp.strftime(format)
mod_datestamp = mod_datestamp.split(' ')
final_mod_datestamp = mod_datestamp[0] + 'T' + mod_datestamp[1] + 'Z'


p = requests.post(ENDPOINT2, data = {'token':API_TOKEN, 'datestamp':final_mod_datestamp})
print(p.text)

