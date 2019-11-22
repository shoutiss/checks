import check50
import check50.c

@check50.check()
def exists():
    """selection.c exists."""
    check50.exists("selection.c")

@check50.check(exists)
def compiles():
    """selection.c compiles."""
    check50.include("selection.h", "sort.c")
    check50.c.compile("sort.c", "selection.c", lcs50=True)

def test_sorted(items):
    p = check50.run("./sort")
    for i in items:
        p.stdin(str(i))
    p.stdin(check50.EOF)

    # Check sort steps
    steps = []
    n = len(items)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if (items[j] < items[min_index]):
                min_index = j
        if (i != min_index):
            temp = items[i]
            items[i] = items[min_index]
            items[min_index] = temp
        steps.append(items.copy())


    for step in steps:
        p.stdout(" ".join(str(item) for item in step))

    p.exit(0)

@check50.check(compiles)
def sort_reversed():
    """sorts {5,4,3,2,1}"""
    test_sorted([5, 4, 3, 2, 1])

@check50.check(compiles)
def sort_shuffled():
    """sorts {5,3,1,2,4,6}"""
    test_sorted([5, 3, 1, 2, 4, 6])

@check50.check(compiles)
def sort_sorted():
    """ Recognizes an already sorted array"""
    test_sorted([1, 2, 3, 4, 5])