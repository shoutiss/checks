
import check50
import check50.c

@check50.check()
def exists():
    """twinprime.c exists"""
    check50.exists("twinprime.c")

@check50.check(exists)
def compiles():
    """twinprime.c compiles"""
    check50.c.compile("twinprime.c", lcs50=True)

@check50.check(compiles)
def find_primes():
    """Finds the twin primes below 100."""
    check50.run("./twinprime").stdout("3, 5\n5, 7\n11, 13\n17, 19\n29, 31\n41, 43\n59, 61\n71, 73").exit(0)