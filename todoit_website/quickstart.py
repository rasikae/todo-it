# ======================================================================
# ======================================================================
# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
from datetime import timedelta

# title = 'Test'
# startdate = datetime.datetime.today()
# enddate = startdate + timedelta(1)
# desc = 'Nothing'


def addEvent2Calendar(title,startdate,enddate,desc):
    print("Setting up calendar")
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('credentials.json')
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)

    service = build('calendar', 'v3', http=creds.authorize(Http()))

    startdate = startdate.strftime('%Y-%m-%d')
    enddate = enddate.strftime('%Y-%m-%d')

    print("Adding event to calendar")
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

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

