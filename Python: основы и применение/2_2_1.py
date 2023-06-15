from datetime import date, timedelta

date = date(*list(map(int, input().split())))
days = timedelta(days=int(input()))
result = date + days

print(result.year, result.month, result.day)