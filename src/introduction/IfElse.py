# problem https://www.hackerrank.com/challenges/py-if-else?h_r=next-challenge&h_v=zen

n = int(input())
if n % 2 != 0:
    print('Weird Odd')
elif 2 <= n <= 5:
    print('Not Weird')
elif 6 <= n <= 20:
    print('Weird')
else:
    print('Not Weird')
