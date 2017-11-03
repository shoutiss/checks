from check50 import *

class Perfect(Checks):
    
    @check()
    def exists(self):
        """perfect.c exists"""
        self.require("perfect.c")

    @check("exists")
    def compiles(self):
        """perfect.c compiles"""
        self.spawn("clang -o perfect perfect.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_6(self):
        """input of 6 yields output of  6\n YES\n"""
        self.spawn("./perfect").stdin("6").stdout("6\nYES\n", "6\nYES\n").exit(0)
          
    @check("compiles")
    def test_28(self):
        """input of 28 yields output of  28\n YES\n"""
        self.spawn("./perfect").stdin("28").stdout("28\nYES\n", "28\nYES\n").exit(0)
