import yfinance as yf

# Define the ticker symbols for the WIG20 companies
wig20_tickers = [
    'PGE.WA'
]

# Create a DataFrame to store the data for each company
wig20_data = yf.download(wig20_tickers, period="1d", group_by='ticker', auto_adjust=True)

# Print the first few rows of the data
print(wig20_data.head())
