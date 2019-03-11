from random import randint, choice


def create_unsorted_array(array_size=10, min_element=0, max_element=100):
    return randint(low=min_element, high=max_element, size=array_size)


def bubble_sort(array):
    counter = 0
    for i in range(len(array)):
        replaced = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                counter += 1
                replaced = True
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        if not replaced:
            break
    return array, counter


def insertion_sort(s):
    counter = 0
    for i in range(0, len(s)-1):
        val = s[i+1]
        j = i
        while (j >= 0) and (s[j] > val):
            counter += 1
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = val
    return s, counter


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    else:
        middle = int(len(array)/2)
        a = merge_sort(array[:middle])
        b = merge_sort(array[middle:])
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] < b[0]:
                c.append(a[0])
                a.remove(a[0])
            else:
                c.append(b[0])
                b.remove(b[0])
        if len(a) == 0:
            c.extend(b)
        else:
            c.extend(a)
        return c


def selection_sort(array):
    for i in range(len(array)-1):
        min_element = array[i]
        min_position = i
        changing = False
        for j in range(i+1, len(array)):
            if array[j] < min_element:
                changing = True
                min_element = array[j]
                min_position = j
        if changing:
            temp = array[min_position]
            array[min_position] = array[i]
            array[i] = temp
    return array


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        num_for_comparing = choice(array)
        left_array, middle_array, right_array = [], [], []
        for element in array:
            if element < num_for_comparing:
                left_array.append(element)
            elif element == num_for_comparing:
                middle_array.append(element)
            else:
                right_array.append(element)
        return quick_sort(left_array) + middle_array + quick_sort(right_array)


def binary_search(array, number=None):
    if len(array) == 0 or (number is None):
        return False
    min_position = 0
    max_position = len(array)-1
    middle_position = int((len(array)-1)/2)

    while True:
        if array[middle_position] == number:
            return middle_position
        elif array[middle_position] < number:
            min_position = middle_position
            middle_position = int((max_position-min_position)/2)
            if middle_position-min_position == 1 and array[min_position+1] != number:
                return False
        else:
            max_position = middle_position
            middle_position = int((max_position-min_position)/2)
            if max_position-middle_position == 1 and array[max_position-1] != number:
                return False


if __name__ == "__main__":
    unsorted_array = [48, 17, 65, 13, 8, 48, 59, 63, 98, 40]
    reversed_sorted_array = list(reversed(bubble_sort(unsorted_array.copy())[0]))
    print(bubble_sort(unsorted_array.copy()))
    print(bubble_sort(reversed_sorted_array.copy()))
    print(merge_sort(reversed_sorted_array.copy()))
    print(insertion_sort(unsorted_array.copy()))
