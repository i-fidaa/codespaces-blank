year = int(input("Year: "))
month = input("Month: ").lower()
day = int(input("Day: "))

century = year // 100
#cycle = [2, 0, 5, 3]
try:
    if century % 4 == 0:
        c_doomsday = 2
    elif (century % 4) - 1 == 0:
        c_doomsday = 0
    elif (century % 4) - 2 == 0:
        c_doomsday = 5
    elif (century % 4) - 3 == 0:
        c_doomsday = 3
except ZeroDivisionError:
    c_doomsday = 2

year_diff = year - century*100
leap_years = year_diff // 4
y_doomsday = (c_doomsday + year_diff + leap_years) % 7

#months = { ("january", "1") : 

'''match month:
    case "january" | "1":
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            answer = ((day - 4) + y_doomsday) % 7
        else:
            answer = ((day - 3) + y_doomsday) % 7
    case "february" | "2":
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            answer = ((day - 29) + y_doomsday) % 7
        else:
            answer = ((day - 28) + y_doomsday) % 7
    case "march" | "3":
        answer = ((day - 14) + y_doomsday) % 7
    case "april" | "4":
        answer = ((day - 4) + y_doomsday) % 7
    case "may" | "5":
        answer = ((day - 9) + y_doomsday) % 7
    case "june" | "6":
        answer = ((day - 6) + y_doomsday) % 7
    case "july" | "7":
        answer = ((day - 11) + y_doomsday) % 7
    case "august" | "8":
        answer = ((day - 8) + y_doomsday) % 7
    case "september" | "9":
        answer = ((day - 5) + y_doomsday) % 7
    case "october" | "10":
        answer = ((day - 10) + y_doomsday) % 7
    case "november" | "11":
        answer = ((day - 7) + y_doomsday) % 7
    case "december" | "12":
        answer = ((day - 12) + y_doomsday) % 7'''

match month:
    case "january" | "1":
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            m_doomsday = 4
        else:
            m_doomsday = 3
    case "february" | "2":
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            m_doomsday = 29
        else:
            m_doomsday = 28
    case "march" | "3":
        m_doomsday = 14
    case "april" | "4":
        m_doomsday = 4
    case "may" | "5":
        m_doomsday = 9
    case "june" | "6":
        m_doomsday = 6
    case "july" | "7":
        m_doomsday = 11
    case "august" | "8":
        m_doomsday = 8
    case "september" | "9":
        m_doomsday = 5
    case "october" | "10":
        m_doomsday = 10
    case "november" | "11":
        m_doomsday = 7
    case "december" | "12":
        m_doomsday = 12

answer = ( day - m_doomsday + y_doomsday) % 7

weekdays = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

#weekdays_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(weekdays[answer])