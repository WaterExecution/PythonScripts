import urllib, urllib2, cookielib

username = 'username'
password = 'password'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'j_username' : username, 'j_password' : password})
opener.open('https://website.com/_login', login_data)
resp = opener.open('https://website.com/hiddenpage')
print resp.read()
