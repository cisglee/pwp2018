import checkpy.tests as t
import checkpy.lib as lib
import re


@t.test(0)
def containsTrain0(test):
    def containsCheck():
        output = lib.outputOf(test.fileName, stdinArgs=[22, 15])
        time = re.search("\d{1,2}:\d{2}", output)
        if time is None:
            return False
        else:
            return True

    test.test = containsCheck
    test.description = lambda: "Checking whether you provided the time"

@t.test(1)
def containsTrain1(test):
    def containsCheck():
        output = lib.outputOf(test.fileName, stdinArgs=[22, 15])
        time = re.search("(10a|11a|13a|14a|15a|15b)", output)
        if time is None:
            return False
        else:
            return True

    test.test = containsCheck
    test.description = lambda: "Checking whether you provide the track number"

#@t.test(2)
#def containsPeak18_22(test):
#    def containsCheck():
#        output = lib.outputOf(test.fileName, stdinArgs=[18, 12])
#        if "peak" in output or "rush" in output:
#            return True
#        else:
#            return False
#
#    test.test = containsCheck
#    test.description = lambda: "Checking whether you mentioned peak hours"
