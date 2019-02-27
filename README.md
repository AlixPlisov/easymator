# easymator

What is it?
-----------

The Easymator is a project for automating workflows. After filling in the 
fields on the HTML page, it automatically finds the necessary data in 
the Gmail and sends the correctly formatted data to Google Sheets.

This program is designed for call center operators. Its main task: after 
entering the source of advertising, to find the number from which there 
was a call, which is in the mail and to save data in a table on its own. 
In some scenarios, providing a report and results to the user in a browser.

Documentation
-------------

For the program to work properly, you need to fill in the following data in the file 
"MangoParser.py":
1. Auth data. This is your Gmail login and password.
2. Key word for searching. Key word for searching in Gmail inbox.

and 

"Save_in_sheet.py":
1. Key secret file (Easymator folder). The google service account secret file for write to you GSheets
Installation.
2. Table ID. Spreadsheet ID.
3. Sheet ID. Sheets ID.
------------

Install
---------

Requires version Python3 and newer.
Just type in console/terminal: 'Python3' and url file 'Flaskstart.py'.


Contacts
--------

GitHub: https://github.com/AlixPlisov
Mail: pllisovalix@gmail.com
Tel. +79094441987
