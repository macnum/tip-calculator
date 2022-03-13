#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

wlcm_msg = "Welocme totip calculator!"
print(wlcm_msg)
bill = float(input("What was the total bill? $"))
print(f"${round(bill,2)}")
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
print(f"{tip}%")
people = int(input("How many people to split the bill? "))
fstb = f"{people}"

calc_total_bill = (tip / 100 * bill + bill) / people
final_amount = "{:.2f}".format(calc_total_bill)
print(f"Each person should pay: ${final_amount}")