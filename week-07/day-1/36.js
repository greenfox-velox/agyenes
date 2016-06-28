'use strict';

var ah = [3, 4, 5, 6, 7];
// print the sum of all numbers in ah

var a = 0
var sum = 0

while (a < ah.length) {
  a += 1;
  sum += ah[a-1];
}

console.log(sum)
