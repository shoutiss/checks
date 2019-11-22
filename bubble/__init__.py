import check50
import check50.c

@check50.check()
def exists():
    """bubble.c exists."""
    check50.exists("bubble.c")

@check50.check(exists)
def compiles():
    """bubble.c compiles."""
    check50.include("bubble.h", "sort.c")
    check50.c.compile("sort.c", "bubble.c", lcs50=True)

def test_sorted(items):
    p = check50.run("./sort")
    for i in items:
        p.stdin(str(i))
    p.stdin(check50.EOF)

    # Attempting to check sort steps
    steps = []
    n = len(items)
    for i in range(n):
        no_swaps = True
        for j in range(n - i - 1):
            if (items[j] > items[j + 1]):
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
                no_swaps = False
        steps.append(items.copy())
        if no_swaps:
            break


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