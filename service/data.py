import gspread as gs
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials as sac

class spread_sheet():
    def __init__(self, id:str):
        self.id = id
        self.creds = sac.from_json_keyfile_name(
            filename='service/Token.json',
            scopes=[
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
        )
        self.auth = gs.authorize(self.creds)
    
    def post(self, data:list, row:int, sheet:int):
        work = self.auth.open_by_key(self.id).get_worksheet(sheet)
        work.insert_rows(data, row)
    
    def get(self, sheet:int):
        work = self.auth.open_by_key(self.id).get_worksheet(sheet)
        return pd.DataFrame(work.get_all_records())
    
    def delete(self, sheet:int, start:int, end:int):
        work = self.auth.open_by_key(self.id).get_worksheet(sheet)
        work.delete_rows(start, end)