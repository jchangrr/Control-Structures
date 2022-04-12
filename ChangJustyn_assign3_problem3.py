date = int(input("Enter a date in YYYYMMDD format (i.e. 20200128 for January 28th, 2020): "))
if date == 20200903 or date == 20200908 or date == 20200910 or date == 20200915 or date == 20200917 or date == 20200922 or date == 20200924 or date == 20200929 or date == 20201001 or date == 20201006 or date == 20201008 or date == 20201013 or date == 20201015 or date == 20201020 or date == 20201022 or date == 20201027 or date == 20201029 or date == 20201103 or date == 20201105 or date == 20201110 or date == 20201112 or date == 20201117 or date == 20201119 or date == 20201124 or date == 20201201 or date == 20201203 or date == 20201208 or date == 20201210:
    print("You have class today")
elif date % 100000 > 228 and date % 100000 < 301:
    print("That's not a valid date!")
elif date % 100000 > 131 and date % 100000 < 201:
    print("That's not a valid date!")
elif date % 100000 > 331 and date % 100000 < 401:
    print("That's not a valid date!")
elif date % 100000 > 430 and date % 100000 < 501:
    print("That's not a valid date!")
elif date % 100000 > 531 and date % 100000 < 601:
    print("That's not a valid date!")
elif date % 100000 > 630 and date % 100000 < 701:
    print("That's not a valid date!")
elif date % 100000 > 731 and date % 100000 < 801:
    print("That's not a valid date!")
elif date % 100000 > 831 and date % 100000 < 901:
    print("That's not a valid date!")
elif date % 100000 > 930 and date % 100000 < 1001:
    print("That's not a valid date!")
elif date % 100000 > 1031 and date % 100000 < 1101:
    print("That's not a valid date!")
elif date % 100000 > 1130 and date % 100000 < 1201:
    print("That's not a valid date!")
elif date % 100000 > 1231 and date % 100000 < 101:
    print("That's not a valid date!")
elif date < 20200902:
    print("This date is before the semester begins")
elif date > 20201221:
    print("This date is after the semester ends")
elif date > 20200902 and date < 20201221:
    if date != 20200903 or date != 20200908 or date != 20200910 or date != 20200915 or date != 20200917 or date != 20200922 or date != 20200924 or date != 20200929 or date != 20201001 or date != 20201006 or date != 20201008 or date != 20201013 or date != 20201015 or date != 20201020 or date != 20201022 or date != 20201027 or date != 20201029 or date != 20201103 or date != 20201105 or date != 20201110 or date != 20201112 or date != 20201117 or date != 20201119 or date != 20201124 or date != 20201201 or date != 20201203 or date != 20201208 or date != 20201210:
        print("You don't have class today")
