'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortest_string(input) {
  var result = input[0]
  for (var i = 1; i < input.length; i++) {
    if (input[i].length < result.length) {
      result = input[i];
    }
  }
  return result
}

console.log(shortest_string(names))
