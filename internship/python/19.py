def day(week):
    match week:
        case 1:
            return("sunday")
        case 2:
            return("monday")
        case 3:
            return("tuesday")
        case 4:
            return("wednsday")
        case 5:
            return("thursday")
        case 6:
            return("friday")
        case 7:
            return("saturday")
        case 8:
            return("invalid")
print(day(int(input("enter the no"))))