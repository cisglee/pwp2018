import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def exactChange0(test):
	test.test = lambda : assertlib.numberOnLine(0, lib.getLine(lib.outputOf(_fileName, [0]), 0))
	test.description = lambda : "0$ in change equals 0 coins"

@t.test(1)
def exactChange41(test):
	test.test = lambda : assertlib.numberOnLine(4, lib.getLine(lib.outputOf(_fileName, [0.41]), 0))
	test.description = lambda : "0.41$ in change equals 4 coins"

@t.test(2)
def exactChange9999(test):
	test.test = lambda : assertlib.numberOnLine(39996, lib.getLine(lib.outputOf(_fileName, [9999]), 0))
	test.description = lambda : "9999$ in change equals 39996 coins"

@t.test(3)
def exactChange402(test):
	test.test = lambda : assertlib.numberOnLine(18, lib.getLine(lib.outputOf(_fileName, [4.02]), 0))
	test.description = lambda : "4.02$ in change equals 18 coins"

@t.test(4)
def exactChange35(test):
	test.test = lambda : assertlib.numberOnLine(2, lib.getLine(lib.outputOf(_fileName, [0.35]), 0))
	test.description = lambda : "0.35$ in change equals 2 coins"

@t.test(10)
def handlesWrongInput(test):
	test.test = lambda : assertlib.numberOnLine(0, lib.getLine(lib.outputOf(_fileName, [-9.50, -327, 0]), 0))
	test.description = lambda : "is able to deal with the following erroneous input: -9.50 and -327"