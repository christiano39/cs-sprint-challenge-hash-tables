def intersection(arrays):
    """
    YOUR CODE HERE
    """
    d = {}

    for arr in arrays:
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

    result = []

    for num in d:
        if d[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
