"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('credentials.json')
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)

service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])

# list of calendars on account
page_token = None
while True:
  calendar_list = service.calendarList().list(pageToken=page_token).execute()
  for calendar_list_entry in calendar_list['items']:
    print(calendar_list_entry['summary'])
  page_token = calendar_list.get('nextPageToken')
  if not page_token:
    break


# ======================================================================
# ======================================================================
# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.


event = {
  'summary': 'Test Event',
  # 'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'Just something small',
  'start': {
    'dateTime': '2018-04-18T09:00:00',
    'timeZone': 'America/New_York',
  },
  'end': {
    'dateTime': '2018-04-18T09:00:00',
    'timeZone': 'America/New_York',
  },
  # 'recurrence': [
  #   'RRULE:FREQ=DAILY;COUNT=2'
  # ],
  # 'attendees': [
  #   {'email': 'lpage@example.com'},
  #   {'email': 'sbrin@example.com'},
  # ],
  # 'reminders': {
  #   'useDefault': False,
  #   'overrides': [
  #     {'method': 'email', 'minutes': 24 * 60},
  #     {'method': 'popup', 'minutes': 10},
  #   ],
  # },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))