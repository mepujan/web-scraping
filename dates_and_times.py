from datetime import date
now = date.today()
print(now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d of %B"))

dob = date(1997,9,7)
age = now-dob
print(f'My age is {age.days}')