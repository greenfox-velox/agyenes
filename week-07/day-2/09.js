'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 2, p: 2, l: 1}

function letter_count(input_string) {
  var letters = {};
  var listOfLetters = input_string.split('');
  listOfLetters.forEach (function(e) {
    if (e in letters) {
      letters[e]++;
    } else {
      letters[e] = 1;
    }
  });
  return letters;
}

console.log(letter_count('appppppplllle'))
