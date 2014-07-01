#!/usr/bin/python

import sys

#
#
#Write a program that prints the numbers from 1 to 100. But for
#multiples of three print "Fizz" instead of the number and for the
#multiples of five print "Buzz". For numbers which are multiples of
#both three and five print "FizzBuzz".
#
#

class FizzBuzz:
    def run(self):
        for i in range(1,100+1):
            if ((i % 3) == 0):
                sys.stdout.write("Fizz")
	    if ((i % 5) == 0):
	        sys.stdout.write("Buzz")
	    if ((i % 3) and (i % 5)):
	        sys.stdout.write("%d" % i)
	    sys.stdout.write('\n')

def main():
    pass

if __name__ == "__main__":
    main()
