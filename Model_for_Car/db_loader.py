import pyodbc
import pandas as pd

def fetch_data_from_sql(server, database, username, password):
    """
    Connects to SQL Server and executes a query to fetch seismic data.
    """
    connection_string = (
        f'DRIVER={{SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    
    try:
        cnxn = pyodbc.connect(connection_string)
        query = "SELECT [GEOPHONE-Z], [TIMESTAMP], [Class] FROM dbo.FINAL;"
        df = pd.read_sql(query, cnxn)
        cnxn.close()
        return df
    except Exception as e:
        print(f"Database connection error: {e}")
        return None