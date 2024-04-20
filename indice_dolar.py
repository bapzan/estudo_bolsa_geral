import yfinance as yf
from datetime import datetime, timedelta

# Define the ticker symbols
ticker1 = 'USDBRL=X'
ticker2 = '^BVSP'

# Calculate the date 20 years ago
end_date = datetime.now()
start_date = end_date - timedelta(days=20*365)

# Download the data for the first ticker
data1 = yf.download(ticker1, start=start_date, end=end_date)

# Select only the 'Close' column
close_price1 = data1['Close']

# Download the data for the second ticker
data2 = yf.download(ticker2, start=start_date, end=end_date)

# Select only the 'Close' column
close_price2 = data2['Close']

print(close_price1)
print(close_price2)


# Gráficos

import matplotlib.pyplot as plt

# Plot the close prices do USDBRL
plt.figure(figsize=(14,7))
plt.plot(close_price1)
plt.title('Close Price of ' + ticker1)
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.show()

# Plot the close prices do Ibovespa
plt.figure(figsize=(14,7))
plt.plot(close_price2)
plt.title('Close Price of ' + ticker2)
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.show()