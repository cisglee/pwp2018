import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def exactWater0(test):
	test.test = lambda : assertlib.numberOnLine(0, lib.getLine(lib.outputOf(_fileName, stdinArgs=[0]), 0))
	test.description = lambda : "0 minutes equals 0 water bottles"

@t.test(1)
def exactWater10(test):
	test.test = lambda : assertlib.numberOnLine(120, lib.getLine(lib.outputOf(_fileName, stdinArgs=[10]), 0))
	test.description = lambda : "10 minutes equals 120 water bottles"

@t.test(2)
def exactWater327(test):
	test.test = lambda : assertlib.numberOnLine(3924, lib.getLine(lib.outputOf(_fileName, stdinArgs=[327]), 0))
	test.description = lambda : "327 minutes equals 3924 water bottles"
