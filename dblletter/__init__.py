
import check50
import check50.c

@check50.check()
def exists():
    """dblletter.c exists"""
    check50.exists("dblletter.c")

@check50.check(exists)
def compiles():
    """dblletter.c compiles"""
    check50.c.compile("dblletter.c", lcs50=True)

@check50.check(compiles)
def sum_arrays():
    """Tests Halloween"""
    check50.run("./dblletter").stdin("Halloween").stdout("Halowen\n").exit(0)