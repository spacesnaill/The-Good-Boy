
#DONE import the google calendar API
#DONE make a method to push events to the calendar
#TODO make a method to pull events from a specific day on the calendar
#TODO make a method to remove an event from the calendar
#TODO make a method to edit an event on the calendar
#TODO make a method to post the events for the day at 7am EST or post 'No events' if no events (this'll probably be implemented in bot.py)

import httplib2
import os

from apiclient import discovery
from oauth2client import client, tools, file

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents = [tools.argparser]).parse_args()
except ImportError:
    flags = None


class CalendarIntegration:
    def __init__(self):
        self.SCOPES = 'https://www.googleapis.com/auth/calendar'
        self.CLIENT_SECRET_FILE = 'client_secret.json'
        self.APPLICATION_NAME = 'The Good Boy'
        self.CALENDAR_ID = ''
        self.store = file.Storage('client_id.json')

        #Set up credentials
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'calendar-credentials.json')
        store = file.Storage(credential_path)
        self.credentials = store.get()
        if not self.credentials or self.credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                self.credentials = tools.run_flow(flow, store, flags)
            print('Storing credentials to ' + credential_path)

        #Set up service
        http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http = http)

    def create_event(self, title, day, description = ''):
        #TODO refactor this to accept times and be mindful of incorrect formatting
        event = {
            'summary' : '{}'.format(title),
            'location' : 'Roll20',
            'description' : '{}'.format(description),
            'start' : { 'date' : '{}'.format(day),
                        'timeZone' : 'America/New_York'},
            'end' : {'date' : '{}'.format(day),
                        'timeZone' : 'America/New_York'}
        }
        event = self.service.events().insert(calendarId = self.CALENDAR_ID, body = event).execute()
        return 'Event created as: %s' % (event.get('htmlLink'))





