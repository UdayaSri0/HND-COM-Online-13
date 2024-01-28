import datetime

current_year = datetime.datetime.now().year

#print(current_year)

input_name = input("What is your name? ")
input_age = int(input("How old are you? "))

year_turn_100 = current_year + (100 - input_age)

print(f"hello {input_name}, you will turn 100 in {year_turn_100}")