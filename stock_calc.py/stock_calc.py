# Title: Stock Transaction Program
# Program created by William Schaeffer
# CPS 313
# P. 115-116, Exercise 12, Stock Transaction Program
# 01.18.22

# This program will display values from the purchase and sale of stock

# CONSTANTS

PURCHASE_AMOUNT = 2000
PURCHASE_PRICE = 40.00
SALE_AMOUNT = 2000
SALE_PRICE = 42.75
PURCHASE_COMMISSION = .03
SALE_COMMISSION = .03

# Calculations

purchaseTotal = PURCHASE_AMOUNT * PURCHASE_PRICE
purchaseCommissionTotal = purchaseTotal * PURCHASE_COMMISSION
saleTotal = SALE_AMOUNT * SALE_PRICE
saleCommissionTotal = saleTotal * SALE_COMMISSION
purchaseTotal = PURCHASE_AMOUNT * PURCHASE_PRICE
netProfit = saleTotal - purchaseTotal - purchaseCommissionTotal - saleCommissionTotal

# Display with a comma for easy reading of large numbers and floating-point to 2 decimals for currency

print(f'Purchase Total: ${purchaseTotal:,.2f}')
print(f'Purchase Commission: ${purchaseCommissionTotal:,.2f}')
print(f'Sale Total: ${saleTotal:,.2f}')
print(f'Sale Commission Total: ${saleCommissionTotal:,.2f}')
print(f'Net Profit: ${netProfit:,.2f}')

if netProfit > 0:
    print(f'You made a profit!')
elif netProfit < 0:
    print(f'You incured a loss.')
else: 
    print(f'You did not make profit or incur a loss.')