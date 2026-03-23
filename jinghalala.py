numbers=[10,20,30,40,50,60,70]


print(f'Original list: {numbers}')

numbers.append(6)
numbers.remove(20)
numbers_length = len(numbers)
max_num = max(numbers)
min_num = min(numbers)
reversed_list = list(reversed(numbers))

print(numbers)
print(numbers_length)
print(max_num)
print(min_num)
print(f'Reversed list: {reversed_list}')
for i in range (len(numbers)):
    print(f'Element at index {i}: {numbers[i]}')

