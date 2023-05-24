
import check50
import check50.c

@check50.check()
def exists():
    """product.c exists"""
    check50.exists("product.c")

@check50.check(exists)
def compiles():
    """product.c compiles"""
    check50.c.compile("product.c", lcs50=True)

@check50.check(compiles)
def largest():
    """Calculate correct largest product"""
    check50.run("./product").stdout("70600674\n").exit(0)
