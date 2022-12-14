# Bank account task
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group


START_DEPOSIT = 1000
FINAL_DEPOSIT = 2000
def count_month(percent):
    count = 1
    deposit = START_DEPOSIT

    while deposit <= FINAL_DEPOSIT:
        deposit = round((deposit + (deposit * percent) / 100), 2)
        count += 1
    return (count, deposit)
 
def main():

    percent = int(input("Please enter percentage: "))
    count, deposit = count_month(percent)

    if 0 < percent < 25:
        msg = f"After {count} months your deposit will be: {deposit}"
    else:
        msg = f"Wrong number of percent"

    print(msg)

main()




