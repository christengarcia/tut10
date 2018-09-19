#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Function to calculate multiple order totals and apply any applicable discount
"""
# Stock prices
price = {'book': 10.0, 'magazine': 5.5, 'newspaper': 2.0}

# Separate orders   
order1 = {'book': 10}
order2 = {'book': 1, 'magazine': 3}
order3 = {'magazine': 5, 'book': 10}

# Calculate total price on orders
# Add discount to orders if applicable 
def calculate_price(price, order):
    order_basket = []
    for key, value in price.items():
        # Raise KeyError if item does not have a price
        if price[key] < 0: 
            raise KeyError('item in order does not have price value') 
        # Check if item has a match in stock    
        if key in order:            
            gross = float(price[key]) * float(order[key])            
            order_basket.append(gross)
        # Sum total on each iteration        
        gross_total = 0
        for sub_total in order_basket:
            gross_total = gross_total + sub_total             
    # Add discount if applicable
    if gross_total > 100.00:
        discount = gross_total * 10 / 100
        discounted_price = gross_total - discount
        return discounted_price
    elif gross_total > 50.00:
        discount = gross_total * 5 / 100
        discounted_price = gross_total - discount
        return discounted_price
    else:
        return gross_total

# Verify calculations are correct
assert(95 == calculate_price(price, order1))
assert(26.5 == calculate_price(price, order2))
assert(114.75 == calculate_price(price, order3))
print("Done")