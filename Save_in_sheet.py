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
import sys, os
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

path_to_current_file = os.path.realpath(__file__)
path_to_current_folder = os.path.dirname(path_to_current_file)

def save_data(time, num, ads, res, cel) -> None:
    print('Начинаю процедуру выгрузки данных')
    CREDENTIALS_FILE = os.path.realpath(path_to_current_folder+'< File.json>')   # Key secret file
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                      'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    # The ID of the spreadsheet to update.
    spreadsheet_id = '1xMCmtWikFkxXkcz2oqE74dtcHk6yAVtIymDNHm31KlM'  # ID table
    range_ = '<Name of range>!A1:B1'
    value_input_option = 'RAW'
    insert_data_option = 'INSERT_ROWS'
    value_range_body = {"values": [[time, num, ads, res, cel]],}  # Insert data
    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id,
                                                     range=range_,
                                                     valueInputOption=value_input_option,
                                                     insertDataOption=insert_data_option,
                                                     body=value_range_body)
    response = request.execute()
    print('Данные выгружены!')
    return print('Результат сохранения в таблицу гугл: '+str(response))

