'use strict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function min_function(input) {
  var result = input[0]
  for (var i = 1; i < input.length; i++) {
    if (input[i] < result) {
      result = input[i];
    }
  }
  return result
}

console.log(min_function(numbers))
