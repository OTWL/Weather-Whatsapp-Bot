import sys
import requests
import datetime
import pywhatkit

latitudeCord = 0.0000
longitudeCord = 0.0000


baseUrl = "https://api.open-meteo.com/v1/forecast"

def getResponse():

    #Dictonary
    apiParams = {
    "latitude": latitudeCord,
    "longitude": longitudeCord,
    # Requested hourly variables
    "hourly": "temperature_2m,precipitation_probability,cloud_cover,rain",
    #Max temp for that day
    "daily": "temperature_2m_max", 
    "timezone": "auto",
     "forecast_days": 2 #Amount of day's you want the weather forecast data to span
    }
   
    #Get weather data
    response = requests.get(baseUrl, params=apiParams)
    return response

def getCurrentTime(now):
    #Clean date to get minutes and hours
    cleanedDate = now.replace(second=0,microsecond=0)
    cleanedDate = cleanedDate.strftime("%Y-%m-%dT%H:%M")
    return cleanedDate


def incrementTime(now):
    timeToAdd = datetime.timedelta(hours=1)
    targetDate = now + timeToAdd
    #Clean string to add 1 hour
    cleanDate = targetDate.replace(minute=0,second=0,microsecond=0)
    cleanDate = cleanDate.strftime("%Y-%m-%dT%H:00")
    return cleanDate

#find index of time
def getIndex(time,jsonResponse):
    index = 0
    searchString = jsonResponse["hourly"]["time"]

    while index < len(searchString):
        if time == searchString[index]:
            return index
        else:index +=1

    return -1

def getValue(index,jsonResponse):
    baseString= jsonResponse['hourly']
    #Insert all weather data you want to pull
    weatherAspects = ["temperature_2m","precipitation_probability","cloud_cover","rain"]
    #Creates dictonary of each aspect's and their value
    for weather in weatherAspects:
        weatherInfo[weather] = baseString[weather][index]
    
    return weatherInfo

#Allows script to only be run between certain hours of the day
def shouldProgramRun():
    isScriptActive = False
    now = datetime.datetime.now()
    currentHour = now.hour
    #gives time of 10 o'clock and 24 o'clock
    if (currentHour>=9) and (currentHour <=23):
        isScriptActive = True 
    return isScriptActive

def sendMessage(message):
    # Must be greater than > 7
    waitTime = 34
    closeTime = 30 
    pywhatkit.sendwhatmsg_to_group_instantly(group_id=groupId,message=message,wait_time=waitTime,tab_close=True,close_time=closeTime)


isScriptActive = shouldProgramRun()

if not isScriptActive:
    sys.exit(0)

#Get data
response = getResponse()

responseCode = response.status_code


if responseCode == 200:
    jsonResponse = response.json()
else: sys.exit(0)

now = datetime.datetime.now() 
time = incrementTime(now=now)

index = getIndex(time=time,jsonResponse=jsonResponse)

if index != -1:
    weatherInfo = getValue(index=index,jsonResponse=jsonResponse)
else: sys.exit(0)

groupId = "groupID" #Insert Group ID

maxTemp = jsonResponse["daily"]["temperature_2m_max"][0]

message =f"""*=== Weather OVersight ===*
---------------------------
*Current Tyd:* {getCurrentTime(now)[11:16]}
*Max Temperatuur:* {maxTemp}°C

*Predection for:* {time[11:16]}
---------------------------
*Temprature:* {weatherInfo['temperature_2m']}°C
*Rain percentage:* {weatherInfo['precipitation_probability']}%
*Amount of Rain:* {weatherInfo["rain"]}mm
*Cloud Coverage:* {weatherInfo['cloud_cover']}%
"""

sendMessage(message=message)


print(message)
