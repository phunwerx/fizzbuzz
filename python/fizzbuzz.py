#!/usr/bin/python

import sys

#
#
# Write a program that prints the numbers from 1 to 100. But for
# multiples of three print "Fizz" instead of the number and for the
# multiples of five print "Buzz". For numbers which are multiples of
# both three and five print "FizzBuzz".
#
#

class FizzBuzz:
    def run(self):
        for i in range(1,100+1):
            fizzy, buzzy = ((i % 3) == 0),((i % 5) == 0)
            if fizzy: sys.stdout.write("Fizz")
            if buzzy: sys.stdout.write("Buzz")
            if not (fizzy or buzzy): sys.stdout.write("%d" % i) 
	    sys.stdout.write('\n')

def main():
    FizzBuzz().run();

if __name__ == "__main__":
    main()
