import requests
from bs4 import BeautifulSoup
import json

## Player Tracking Speed
url = 'stats.nba.com/js/data/sportvu/speedData.js'
url = 'http://%s' % url
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
idx = r.content.find('=') + 2
try:
    stats = json.loads(r.content[idx:-1])['resultSets'][0]
    speed_headers = stats['headers']
    speed_values = stats['rowSet']
except:
    print 'Could not parse %s' % url

## Player Tracking Touches
url = 'stats.nba.com/js/data/sportvu/touchesData.js'
url = 'http://%s' % url
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
idx = r.content.find('=') + 2
try:
    stats = json.loads(r.content[idx:-1])['resultSets'][0]
    touches_headers = stats['headers']
    touches_values = stats['rowSet']
except:
    print 'Could not parse %s' % url

## Player Tracking Passing
url = 'stats.nba.com/js/data/sportvu/passingData.js'
url = 'http://%s' % url
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
idx = r.content.find('=') + 2
try:
    stats = json.loads(r.content[idx:-1])['resultSets'][0]
    passing_headers = stats['headers']
    passing_values = stats['rowSet']
except:
    print 'Could not parse %s' % url

## Player Tracking Defense
url = 'stats.nba.com/js/data/sportvu/defenseData.js'
url = 'http://%s' % url
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
idx = r.content.find('=') + 2
try:
    stats = json.loads(r.content[idx:-1])['resultSets'][0]
    defense_headers = stats['headers']
    defense_values = stats['rowSet']
except:
    print 'Could not parse %s' % url

## Player Tracking Rebounding
url = 'stats.nba.com/js/data/sportvu/reboundingData.js'
url = 'http://%s' % url
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
idx = r.content.find('=') + 2
try:
    stats = json.loads(r.content[idx:-1])['resultSets'][0]
    rebounding_headers = stats['headers']
    rebounding_values = stats['rowSet']
except:
    print 'Could not parse %s' % url

## Player Tracking Drives
url = 'stats.nba.com/js/data/sportvu/drivesData.js'
url = 'http://%s' % url
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
idx = r.content.find('=') + 2
try:
    stats = json.loads(r.content[idx:-1])['resultSets'][0]
    drives_headers = stats['headers']
    drives_values = stats['rowSet']
except:
    print 'Could not parse %s' % url

## Player Tracking Catch and Shoot
url = 'stats.nba.com/js/data/sportvu/catchShootData.js'
url = 'http://%s' % url
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
idx = r.content.find('=') + 2
try:
    stats = json.loads(r.content[idx:-1])['resultSets'][0]
    catchshoot_headers = stats['headers']
    catchshoot_values = stats['rowSet']
except:
    print 'Could not parse %s' % url

## Player Tracking Pull Up
url = 'stats.nba.com/js/data/sportvu/pullUpShootData.js'
url = 'http://%s' % url
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
idx = r.content.find('=') + 2
try:
    stats = json.loads(r.content[idx:-1])['resultSets'][0]
    pullup_headers = stats['headers']
    pullup_values = stats['rowSet']
except:
    print 'Could not parse %s' % url

## Player Tracking Shooting
url = 'stats.nba.com/js/data/sportvu/shootingData.js'
url = 'http://%s' % url
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
idx = r.content.find('=') + 2
try:
    stats = json.loads(r.content[idx:-1])['resultSets'][0]
    shooting_headers = stats['headers']
    shooting_values = stats['rowSet']
except:
    print 'Could not parse %s' % url

# Shot chart
url = 'http://stats.nba.com/stats/shotchartdetail?SeasonType=Regular%20Season&Season=2013-14&Period=0&LastNGames=0&GameSegment=&Position=&RookieYear=&Month=0&VsDivision=&VsConference=&OpponentTeamID=0&DateTo=&DateFrom=&SeasonSegment=&TeamID=1610612752&PlayerID=2747&Location=&GameID=0021301149&ContextMeasure=FG3A&Outcome='
r = requests.get(url)
if r.status_code != 200:
    print 'Request failed: %s' % url
try:
    chart = json.loads(r.content)['resultSets'][0]
    shotchart_headers = chart['headers']
    shotchart_values = chart['rowSet']
except:
    print 'Could not parse %s' % url




