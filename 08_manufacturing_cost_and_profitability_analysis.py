"""Case Study 8: Manufacturing Cost and Profitability Analysis
Calculate production cost, revenue, profit or loss, and profit margin.
"""

quantity = int(input("Quantity produced: "))
cost_per_item = float(input("Cost per item (₹): "))
selling_price = float(input("Selling price per item (₹): "))

if quantity < 0 or cost_per_item < 0 or selling_price < 0:
    print("Invalid input. Values cannot be negative.")
else:
    total_cost = quantity * cost_per_item
    revenue = quantity * selling_price
    profit = revenue - total_cost
    margin = (profit / revenue * 100) if revenue > 0 else 0

    if profit > 0:
        status = "Profit"
    elif profit < 0:
        status = "Loss"
    else:
        status = "Break-even"

    print(f"Total production cost: ₹{total_cost:.2f}")
    print(f"Total revenue: ₹{revenue:.2f}")
    print(f"Profit/Loss: ₹{profit:.2f}")
    print(f"Status: {status}")
    print(f"Profit margin: {margin:.2f}%")
