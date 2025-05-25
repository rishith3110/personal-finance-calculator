print("PERSONAL FINANCE CALCULATOR")

def budget_planner():
    income = float(input("please enter the user income: "))
    expenses = float(input("please enter the user expenses: "))
    remaining_disposable_income = income - expenses
    print(f"the remaining disposable income is: {remaining_disposable_income:.2f}")  
budget_planner()
def loan_calculator():
    print("PERSONAL HOME LOAN!!")
    principal_amt = float(input("please enter the principal amount to calculate loan amount: "))
    if principal_amt > 0:
        if principal_amt > 200000 or principal_amt < 1000000:
            interest_rate = principal_amt * 0.04
            tenure = 3650
            total_amt = principal_amt + interest_rate
            print(f"the principal amount is: {principal_amt:.2f}")
            print(f"the interest amount is: {interest_rate:.2f}")
            print(f"the tenure period (days*years) is: {tenure}")
            print(f"the total amount is: {total_amt:.2f}")
        elif principal_amt > 1500000 or principal_amt < 2500000:
            interest_rate = principal_amt * 0.07
            tenure = 3650
            total_amt = principal_amt + interest_rate
            print(f"the principal amount is: {principal_amt:.2f}")
            print(f"the interest amount is: {interest_rate:.2f}")
            print(f"the tenure period (days*years) is: {tenure}")
            print(f"the total amount is: {total_amt:.2f}")
        elif principal_amt < 200000:
            interest_rate = principal_amt * 0.00
            tenure = 0
            total_amt = principal_amt + interest_rate
            print(f"the principal amount is: {principal_amt:.2f}")
            print(f"the interest amount is: {interest_rate:.2f}")
            print(f"the tenure period (days*years) is: {tenure}")
            print(f"the total amount is: {total_amt:.2f}")
        else:
            print(f"the principal amount is: {principal_amt:.2f}")
            print(f"the interest amount is: {interest_rate:.2f}")
            print(f"the tenure period (days*years) is: {tenure}")
            print(f"the total amount is: {total_amt:.2f}")
    else:
        print("Invalid input principal amount!")
        count = 0  
        while count < 3:   
            principal_amt = float(input("Please re-enter the principal amount: "))  
            if principal_amt > 0:
                loan_calculator()  
                return  
            else:
                print("Invalid input! Please try again.")  
                count += 1  
        print("Sorry! Your chances are completed. Please try again after some time.")  
loan_calculator()
def expense_tracker():
    print("Expense Tracker - Enter your expenses!")
    food = []
    entertainment = []
    bills = []
    savings = []
    while True:
        item = input("Enter an expense item ((food/entertainment/bills) or type 'exit' to stop: ").strip().lower()
        if item == "exit":
            break  
        cost = float(input(f"Enter cost for {item}: "))
        category = input("Enter category (food/entertainment/bills): ").strip().lower()
        if category == "food":
            food.append(f"{item}: ${cost:.2f}")
        elif category == "entertainment":
            entertainment.append(f"{item}: ${cost:.2f}")
        elif category == "bills":
            bills.append(f"{item}: ${cost:.2f}")
        else:
            print("Invalid category! Please enter food, entertainment, or bills.")
    print("\nYOUR LOGGED EXPENSES:")
    print(f"Food: {food if food else 'None'}")
    print(f"Entertainment: {entertainment if entertainment else 'None'}")
    print(f"Bills: {bills if bills else 'None'}")
expense_tracker()
def savings_estimator():
    income = float(input("please enter the monthly income: "))
    savings = float(input("please enter the monthly savings: "))
    savings_rate = (savings / income) * 100
    print(f"the future savings are {savings_rate} based on monthly savings rate")
savings_estimator()
import matplotlib.pyplot as plt
categories = ["Food" , "Entertainment" , "Bills" , "Savings"]
expenses = [5000 , 6000, 1000, 8000]
plt.bar(categories, expenses, color=['blue', 'red', 'green', 'orange'])
plt.xlabel("Expense Categories")
plt.ylabel("Amount Spent ($)")
plt.title("Monthly Expense Report")
plt.show()



