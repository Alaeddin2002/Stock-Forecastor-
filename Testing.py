#testing
#our training data ends at '2023-04-25', so to test the code, we call test days that the stock has already happened and compare.

#for example, we test what the predicted stock of Google is on April 27, which given by yahoo finance $108.37
stock_forecast("GOOG",'2023-05-27')

#We see that our code undervalues the stock, which is $107,but not by much.

#To see real change, we have to see long term prediction, so we changed the data extracted to be from 2010-01-01 to 2020-04-25
# The new price we see is $78.7, so the stock is undervalued a lot
#The conclusion we reach from our test is that our program undervalues stock prices
