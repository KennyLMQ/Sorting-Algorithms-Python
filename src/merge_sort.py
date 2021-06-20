import logging
import math


def merge_sort(numbers):
    sort(numbers, 0, len(numbers) - 1)


def sort(numbers, left, right):
    if (left < right):
        middle = left + math.floor((right - left) / 2)

        sort(numbers, left, middle)
        sort(numbers, middle + 1, right)
        merge(numbers, left, middle, right)


def merge(numbers, left, middle, right):
    leftNumbers = numbers[left:middle + 1]
    rightNumbers = numbers[middle + 1:right + 1]

    logging.debug(f"{leftNumbers}, {rightNumbers}")

    leftLen = len(leftNumbers)
    rightLen = len(rightNumbers)

    leftIndex = 0
    rightIndex = 0
    numbersIndex = left

    while leftIndex < leftLen and rightIndex < rightLen:
        if leftNumbers[leftIndex] < rightNumbers[rightIndex]:
            numbers[numbersIndex] = leftNumbers[leftIndex]
            numbersIndex += 1
            leftIndex += 1
        else:
            numbers[numbersIndex] = rightNumbers[rightIndex]
            numbersIndex += 1
            rightIndex += 1

    while leftIndex < leftLen:
        numbers[numbersIndex] = leftNumbers[leftIndex]
        numbersIndex += 1
        leftIndex += 1

    while rightIndex < rightLen:
        numbers[numbersIndex] = rightNumbers[rightIndex]
        numbersIndex += 1
        rightIndex += 1


def main():
    logging.basicConfig(level=logging.INFO)

    numbers = [1234, 51, -6163216, 56161, 135, 1, -351, 616, 99]
    logging.info(f"Before Merge Sort: {numbers}")

    merge_sort(numbers)

    logging.info(f"After Merge Sort:  {numbers}")


if __name__ == "__main__":
    main()