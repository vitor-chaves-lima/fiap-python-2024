import time

count: int = 10

while count > 0:
    print(count)
    count -= 1
    time.sleep(1)
    
print("Fogo!")