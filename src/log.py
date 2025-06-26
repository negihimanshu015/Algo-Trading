import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging

def connect(sheet_name, cred_path):

    """
    Connect to google sheets.

    Parameters
    ----------
    sheet_name: str
        Name of the google sheet.

    cred_path: str
        File path for credentials.   

    Returns
    -------
        gspread.models.Spreadsheet                       
    """

    logging.info(f"Connecting to Google Sheet: {sheet_name}")
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]    
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scope)
    client = gspread.authorize(creds)

    return client.open(sheet_name)


def log_trades(sheet, trades_df, ticker):

    """
    Log the trades to the google sheets.

    Parameters
    ----------
    sheet: str
        gspread.Spreadsheet
    
    trades_df : DataFrame
        DataFrame containing the trade records.

    ticker : str
        The stock ticker symbol.

    """
     
    sheet_title = f"Trade_log_{ticker.replace('.', '_')}"

    try:
        ws = sheet.worksheet(sheet_title)
    except:
        ws = sheet.add_worksheet(title=sheet_title, rows=100, cols=10)

    ws.clear()
    trades_df = trades_df.fillna(0)
    ws.update([trades_df.columns.tolist()] + trades_df.values.tolist())
    logging.info(f"Logged trades to {sheet_title}")


def summary(sheet, summary_dict, ticker):

    """
    Log the summary to the google sheets.

    Parameters
    ----------
    sheet: str
        gspread.Spreadsheet
    
    summary_dict : dict
        Dictionary containing metrics.

    ticker : str
        The stock ticker symbol.
                                  
    """
        
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
    logging.info(f"Logged summary data to {sheet_title}")
