'use strict';

// create a function that returns it's input factorial

var result = 1

function fact_function(input) {
  for (var i = 1; i <= input; i++) {
    result *= i;
  }
  return result;
}

console.log(fact_function(5))
