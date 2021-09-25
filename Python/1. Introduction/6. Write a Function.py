#Write a Function

def is_leap(year):
    
    leap = False
    # Write your logic here
    if  (year%4==0):
        if year%400==100 or year%400==200 or year%400==300:
            leap = False
        else:
            leap = True

    return leap
