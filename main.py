import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
    return arr


def main():
    data_sizes = [1000, 10000, 100000]
    for size in data_sizes:
        data = [random.randint(0, 1000000) for _ in range(size)]
        print(f"Data size: {size}")

        merge_sort_time = timeit.timeit(
            lambda: merge_sort(data.copy()), number=1)
        print(f"Merge Sort Time: {merge_sort_time}")

        insertion_sort_time = timeit.timeit(
            lambda: insertion_sort(data.copy()), number=1)
        print(f"Insertion Sort Time: {insertion_sort_time}")

        timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)
        print(f"Timsort Time: {timsort_time}")

        print("-" * 50)
    print("Conclusion: use Timsort. It's the fastest due to the fact that it uses hybrid sorting algorithm (merge sort and insertion sort). Also, it's stable. It has been tested and adapted during it's lifetime.")


if __name__ == "__main__":
    main()
