def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    d = {}
    for i in range(length):
        d[weights[i]] = i

    for i in range(length):
        if (limit - weights[i]) in d:
            return (d[limit - weights[i]], i)

    return None
