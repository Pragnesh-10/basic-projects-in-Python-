from datetime import date
def age_calculator(birth_year,birth_month,birth_date):
  today = date.today()
  age = today.year-birth_year
  if (today.month,today.day) < (birth_month,birth_year):
    age -= 1
  return age
birth_year = int(input("enter the year"))
birth_month = int(input("enter month"))
birth_date = int(input("emter date"))
print(age_calculator(birth_year,birth_month,birth_date))
