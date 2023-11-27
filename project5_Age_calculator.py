from datetime import datetime

def Calculate_Age():
    print(f"\n{'~'*50}\n{'Welcome to Age Calculator'.center(50)}\n{'~'*50}")    
    current_Age=datetime.now()
    Age=current_Age-Valid_Age()
    # Calculate the number of years, months, days, hours, minutes, and seconds
    years = Age.days // 365
    months = (Age.days % 365) // 30
    days = (Age.days % 365) % 30
    hours = Age.seconds // 3600
    minutes = (Age.seconds // 60) % 60
    seconds = Age.seconds % 60

    print(f"\n{'~'*15}...Calculated Details... {'~'*15}")
    print(f'\n"Your Are" : {years} "Years", {months} "Months", {days} "Days", {hours} "Hours, {minutes} "Minutes", {seconds} Seconds Old\n\n')


def Valid_Age():
    while True:
        try:
            print(f"\n{'~'*15} Date Of Birth {'~'*15}")
            date = int(input("\nEnter Birth Date (DD) : "))
            month = int(input("\nEnter Birth Month (MM) : "))
            year = int(input("\nEnter Birth Year (YYYY) : "))

            DOB = datetime(year, month, date)
            return DOB
        except:
            print("\n--> Invalid Date of Birth")


age=Calculate_Age()

