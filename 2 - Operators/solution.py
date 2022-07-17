
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    taxes = (tax_percent / 100) * meal_cost

    print(round(meal_cost + tip + taxes))


meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())
solve(meal_cost, tip_percent, tax_percent)
