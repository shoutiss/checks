from check50 import *


class sigma(Checks):

    @check()
    def exists(self):
        """sigma.c exists."""
        self.require("sigma.c")

    @check("exists")
    def compiles(self):
        """sigma.c compiles."""
        self.spawn("clang -std=c11 -o sigma sigma.c -lcs50 -lm").exit(0)

    @check("compiles")
    def sum_1_2_3(self):
        """Finds the sum of 1, 2, and 3"""
        self.spawn("./sigma 1 2 3").stdout("6\n").exit(0)

    @check("compiles")
    def sum_10_15_20(self):
        """Finds the sum of 10, 15, and 20"""
        self.spawn("./sigma 10 15 20").stdout("45\n").exit(0)

    @check("compiles")
    def sum_neg4_neg3_neg2_(self):
        """Finds the sum of -4, -3, -2"""
        self.spawn("./sigma -4, -3, -2").stdout("-9\n").exit(0)

    @check("compiles")
    def rejects_no_commands(self):
        """Rejects lack of command line"""
        self.spawn("./sigma").exit(1)

