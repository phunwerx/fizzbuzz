#include <stdio.h>

/*

Write a program that prints the numbers from 1 to 100. But for
multiples of three print "Fizz" instead of the number and for the
multiples of five print "Buzz". For numbers which are multiples of
both three and five print "FizzBuzz".

*/

int main(int argc, char ** argv)
{
  int i;
  for (i = 1; i <= 100; i++){
    if ((i % 3) == 0)
      printf("Fizz");

    if ((i % 5) == 0)
      printf("Buzz");

    if ((i % 3) && (i % 5))
      printf("%d",i);

    printf("\n");
  }
  return 0;
}
