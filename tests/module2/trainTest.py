import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

# TODO: Add test to check for correct times, using Excel workbook values
@t.test(0)
def containsTrain1(test):
    print(lib.getLine(lib.outputOf(_fileName), 0).lower())
    test.test = lambda : assertlib.contains(lib.getLine(lib.outputOf(_fileName), 0).lower(), "minutes") and assertlib.contains(
		lib.getLine(lib.outputOf(_fileName), 0), "?")
    test.description = lambda : "Could not ascertain whether you asked how many minutes it would take to get to the station"
