#!/usr/bin/perl

for my $i (1..100){
    my ($fizzy,$buzzy) = (!($i%3),!($i%5));
    print "Fizz" if $fizzy;
    print "Buzz" if $buzzy;
    print $i unless ($fizzy || $buzzy);
    print "\n";
}
