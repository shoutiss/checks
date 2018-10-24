import check50
import check50.c

@check50.check()
def exists():
    """triangle.c exists"""
    check50.exists("triangle.c")

@check50.check(exists)
def compiles():
    """triangle.c compiles"""
    check50.c.compile("triangle.c", lcs50=True)

@check50.check(compiles)
def test_3_4_5():
    """3, 4, 5 yields YES\n"""
    check50.run("./triangle").stdin("3").stdin("4").stdin("5").stdout("YES\n", regex=False).exit(0)

@check50.check(compiles)
def test_3_4_10():
    """3, 4, 10 yields NO\n"""
    check50.run("./triangle").stdin("3").stdin("4").stdin("10").stdout("NO\n", regex=False).exit(0)

@check50.check(compiles)
def test_neg3_4_5():
    """-3, 4, 5 yields NO\n"""
    check50.run("./triangle").stdin("-3").stdin("4").stdin("5").stdout("NO\n", regex=False).exit(0)

@check50.check(compiles)
def test_reject_nonintegers():
    """rejects non-integer values"""
    check50.run("./triangle").stdin("3.5").reject().stdin("2.7").reject().stdin("-0.5").reject()

@check50.check(compiles)
def test_reject_foo_days():
    """rejects inputs == "foo" """
    check50.run("./triangle").stdin("foo").reject().stdin("foo").reject().stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty_string_days():
    """rejects a non-numeric input of "" for sides """
    check50.run("./triangle").stdin("").reject()
