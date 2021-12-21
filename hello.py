#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 17:18:21 2021

@author: clockshield
"""

profits = (10000, 20000, 30000, 40000, 50000, 10000000000000000, 1, 2, 3, 4, 5, 0)

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

max_profits = max(profits)
max_profits_index = profits.index(max_profits)
max_profits_month = months[max_profits_index]
print("The most amount of profits made is " + str(max_profits) + ". It was made in " + max_profits_month + ". ")

min_profits = min(profits)
min_profits_index = profits.index(min_profits)
print(min_profits_index)
min_profits_month = months[min_profits_index]
print("The least amount of profits made is " + str(min_profits) + ". It was made in " + min_profits_month + ". ")
