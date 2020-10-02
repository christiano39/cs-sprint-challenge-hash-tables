#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    d = {}

    for t in tickets:
        d[t.source] = t.destination

    route = [d["NONE"]]
    for i in range(length - 1):
        route.append(d[route[i]])

    return route
