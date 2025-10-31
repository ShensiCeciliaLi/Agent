# 创建一个数据探索脚本
import yfinance as yf
import pandas as pd

# 测试多只股票
stocks = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']
for symbol in stocks:
    stock = yf.Ticker(symbol)
    hist = stock.history(period="5d")
    if not hist.empty:
        price = hist['Close'].iloc[-1]
        print(f"{symbol}: ${price:.2f}")