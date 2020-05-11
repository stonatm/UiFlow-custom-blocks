# (c) stonatm@gmail.com
# Blynk access via REST API
class blynk:

  import urequests

  AUTH_TOKEN = ''
  initialise = False

  def _parse_in(text):
    out = str(text)
    out = out.replace('[','')
    out = out.replace(']','')
    out = out.replace('"','')
    return out

  def _parse_out(text):
    out = str(text)
    out = out.replace(' ','%20')
    return out

  def init(token):
    blynk.AUTH_TOKEN = token
    blynk.initialise = True

  def write_pin(pin, value):
    if not blynk.initialise:
      return
    url = 'http://blynk-cloud.com/' + blynk.AUTH_TOKEN + '/update/' + str(pin) + '?value=' + str(blynk._parse_out(value))
    response = blynk.urequests.get( url )
    return( blynk._parse_in(response.text) )

  def read_pin(pin):
    if not blynk.initialise:
      return
    url = 'http://blynk-cloud.com/' + blynk.AUTH_TOKEN + '/get/' + str(pin)
    response = blynk.urequests.get( url )
    return( blynk._parse_in(response.text) )

  def notify(message):
    if not blynk.initialise:
      return
    headers = {'Content-Type':'application/json'}
    values = '{"body":"' + str(message) + '"}'
    url = 'http://blynk-cloud.com/' + blynk.AUTH_TOKEN + '/notify'
    response = blynk.urequests.post( url, data = values ,headers = headers)
    return( blynk._parse_in(response.text) )

  def is_app_connected():
    if not blynk.initialise:
      return
    url = 'http://blynk-cloud.com/' + blynk.AUTH_TOKEN + '/isAppConnected'
    response = blynk.urequests.get( url )
    return( blynk._parse_in(response.text) )
