

randomList = [1, 'a', 2, 'b', 3]
result = 0
for entry in randomList:
    try:
        result += int(entry)
    except ValueError:
        print("A ValueError occured.")
print(f"The sum is: {result}")