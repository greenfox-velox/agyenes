'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

var result = 0

function sum_function(input) {
  for (var i = 0; i < input.length; i++) {
    result += input[i];
  }
  return result;
}

console.log(sum_function(numbers))
