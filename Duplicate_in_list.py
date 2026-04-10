n = [545,56,54,564,564,654,65,45,454,5,45,4]
result = []

for num in n:
    if num not in result:
        result.append(num)

print(result)

n = [545,56,54,564,564,654,65,45,454,5,45,4]

result = []
seen = set()

for num in n:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(result)
