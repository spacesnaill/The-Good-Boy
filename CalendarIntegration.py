
#DONE import the google calendar API
#DONE make a method to push events to the calendar
#TODO make a method to pull events from a specific day on the calendar
#TODO make a method to remove an event from the calendar
#TODO make a method to edit an event on the calendar
#TODO make a method to post the events for the day at 7am EST or post 'No events' if no events (this'll probably be implemented in bot.py)

import httplib2
import os
import re

from apiclient import discovery
from oauth2client import client, tools, file

from settings import CALENDAR

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
        self.CALENDAR_ID = CALENDAR
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

    #creates an all day event on the specified day description is optional
    def create_event(self, title, day, time=0, description = ''):
        #TODO refactor this to accept times and be mindful of incorrect formatting

        #check the make sure the format of the date is correct, if it is not return an error message
        if not re.match(r'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]', day):
            return "The format of your date is incorrect. Please make sures it follows this format: YYYY-MM-DD"

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
        return 'Success'

    #returns all the events on a specified day
    #grabs all the event summaries from the given day, stores them in output_list and then returns that list
    def check_day(self, day):
        if not re.match(r'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]', day):
            return "The format of your date is incorrect. Please make sures it follows this format: YYYY-MM-DD"

        date = day.split('-')
        #date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        page_token = None
        output_list = []
        while True:
            events = self.service.events().list(calendarId = self.CALENDAR_ID,
                                                timeMin='{}-{}-{}T00:00:00Z'.format(date[0], date[1], date[2]),
                                                timeMax='{}-{}-{}T00:00:00Z'.format(date[0], date[1], (int(date[2])+1)),
                                                pageToken = page_token,
                                                ).execute()
            for event in events['items']:
                output_list.append(event['summary'])
            page_token = events.get('nextPageToken')
            if not page_token:
                return output_list

