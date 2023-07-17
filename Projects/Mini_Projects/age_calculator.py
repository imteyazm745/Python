def ageCalculator(y, m, d):
    import datetime
    today = datetime.date.today()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days/365.25)
    return age

myage = ageCalculator(2000, 6, 7)
print(myage)