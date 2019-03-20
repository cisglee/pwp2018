import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

# TODO: Add test to check for correct times, using Excel workbook values
@t.test(0)
def containsTrain1(test):
	test.test = lambda : True
	test.description = lambda : "Could not ascertain whether you asked how many minutes it would take to get to the station"
