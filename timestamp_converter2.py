timestamp = 87426

seconds = timestamp % 60
minutes = timestamp // 60 % 60
hours = timestamp // 3600 % 60 % 60
days = hours // 24

print(seconds)
print(minutes)
print(hours)
print(days)