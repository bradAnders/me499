#!/usr/bin/env python


from complex import Complex
from random import uniform


def do_all_tests():
    NUM_TESTS = 1000

    passed = 0
    total = 0

    # Binary operators
    tests = [lambda x,y: x + y, lambda x,y: x - y, lambda x,y: x * y, lambda x,y: x / y]
    for test in tests:
        passed += do_binary_tests(test, NUM_TESTS)
        total += NUM_TESTS

    print 'Passed {0} of {1} tests: {2:.2f}%'.format(passed, total, passed * 100.0 / total)


def do_binary_tests(f, n):
    total = 0
    for i in xrange(n):
        try:
            ar,ai,br,bi = [uniform(-10, 10) for x in xrange(4)]
            a = complex(ar, ai)
            b = complex(br, bi)
            answer = f(a, b)
            a = Complex(ar, ai)
            b = Complex(br, bi)
            guess = f(a, b)

            if answer.real == guess.re and answer.imag == guess.im:
                total += 1
        except:
            pass

    return total


if __name__ == '__main__':
    do_all_tests()

