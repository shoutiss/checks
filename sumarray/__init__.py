
import check50
import check50.c

@check50.check()
def exists():
    """sumarray.c exists"""
    check50.exists("sumarray.c")

@check50.check(exists)
def compiles():
    """sumarray.c compiles"""
    check50.c.compile("sumarray.c", lcs50=True)

@check50.check(compiles)
def sum_arrays():
    """Calculates the sum of the arrays"""
    check50.run("./sumarray").stdout("Array 1: 15  Array 2: 30\n").exit(0)