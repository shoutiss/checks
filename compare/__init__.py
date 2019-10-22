
import check50
import check50.c

@check50.check()
def exists():
    """compare.c exists"""
    check50.exists("compare.c")

@check50.check(exists)
def compiles():
    """compare.c compiles"""
    check50.c.compile("compare.c", lcs50=True)

@check50.check(compiles)
def compare_8():
    """Compares 8! to 10^8"""
    check50.run("./compare").stdin("8").stdout("10^8 is larger.").exit(0)

@check50.check(compiles)
def compare_12():
    """Compares 12! to 10^12"""
    check50.run("./compare").stdin("12").stdout("12! is larger.").exit(0)