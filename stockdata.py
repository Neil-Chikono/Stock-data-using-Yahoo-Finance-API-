import yfinance as yf 

# select company 

ticker = "AAPL"

stock = yf.Ticker(ticker)

#download the last five days of prices 

data = stock.history(period="5d")

print("stock:" , ticker)

print(data)

#get latest available closing price 

if not data.empty:
    latest_price =data["close"].iloc [-1]
    print(f"\nLatest closing price: ${latest_price:. 2f}")
else: 
    print ("no price data available")
