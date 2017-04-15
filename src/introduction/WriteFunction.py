# problem https://www.hackerrank.com/challenges/write-a-function?h_r=next-challenge&h_v=zen


def is_leap(year):
    if year % 4 != 0:
        leap = False

    elif year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True

    return leap

year = int(input())
print(is_leap(year))
print(year)