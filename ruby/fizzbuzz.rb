#!/usr/bin/env ruby

#
# 
# Write a program that prints the numbers from 1 to 100. But for
# multiples of three print "Fizz" instead of the number and for the
# multiples of five print "Buzz". For numbers which are multiples of
# both three and five print "FizzBuzz".
# 
#

class FizzBuzz
  def run
    1.upto(100) do |i|
      fizzy, buzzy = (i%3).zero?, (i%5).zero?
      print 'Fizz' if fizzy
      print 'Buzz' if buzzy
      print i unless fizzy or buzzy
      print "\n"
    end
  end
end

def main
  $stdout.sync = true
  FizzBuzz.new.run
end

if __FILE__ == $0
    main
end
