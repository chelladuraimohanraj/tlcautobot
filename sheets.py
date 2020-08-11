import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from io import StringIO

class sheet:
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json',self.scope)
        self.client = gspread.authorize(self.creds)
    def opensheet(self,name):
        self.sheet = self.client.open("tlc").worksheet(name)
    def getids(self):
        self.availableids=self.sheet.col_values(1)
        return self.availableids
    def insertrow(self,id,string):
        row=[id,string]
        self.sheet.insert_row(row,1)
    def getrow(self,number):
        cell=self.sheet.find(number)
        values=self.sheet.cell(cell.row,cell.col+1).value
        return values

# s=sheet()
# s.opensheet('CSHARP')
# k=s.getrow('2118110106')
# k=k.replace('\u200b','')
# line=StringIO(k)
# m=(line.readlines())

# print(m)