#Ryan Malani
#Final Project

#raw packages
import numpy as np
import pandas as pd

#data source
import yfinance as yf

#data visualization (chart)
import plotly.graph_objs as graph

#getting user input for API arguments
tick = input('Enter Ticker(s) (Ex: AAPL): ')
per = input('Enter Time Period (Ex: 5d): ')
inv = input('Enter Time Interval (Ex: 15m): ')

#using user inputs as API arguments
data = yf.download(tickers=tick, period=per, interval=inv)

#shows a table of the market data for the selected time frame
data

#declaring the figure
chart = graph.Figure()

# Adding 'candlesticks' to the chart
chart.add_trace(graph.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))

#adding titles to the chart
chart.update_layout(
    title=tick + ' chart for the last ' + per,
    yaxis_title='Stock Price (USD per Share)')

#adding X-Axes to the chart
chart.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label ="1m", step="minute", stepmode="backward"),
            dict(count=5, label="5m", step="minute", stepmode="backward"),
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=30, label="30m", step="minute", stepmode="backward"),
            dict(count=1, label="1h", step="hour", stepmode="backward"),
            dict(count=2, label="2h", step="hour", stepmode="backward"),
            dict(count=4, label="4h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#showing the chart
chart.show()
