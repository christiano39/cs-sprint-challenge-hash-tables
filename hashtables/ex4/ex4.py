def has_negatives(a):
    """
    YOUR CODE HERE
    """
    d = {}

    for num in a:
        if abs(num) in d:
            d[abs(num)] += 1
        else:
            d[abs(num)] = 1

    result = []

    for num in d:
        if d[num] == 2:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
