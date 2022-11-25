print ("Current Year is")
import datetime
today = datetime.date.today()
year = today.year
print(year)
print ("Enter Last Year")
endYear = int(input())
print ("List of Leap Years")
for year in range(year, endYear):
  if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
    print (year)
