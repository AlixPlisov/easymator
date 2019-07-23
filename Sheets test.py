###https://habr.com/ru/post/305378/
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = '<file.json>'  # имя файла с закрытым ключом

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'test_sheet_python', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'test_sheet_python',
                               'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
}).execute()


driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
shareRes = driveService.permissions().create(
    fileId = spreadsheet['spreadsheetId'],
    body = {'type': 'anyone', 'role': 'reader'},  # доступ на чтение кому угодно
    fields = 'id'
).execute()

results = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
  "requests": [

    # Задать ширину столбца A: 317 пикселей
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": 0,
          "dimension": "COLUMNS",  # COLUMNS - потому что столбец
          "startIndex": 0,         # Столбцы нумеруются с нуля
          "endIndex": 1            # startIndex берётся включительно, endIndex - НЕ включительно,
                                   # т.е. размер будет применён к столбцам в диапазоне [0,1), т.е. только к столбцу A
        },
        "properties": {
          "pixelSize": 317     # размер в пикселях
        },
        "fields": "pixelSize"  # нужно задать только pixelSize и не трогать другие параметры столбца
      }
    },

    # Задать ширину столбца B: 200 пикселей
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": 0,
          "dimension": "COLUMNS",
          "startIndex": 1,
          "endIndex": 2
        },
        "properties": {
          "pixelSize": 200
        },
        "fields": "pixelSize"
      }
    },

    # Задать ширину столбцов C и D: 165 пикселей
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": 0,
          "dimension": "COLUMNS",
          "startIndex": 2,
          "endIndex": 4
        },
        "properties": {
          "pixelSize": 165
        },
        "fields": "pixelSize"
      }
    },

    # Задать ширину столбца E: 100 пикселей
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": 0,
          "dimension": "COLUMNS",
          "startIndex": 4,
          "endIndex": 5
        },
        "properties": {
          "pixelSize": 100
        },
        "fields": "pixelSize"
      }
    }
  ]
}).execute()


results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": "test_sheet_python!B2:C3",
         "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": [["This is B2", "This is C2"], ["This is B3", "This is C3"]]},

        {"range": "test_sheet_python!D5:E6",
         "majorDimension": "COLUMNS",  # сначала заполнять столбцы, затем ряды (т.е. самые внутренние списки в values - это столбцы)
         "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
    ]
}).execute()



request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
response = request.execute()












spreadsheet
Out[8]:
{'spreadsheetId': '1upNlY9lLJi-_Taqhzwn44WGdxsNx3OSFdzAUmTj4zU8',
 'properties': {'title': 'test_sheet_python',
  'locale': 'ru_RU',
  'autoRecalc': 'ON_CHANGE',
  'timeZone': 'Etc/GMT',
  'defaultFormat': {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1},
   'padding': {'top': 2, 'right': 3, 'bottom': 2, 'left': 3},
   'verticalAlignment': 'BOTTOM',
   'wrapStrategy': 'OVERFLOW_CELL',
   'textFormat': {'foregroundColor': {},
    'fontFamily': 'arial,sans,sans-serif',
    'fontSize': 10,
    'bold': False,
    'italic': False,
    'strikethrough': False,
    'underline': False}}},
 'sheets': [{'properties': {'sheetId': 0,
    'title': 'test_sheet_python',
    'index': 0,
    'sheetType': 'GRID',
    'gridProperties': {'rowCount': 8, 'columnCount': 5}}}],
 'spreadsheetUrl': 'https://docs.google.com/spreadsheets/d/1upNlY9lLJi-_Taqhzwn44WGdxsNx3OSFdzAUmTj4zU8/edit'}









request = service.spreadsheets().values().append(spreadsheetId=spreadsheet, range=range, valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body=body)
response = request.execute()
