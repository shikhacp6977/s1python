start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))
for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)