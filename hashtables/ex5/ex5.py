# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    d = {}

    for f in files:
        filename = f.split('/')[-1]
        if filename in d:
            d[filename].append(f)
        else:
            d[filename] = [f]

    result = []

    for q in queries:
        if q in d:
            result += d[q]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
