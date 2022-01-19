# Title: Stock Transaction Program
# Program created by William Schaeffer
# CPS 313
# P. 115-116, Exercise 12, Stock Transaction Program - Instructor's Instructions
# 01.18.22

# This program will display values from the purchase and sale of stock

# Variable Declaration

    # Variables for user input

purchaseAmount = 0.0                # Number of stock shares purchased
purchasePrice = 0.0                 # Price of stock share when purchasd
saleAmount = 0.0                    # Number of stock shares sold
salePrice = 0.0                     # Price of stock share when sold
purchaseCommission = 0.0            # Percentage of commission for each purchase
saleCommission = 0.0                # Percentage of commission for each sale

    # Variables for calculation

purchaseTotal = 0.0                 # Total of purchase, purchaseAmount * purchasePrice
purchaseCommissionTotal = 0.0       # Total of purchase commission, purchaseTotal * purcahseCommision
saleTotal = 0.0                     # Total of sale, saleAmount * salePrice
saleCommissionTotal = 0.0           # Total of sale commission, saleTotal * saleCommission
netProfit = 0.0                     # Total profit, saleTotal - purchaseTotal - purchaseCommision - saleCommission

# User input

purchaseAmount = float(input('How many stock shares did you purchase? '))
purchasePrice = float(input('At what price did you purchase each stock? '))
saleAmount = float(input('How many stock shares did you sell? '))
salePrice = float(input ('At what price did you sell each stock? '))
purchaseCommission = float(input('What is the commission for purchases with your stock broker? '))
saleCommission = float(input('What is the commission for sales with your stock broker? '))

# Calculations

purchaseTotal = purchaseAmount * purchasePrice
purchaseCommissionTotal = purchaseTotal * purchaseCommission
saleTotal = saleAmount * salePrice
saleCommissionTotal = saleTotal * saleCommission
netProfit = saleTotal - purchaseTotal - purchaseCommissionTotal - saleCommissionTotal

# Display with a comma for easy reading of large numbers and floating-point to 2 decimals for currency

print(f'Purchase Total: ${purchaseTotal:,.2f}')
print(f'Purchase Commission: ${purchaseCommissionTotal:,.2f}')
print(f'Sale Total: ${saleTotal:,.2f}')
print(f'Sale Commission Total: ${saleCommissionTotal:,.2f}')
print(f'Net Profit: ${netProfit:,.2f}')

# Display text to indicate if transaction was a loss, profit, or neutral
    # if greater than 0, profit. If less than 0, loss. 

if netProfit > 0:
    print(f'You made a profit!')
elif netProfit < 0:
    print(f'You incured a loss.')
else: 
    print(f'You did not make profit or incur a loss.')