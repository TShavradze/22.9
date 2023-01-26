array = input("Введите числа через пробел:").split()
array_list = list(map(int, array))

print(type(array_list))

array_list.sort()
print(f'Отсортированный по возрастанию список: {array_list}')

element = int(input('Введите число в рамках последовательности: '))

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

array = [i for i in range(1, 10)]

print(binary_search(array, element, 0, 9))


