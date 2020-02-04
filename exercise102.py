import datetime
#Today date
# today_date = datetime.now().strftime("%d/%m/%Y")

name = "Hamza"
year_now = 2020
age_calc = int(input(f"Hello {name}, how old did you say you were?"))
year_born = year_now - age_calc
print(f"You said you were {age_calc} hence you were born in {year_born}")