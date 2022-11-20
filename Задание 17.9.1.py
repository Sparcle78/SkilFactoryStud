array = list(map(int, input('Введите числа через пробел: ').split()))
print(array)

while True:
    element = int(input('Введите число в рамках последовательности: '))
    if element not in range(min(array) + 1, max(array)):
        print('Некорректное число')
    else:
        break

array.append(element)

def sortirovka(array):
    for i in range(len(array)):  
        idx_min = i  
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:  
            array[i], array[idx_min] = array[idx_min], array[i]
    return array

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

a = (binary_search(sortirovka(array), element, 0, len(array) - 1))
print('Позиция элемента, который меньше введенного вами числа: ', a+1)
# а+1 - нумерация индексов в массиве начинается с единицы
print(array)