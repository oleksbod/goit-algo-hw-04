import timeit
import random

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def timsort(array):
    return sorted(array)

def generate_array(data_type, size):
    if data_type == "random":
        return random.sample(range(size), size)
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size))[::-1]
    else:
        raise ValueError(f"Невідомий тип даних: {data_type}")

def main(size = 10):
    print(f"**Кількість: {size}")
    for data_type in ["random", "sorted", "reversed"]:
        array = generate_array(data_type, size)

        print(f"**Дані:** {data_type}")
        for algorithm in ["merge_sort", "insertion_sort", "timsort"]:
            time = timeit.timeit(lambda: globals()[algorithm](array.copy()), number=1)
            print(f"  {algorithm}: {time:.6f} сек")

        print()

if __name__ == "__main__":
    main(100)
    main(1000)
    main(10000)