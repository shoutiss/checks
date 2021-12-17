import check50
import check50.c

@check50.check()
def exists():
    """fifteenext.c exists."""
    check50.exists("fifteenext.c")

@check50.check(exists)
def compiles():
    """fifteenext.c compiles."""
    check50.c.compile("fifteenext.c", lcs50=True)

def test_solvable(size):
    out = check50.run("./fifteenext " + size).stdout()
    print(out)



@check50.check(compiles)
def test_3x3():
    """Solvable 3x3?"""
    print(test_solvable('3'))

# @check50.check(compiles)
# def sort_shuffled():
#     """sorts {5,3,1,2,4,6}"""
#     test_sorted([5, 3, 1, 2, 4, 6])

# @check50.check(compiles)
# def sort_sorted():
#     """ Recognizes an already sorted array"""
#     test_sorted([1, 2, 3, 4, 5])