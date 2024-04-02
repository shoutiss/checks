import check50
import check50.c

@check50.check()
def exists():
    """create.c exists"""
    check50.exists("create.c")

@check50.check()
def exisits():
    """create.py exists"""
    check50.exists("create.py")
