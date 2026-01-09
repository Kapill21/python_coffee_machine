# Coffee Machine Simulator (Python CLI)

A command-line coffee machine simulator built in Python. Users can order drinks (espresso/latte/cappuccino), insert coins, receive change, and the machine tracks ingredient resources and total money earned.

## Features
- Drink menu stored in a Python dictionary (ingredients + cost)
- Coin-based payment system (quarters, dimes, nickels, pennies)
- Change calculation with formatted output
- Resource tracking (water/milk/coffee) that decreases per purchase
- `report` command to display remaining resources and profit
- `off` command to shut down the machine
