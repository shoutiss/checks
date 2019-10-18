
import check50
import check50.c

@check50.check()
def exists():
    """sigma.c exists"""
    check50.exists("sigma.c")

@check50.check()
def compiles():
    """sigma.c compiles"""
    check50.c.compile("sigma.c", lcs50=True)

@check50.check(compiles)
def sums_1_5():
    """finds the sum of 1, 2, 3 inclusive" """
    check50.run("./sigma 1 2 3").stdout("6\n").exit(0)

@check50.check(compiles)
def sum_10_15_20(self):
    """Finds the sum of 10, 15, and 20"""
    check50.run("./sigma 10 15 20").stdout("45\n").exit(0)

@check50.check(compiles)
def sum_neg4_neg3_neg2_(self):
    """Finds the sum of -4, -3, -2"""
    check50.run("./sigma -4 -3 -2").stdout("-9\n").exit(0)

@check50.check(compiles)
def rejects_no_commands(self):
    """Rejects lack of command line"""
    check50.run("./sigma").exit(1)