import pyinputplus as pyip

#User input for investment variables
initial_investment = pyip.inputNum('What is your initial investment? ')
time_invested = pyip.inputNum('How many years will you hold your investment? ')
monthly_investment = pyip.inputNum('How much will you invest each month? ')
interest_rate = (pyip.inputNum('What is your APY(%)? ') * .01)

#Set balance to initial investment before starting loop
balance = initial_investment

#Iterate over time_invested to calculate
for i in range(time_invested):
    interest_yearly = balance * interest_rate
    balance += interest_yearly
    balance += monthly_investment * 12

#Print final results
print(f'After {time_invested} years, your account would be worth ${balance}.')