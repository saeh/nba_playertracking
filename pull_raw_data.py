import requests
from bs4 import BeautifulSoup
import json
import pandas

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


#Load data into pandas dataframe
speed_df = pandas.DataFrame(data=speed_values,columns=speed_headers[:7]+['SPEED_' + i for i in speed_headers[7:]])
touches_df = pandas.DataFrame(data=touches_values,columns=touches_headers[:7]+['TOUCHES_' + i for i in touches_headers[7:]])
passing_df = pandas.DataFrame(data=passing_values,columns=passing_headers[:7]+['PASSING_' + i for i in passing_headers[7:]])
defense_df = pandas.DataFrame(data=defense_values,columns=defense_headers[:7]+['DEFENSE_' + i for i in defense_headers[7:]])
rebounding_df = pandas.DataFrame(data=rebounding_values,columns=rebounding_headers[:7]+['REBOUNDING_' + i for i in rebounding_headers[7:]])
drives_df = pandas.DataFrame(data=drives_values,columns=drives_headers[:7]+['DRIVES_' + i for i in drives_headers[7:]])
catchshoot_df = pandas.DataFrame(data=catchshoot_values,columns=catchshoot_headers[:7]+['CATCHSHOOT_' + i for i in catchshoot_headers[7:]])
pullup_df = pandas.DataFrame(data=pullup_values,columns=pullup_headers[:7]+['PULLUP_' + i for i in pullup_headers[7:]])
shooting_df = pandas.DataFrame(data=shooting_values,columns=shooting_headers[:7]+['SHOOTING_' + i for i in shooting_headers[7:]])

#shotchart data looks a little wrong.... don't merge in with rest
shotchart_df = pandas.DataFrame(data=shotchart_values,columns=['SHOTCHART_' + i for i in shotchart_headers])

#merge data frames together on common data points
player_df = pandas.merge(speed_df,touches_df, on=['PLAYER_ID','PLAYER','FIRST_NAME','LAST_NAME','TEAM_ABBREVIATION','GP','MIN'], how='outer')
player_df = pandas.merge(player_df,passing_df, on=['PLAYER_ID','PLAYER','FIRST_NAME','LAST_NAME','TEAM_ABBREVIATION','GP','MIN'], how='outer')
player_df = pandas.merge(player_df,defense_df, on=['PLAYER_ID','PLAYER','FIRST_NAME','LAST_NAME','TEAM_ABBREVIATION','GP','MIN'], how='outer')
player_df = pandas.merge(player_df,rebounding_df, on=['PLAYER_ID','PLAYER','FIRST_NAME','LAST_NAME','TEAM_ABBREVIATION','GP','MIN'], how='outer')
player_df = pandas.merge(player_df,drives_df, on=['PLAYER_ID','PLAYER','FIRST_NAME','LAST_NAME','TEAM_ABBREVIATION','GP','MIN'], how='outer')
player_df = pandas.merge(player_df,catchshoot_df, on=['PLAYER_ID','PLAYER','FIRST_NAME','LAST_NAME','TEAM_ABBREVIATION','GP','MIN'], how='outer')
player_df = pandas.merge(player_df,pullup_df, on=['PLAYER_ID','PLAYER','FIRST_NAME','LAST_NAME','TEAM_ABBREVIATION','GP','MIN'], how='outer')
player_df = pandas.merge(player_df,shooting_df, on=['PLAYER_ID','PLAYER','FIRST_NAME','LAST_NAME','TEAM_ABBREVIATION','GP','MIN'], how='outer')

#save to csv
player_df.to_csv('players.csv')
shotchart_df.to_csv('shotchart.csv')


