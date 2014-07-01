#include <stdio.h>

/*

Write a program that prints the numbers from 1 to 100. But for
multiples of three print "Fizz" instead of the number and for the
multiples of five print "Buzz". For numbers which are multiples of
both three and five print "FizzBuzz".

*/

int main(int argc, char ** argv)
{
  int i, fizzy=0, buzzy=0;

  for (i = 1; i < 101; i++,fizzy=!(i%3), buzzy=!(i%5)){
    if (fizzy)
      printf("Fizz");

    if (buzzy)
      printf("Buzz");

    if (!(fizzy || buzzy))
      printf("%d",i);

    printf("\n");
  }
  return 0;
}
