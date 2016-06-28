'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

var new_list = []

function even_numbers(input) {
  for (var i = 0; i < input.length; i++) {
    if (input[i] % 2 !== 0) {
      new_list.push(input[i]);
    }
  }
  return new_list
}

console.log(even_numbers(numbers))
