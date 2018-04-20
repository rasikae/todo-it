# ======================================================================
# ======================================================================
# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
# from task.models import User, Credentials
import datetime
from datetime import timedelta

# variables used for testing
# title = 'Test'
# startdate = datetime.datetime.today()
# enddate = startdate + timedelta(1)
# desc = 'Nothing'


def addEvent2Calendar(user,title,startdate,enddate,desc):
    print("Setting up calendar")

    SCOPES = 'https://www.googleapis.com/auth/calendar'
    # stores user credentials to access their google account     
    store = file.Storage('credentials.json')

    print("Check here")
    
    # gets stored credentials
    creds = store.get()
    
    print("or here")

    # if credentials for user is not found, create credentials
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)

    print("maybe here")

    # builds the service to connect the user to the api
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    print("check here too")

    # converts dates into string format instead of datetime.datetime format
    startdate = startdate.strftime('%Y-%m-%d')
    enddate = enddate.strftime('%Y-%m-%d')

    print("Adding event to calendar")

    # sets up json event
    event = {
      'summary': title,
      'description': desc,
      'start': {
        'date': startdate,
        'timeZone': 'America/New_York',
      },
      'end': {
        'date': enddate,
        'timeZone': 'America/New_York',
      },
    }

    print("final check")

    # insert the event into the user's google calendar
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))