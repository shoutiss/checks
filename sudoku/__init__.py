import check50
import check50.c

@check50.check()
def exists():
    """sudoku.c exists."""
    check50.exists("sudoku.c")

@check50.check(exists)
def compiles():
    """sudoku.c compiles."""
    check50.include("sudoku.h")
    check50.c.compile("sudoku.c", lcs50=True)