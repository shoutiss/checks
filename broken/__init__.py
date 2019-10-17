import check50
import check50.c

@check50.check()
def compiles():
    """broken.c compiles"""
    check50.c.compile("broken.c")

@check50.check(compiles)
def sums_1_5():
    """finds the sum of 1 through 5 inclusive" """
    check50.run("./broken").stdin(1).stdin(5).stdout("Sum: 15\n").exit(0)
