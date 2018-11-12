import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def showsGraph(test):
	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "savefig")
	test.description = lambda : "stores a graph"

@t.test(1)
def exactZeroPoint(test):
	test.test = lambda : assertlib.numberOnLine(0.37, lib.getLine(lib.outputOf(_fileName), stdinArgs=[0]), deviation = 0.01)\
				     and assertlib.numberOnLine(0.69, lib.getLine(lib.outputOf(_fileName), stdinArgs=[0]), deviation = 0.01)
	test.description = lambda : "prints the intersects of the axes (x = 0.37 and y = 0.69)"
