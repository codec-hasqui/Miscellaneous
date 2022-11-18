import os

# Clearing the shell
os.system('cls')

print("=================================================")
print("=                                               =")
print("=       Zodiac Sign finder & Horoscope          =")
print("=                                               =")
print("=================================================")
print("                                                 ")
day = int(input("What is your birth day?(1-31): "))
month = input("Which month were you born in(e.g. april, july etc): ")
if month == 'december':
	sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
	sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
	sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
	sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
	sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
	sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
	sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
	sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :",sign)
horoscope = input("Whould you like to get your Horoscope for today?(yes/no)")
if horoscope == 'yes':
    print(" you will have a wonderful day")
