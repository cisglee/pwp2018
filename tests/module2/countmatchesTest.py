import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def has_count_exact_matches(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "count_exact_matches")
    test.description = lambda : "defines the function count_exact_matches"

@t.passed(has_count_exact_matches)
@t.test(1)
def is_int_count_exact_matches(test):
    test.test = lambda : assertlib.sameType(lib.getFunction("count_exact_matches", _fileName)("a", "a"), 0)
    test.description = lambda : "count_exact_matches returns the right integer"

@t.passed(is_int_count_exact_matches)
@t.test(2)
def count_exact_matches_2(test):
    test.test = lambda : assertlib.exact(
        lib.getFunction("count_exact_matches",
        _fileName)("atgacatgcacaagtatgcat", "atgc"), 2)
    test.description = lambda : "count_exact_matches works for input 'atgacatgcacaagtatgcat', 'atgc'"

@t.passed(is_int_count_exact_matches)
@t.test(3)
def count_exact_matches_8(test):
    test.test = lambda : assertlib.exact(
        lib.getFunction("count_exact_matches",
        _fileName)("atgacatgcacaagtatgcat", "a"),  8)
    test.description = lambda : "count_exact_matches works for input 'atgacatgcacaagtatgcat', 'a'"

@t.passed(is_int_count_exact_matches)
@t.test(4)
def count_exact_matches_0a(test):
    test.test = lambda : assertlib.exact(
        lib.getFunction("count_exact_matches",
        _fileName)("atgacatgcacaagtatgcat", "b"), 0)
    test.description = lambda : "count_exact_matches works for input 'atgacatgcacaagtatgcat', 'b'"

@t.passed(is_int_count_exact_matches)
@t.test(5)
def count_exact_matches_0b(test):
    test.test = lambda : assertlib.exact(
        lib.getFunction("count_exact_matches",
        _fileName)("", "atgc"), 0)
    test.description = lambda : "count_exact_matches works for input '', 'atgc'"
