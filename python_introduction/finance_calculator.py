#!/bin/bash
monthly_income = float(input("Enter yoour monthly income: "))
total_monthly_expenses = float(input("Enter your monthly expeenses: "))

monthly_savings = monthly_income - total_monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print("Your monthly savings are $" monthly_savings)
print("Projected savings after one year, with interest, is: $" projected_savings)