def code(numbers):
    result = []
    for i in range(1, numbers + 1):
        for j in range(i + 1, numbers + 1):
            sum_ = i + j
            if numbers % sum_ == 0:
                result.append(i)
                result.append(j)
    return result
numbers = int(input('Введите число от 3 до 20:'))
result = code(numbers)
print(*result, sep='')