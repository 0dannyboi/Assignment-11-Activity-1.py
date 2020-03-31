# This program takes a user input of year and month numbers of that year to calcuate number of days in each month based on presence of leap years.
def get_year():
  print("Please enter a year:")
  year = int(input())
  return year 


def leap_year(year):
  if (year % 4 == 0 and year % 100 != 0): 
    return True 
  elif (year % 400 == 0):
    return True 
  else: 
    return False


def get_month(): 
  print("Please enter month number.") 
  month = int(input()) 
  return month
  
  
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] 


leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 


regular_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def process(result, year):
  month = get_month() 
  while (month > 0 and month < 13): 
    if (result == True): 
      print(month_names[month - 1] + " " + str(year) + " has " + str(leap_month_days[month - 1]) + " days.") 
    else:
      print(month_names[month - 1] + " " + str(year) + " has " + str(regular_month_days[month - 1]) + " days.")
    month = get_month()


def main(): 
  year = get_year()
  result = leap_year(year) 
  process(result, year)


main()
