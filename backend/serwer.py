from datetime import datetime
from psycopg2 import pool


#from logic import BOUGHT, SOLD
#from logic import format_db_row_to_transaction


import yfinance as yf

# Define the ticker symbols for the WIG20 companies
wig20_tickers = [
    'PGE.WA'
]

# Create a DataFrame to store the data for each company
wig20_data = yf.download(wig20_tickers, period="2d", group_by='ticker', auto_adjust=True)

# Print the first few rows of the data
print(wig20_data.head())

postgreSQL_pool = pool.SimpleConnectionPool(
    1,
    20,
    database="exampledb",
    user="docker",
    password="docker",
    host="0.0.0.0"
)

