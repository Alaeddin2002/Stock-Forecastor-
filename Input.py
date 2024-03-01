"""
This code allows the user to input a stock and future date
Output is a visulaization and a predicted price for the future date
"""

def validate_ticker_symbol(ts):
    try:
        ticker = yf.Ticker(ts)
        info = ticker.info
        if info["quoteType"] == "EQUITY": # check if it's an equity (stock) symbol
            return True
        else:
            return False
    except:
        return False

def validate_date(date):
    try:
        pd.to_datetime(date)
        return True
    except:
        return False

#On a button click the inputs will be validated and the user will be prompted to re-enter if they are invalid entries
def button_clicked(_):
    button.disabled = False #allows button to be clicked multiple times
    if not validate_ticker_symbol(input_ticker_symbol.value) or not validate_date(input_date.value):
      if not validate_ticker_symbol(input_ticker_symbol.value):
          #clear the input widget
          input_ticker_symbol.value = ""
          input_ticker_symbol.placeholder = "Invalid symbol, please try again:"
      if not validate_date(input_date.value):
          #clear the input widget
          input_date.value = ""
          input_date.placeholder = "Invalid date, please try again:"
    else:
      ticker_symbol, future_date = input_ticker_symbol.value, input_date.value
      future_price = round(stock_forecast(ticker_symbol, future_date),2)
      print(f"The price will be: {future_price} on {future_date}")

#Creates label widgets
label_ticker_symbol = widgets.Label("Enter ticker symbol:")
label_date = widgets.Label("Enter future date (YYYY-MM-DD):")

#Create inputs
input_ticker_symbol = widgets.Text()
input_date = widgets.Text()

#Create the buttons
button = widgets.Button(description='Enter')

#Create vertical box layout and structure widgets
box_layout = widgets.VBox([label_ticker_symbol,input_ticker_symbol,label_date,input_date,button])

#Attach button click functions to the buttons
button.on_click(button_clicked)

#Display the layout
box_layout
