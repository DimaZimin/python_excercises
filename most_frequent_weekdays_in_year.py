#FROM CODEWARS:
#What is your favourite day of the week? Check if it's the most frequent day of the week in the year.
#You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. 
#The result has to be a list of days sorted by the order of days in week 
#(e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.
#Input: Year as an int.
#Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

def most_frequent_days(year):
    return [day_name[day] for day in sorted( {weekday(year, 1, 1), weekday(year, 12, 31)} ) ]
