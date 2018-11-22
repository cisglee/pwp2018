import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def has_exact_matches(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "exact_matches")
    test.description = lambda : "defines the function exact_matches"

@t.passed(has_exact_matches)
@t.test(1)
def is_list_exact_matches(test):
    test.test = lambda : assertlib.sameType(lib.getFunction("exact_matches", _fileName)("a", "a"), [])
    test.description = lambda : "exact_matches returns a list"

@t.passed(is_list_exact_matches)
@t.test(2)
def exact_matches_a(test):
    test.test = lambda : set(lib.getFunction("exact_matches",
        _fileName)("atgacatgcacaagtatgcat", "atgc")) == set([5,15])
    test.description = lambda : "exact_matches works for input 'atgacatgcacaagtatgcat', 'atgc'"

@t.passed(is_list_exact_matches)
@t.test(3)
def exact_matches_b(test):
    test.test = lambda : set(lib.getFunction("exact_matches",
        _fileName)("atgacatgca", "a")) == set([0, 3, 5, 9])
    test.description = lambda : "exact_matches works for input 'atgacatgca', 'a'"

@t.passed(is_list_exact_matches)
@t.test(4)
def exact_matches_c(test):
    test.test = lambda : set(lib.getFunction("exact_matches",
        _fileName)("atgacatgca", "b")) == set([])
    test.description = lambda : "exact_matches works for input 'atgacatgca', 'b'"

@t.passed(is_list_exact_matches)
@t.test(5)
def exact_matches_c(test):
    test.test = lambda : set(lib.getFunction("exact_matches",
        _fileName)("atgacatgca", "")) == set(range(10))
    test.description = lambda : "exact_matches works for input 'atgacatgca', ''"

@t.passed(is_list_exact_matches)
@t.test(6)
def exact_matches_c(test):
    test.test = lambda : set(lib.getFunction("exact_matches",
        _fileName)("", "test")) == set()
    test.description = lambda : "exact_matches works for input '', 'test'"
