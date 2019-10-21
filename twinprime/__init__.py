
import check50
import check50.c

@check50.check()
def exists():
    """twinprime.c exists"""
    check50.exists("twinprime.c")

@check50.check()
def compiles(exists):
    """twinprime.c compiles"""
    check50.c.compile("twinprime.c", lcs50=True)

@check50.check(compiles)
def find_primes:
    """Finds the twin primes below 100."""
    check50.run("./twinprime").stdout("3, 5\n").exit(0)
