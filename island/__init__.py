import check50
import check50.c

@check50.check()
def exists():
    """island.c exists."""
    check50.include("island.h", "testing.c", "Makefile")
    check50.exists("island.c")

@check50.check(exists)
def compiles():
    """island.c compiles."""
    check50.run("make").exit(0)

@check50.check(compiles)
def island_x():
    """Test Island X"""
    check50.run("./testing 0").stdout("24")

@check50.check(compiles)
def island_y():
    """Test Island Y"""
    check50.run("./testing 1").stdout("28")

@check50.check(compiles)
def island_z():
    """Test Island Z"""
    check50.run("./testing 2").stdout("18")

@check50.check(compiles)
def island_w():
    """Test Island W"""
    check50.run("./testing 3").stdout("36")

# @check50.check(compiles)
# def island_t():
#     """Indexing out of bounds?"""
#     check50.run("./testing 4").stdout("20")