import requests         # Gets weather info from openweathermap.org, parses the response as JSON, and uses it in output

r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Boise&&appid=344143366e48285f89319137af3b0853')
res = r.json()
print "Boise's coordinates are: \nlattitude: {} \nlongitude {}".format(res['coord']['lat'], res['coord']['lon'])
print "Current temperature in Boise is {} degrees Kelvin, which doesn't mean anything to anyone.".format(res['main']['temp'])
