from check50 import *

class Triangle(Checks):

    @check()
    def exists(self):
        """triangle.c exists"""
        self.require("triangle.c")

    @check("exists")
    def compiles(self):
        """triangle.c compiles"""
        self.spawn("clang -o triangle triangle.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_3_4_5(self):
        """input of 3, 4, 5 yields output of YES\n"""
        self.spawn("./triangle").stdin("3").stdin("4").stdin("5").stdout("YES\n", "YES\n").exit(0)

    @check("compiles")
    def test_3_4_10(self):
        """input of 28 yields output of  28\n YES\n"""
        self.spawn("./triangle").stdin("3").stdin("4").stdin("10").stdout("NO\n", "NO\n").exit(0)

