monthly_income=float(input("Enter the monthly income: "))
monthly_expense=float(input("Enter the monthly expense: "))
rate=0.05
monthly_savings= monthly_income - monthly_expense
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings are $",monthly_savings,"." )
print ("Projected savings after one year, with interest, is: $",projected_savings,".")