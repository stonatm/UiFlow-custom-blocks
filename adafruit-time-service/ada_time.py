# (c) stonatm@gmail.com
# Adafruit IO Time Service
class adafruitTime:

  import urequests
  import json

  data = {"error":"Set username and aio key first"}
  USERNAME = ''
  AIOKEY = ''

  def init(user, key):
    adafruitTime.USERNAME = user
    adafruitTime.AIOKEY = key

  def refreshTime():
    headers = {"X-AIO-Key":adafruitTime.AIOKEY}
    url ="https://io.adafruit.com/api/v2/" + str(adafruitTime.USERNAME) + "/integrations/time/struct"
    response = adafruitTime.urequests.get(url, headers=headers)
    adafruitTime.data = adafruitTime.json.loads(response.text)

  def getYear():
    if 'year' in adafruitTime.data:
      return(adafruitTime.data["year"])
    else:
      return(adafruitTime.data["error"])

  def getMonth():
    if 'mon' in adafruitTime.data:
      return(adafruitTime.data["mon"])
    else:
      return(adafruitTime.data["error"])

  def getDay():
    if 'mday' in adafruitTime.data:
      return(adafruitTime.data["mday"])
    else:
      return(adafruitTime.data["error"])

  def getHour():
    if 'hour' in adafruitTime.data:
      return(adafruitTime.data["hour"])
    else:
      return(adafruitTime.data["error"])

  def getMinute():
    if 'min' in adafruitTime.data:
      return(adafruitTime.data["min"])
    else:
      return(adafruitTime.data["error"])

  def getSecond():
    if 'sec' in adafruitTime.data:
      return(adafruitTime.data["sec"])
    else:
      return(adafruitTime.data["error"])

  def getDayOfWeek():
    if 'wday' in adafruitTime.data:
      return(adafruitTime.data["wday"])
    else:
      return(adafruitTime.data["error"])

  def getDayOfYear():
    if 'yday' in adafruitTime.data:
      return(adafruitTime.data["yday"])
    else:
      return(adafruitTime.data["error"])

  def getIsDaySavingTime():
    if 'isdst' in adafruitTime.data:
      return(adafruitTime.data["isdst"])
    else:
      return(adafruitTime.data["error"])
