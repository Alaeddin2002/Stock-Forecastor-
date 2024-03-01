"""
This code will create a linear regression model that is trained on the historical data of a stock
Output is a visulaization and a predicted price for the future date
"""

def stock_forecast(ticker, future_date):
    today = date.today()
    date_of_today = ''
    date_of_future = ''

    # transform dates from format YYYY-MM-DD to YYYYMMDD
    for i in str(today):
      if i.isdigit() == True:
        date_of_today+=(i)

    for i in str(future_date):
      if i.isdigit() == True:
        date_of_future+=(i)

    # get the number of days we need to forecast
    amount_of_days = ''
    forecast_days = str(datetime.datetime.strptime(date_of_future, '%Y%m%d') - datetime.datetime.strptime(date_of_today, '%Y%m%d'))
    for i in range(7):
      if forecast_days[i].isdigit():
        amount_of_days+=forecast_days[i]

    forecast_days = int(amount_of_days)
    #forecast days =  print(datetime.datetime.strptime(future_date, '%Y%m%d') - datetime.datetime.strptime('20230425', '%Y%m%d'))
    # get historical data from yahoo finance
    stock_data = yf.download(ticker, start='2010-01-01', end='2023-05-02')

    # create a new DataFrame with just the date and close columns
    df = pd.DataFrame({'Date': stock_data.index, 'Close': stock_data['Close']})
    # Set date as index
    df.set_index('Date', inplace=True)

    # Create feature matrix and target vector
    X = df.index.astype(int).values.reshape(-1, 1)
    y = df['Close'].values.reshape(-1, 1)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict the future closing prices
    last_date = df.index[-1]
    # future_dates = pd.date_range(last_date, periods=forecast_days+1, freq='B')[1:]
    future_dates = pd.date_range(start=last_date, end=future_date)
    future_dates_int = future_dates.astype(int).values.reshape(-1, 1)
    future_closing_prices = model.predict(future_dates_int).flatten()

    # Create a dataframe with future dates and closing prices
    future_df = pd.DataFrame({'Date': future_dates, 'Close': future_closing_prices})

    # Plot the historical and future closing prices
    plt.plot(df['Close'])
    plt.plot(future_df['Date'],future_df['Close'])
    #df.plot()
    #future_df.plot(x='Date', y='Close', legend=True)
    for i in range(len(future_df['Date'])):
      if future_df['Date'][i] == datetime.datetime.strptime(date_of_future, '%Y%m%d'):
        price = (future_df['Close'][i])
    return price

stock_forecast("META",'2028-05-02')
