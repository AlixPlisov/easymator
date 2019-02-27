"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""

import httplib2
import os
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


def save_data(time, num, ads, res, cel) -> str:
    """Save data in Google Sheet"""
    print('safe data start')
    CREDENTIALS_FILE = os.path.dirname(__file__)+'/<Key secret file>'  # Key secret file (Easymator folder)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    spreadsheet_id = '<ID table>'  # Table ID
    range_ = '<SheetID>!A1:B1'  # Sheet ID
    value_input_option = 'RAW'
    insert_data_option = 'INSERT_ROWS'
    value_range_body = {"values": [[time, num, ads, res, cel]],}  # Insert data
    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id,
                                                     range=range_,
                                                     valueInputOption=value_input_option,
                                                     insertDataOption=insert_data_option,
                                                     body=value_range_body)
    response = request.execute()
    print('safe data end')
    return print('Results: ' + str(response))
