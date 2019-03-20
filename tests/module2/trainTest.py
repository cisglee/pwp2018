import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

# TODO: Add test to check for correct times, using Excel workbook values
@t.test(0)
def containsOneQuestion(test):
	test.test = lambda : assertlib.contains(lib.getLine(lib.outputOf(_fileName), 0), "minutes") and assertlib.contains(
		lib.getLine(lib.outputOf(_fileName), 0), "?")
	test.description = lambda : "Could not ascertain whether you asked how many minutes it would take to get to the station"


@t.test(1)
def containsTwoQuestions(test):
	test.test = lambda: assertlib.contains(lib.getLine(lib.outputOf(_fileName), 0), "minutes") and assertlib.contains(
		lib.getLine(lib.outputOf(_fileName), 0), "?")
	test.description = lambda : "Could not ascertain whether you asked how many minutes it would take to get from the station to the destination"

# TODO: Check how arguments for separate questions can be provided
@t.test(2)
def containsPeak(test):
	def containsCheck():
		if assertlib.contains(lib.getLine(lib.outputOf(_fileName), [18, 12]).lower(), "peak"):  # Possibly provides all arguments at once, instead of waiting for the second question
			return True
		elif assertlib.contains(lib.getLine(lib.outputOf(_fileName), [18, 12]).lower(), "rush"):
			return True
		else:
			return False
	test.test = containsCheck
	test.description = lambda : "Could not find any mention of off-peak or peak hours"
