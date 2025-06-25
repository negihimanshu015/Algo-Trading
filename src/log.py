import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect(sheet_name, cred_path):
    scope = ["https://spreadsheets.google.com/feeds"]    
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name)

def log_trades(sheet, trades_df):
    try:
        ws = sheet.worksheet("Trade_log")
    except:
        ws = sheet.add_worksheet(title="Trade_log", rows=100, cols=10)
    ws.clear()
    trades_df = trades_df.fillna(0)
    ws.update([trades_df.columns.tolist()] + trades_df.values.tolist())

def summary(sheet, summary_dict):
    try:
        ws = sheet.worksheet("Summmary")
    except:
        ws = sheet.add_worksheet(title="Summary", rows=20, cols=2)
    ws.clear()

    rows=[]
    for key, value in summary_dict.items():
        rows.append([key,value])
    ws.update(rows)
