import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect(sheet_name, cred_path):
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]    
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name)

def log_trades(sheet, trades_df, ticker):
    sheet_title = f"Trade_log_{ticker.replace('.', '_')}"
    try:
        ws = sheet.worksheet(sheet_title)
    except:
        ws = sheet.add_worksheet(title=sheet_title, rows=100, cols=10)
    ws.clear()
    trades_df = trades_df.fillna(0)
    ws.update([trades_df.columns.tolist()] + trades_df.values.tolist())

def summary(sheet, summary_dict, ticker):
    sheet_title = f"Summary_{ticker.replace('.', '_')}"
    try:
        ws = sheet.worksheet(sheet_title)
    except:
        ws = sheet.add_worksheet(title=sheet_title, rows=20, cols=2)
    ws.clear()

    rows=[]
    for key, value in summary_dict.items():
        rows.append([key,value])
    ws.update(rows)
