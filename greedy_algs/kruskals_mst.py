
# Find operation on Disjoint Set


# Finds the representative of the set
# that i is an element of

parent: list[int] = []


def find(i):

    # if i is the parent of itself
    if parent[i] == i:

        # then i is the representative
        # of its set
        return i

    else:
        # Else if i is not the parent of
        # itself, then i is not the
        # representative of his set. So we
        # recursively call Find on its parent
        return find(parent[i])
