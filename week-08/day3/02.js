'use strict';

// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error
//

var fs = require('fs');

function charCounter(filename, letter, cb) {
  fs.readFile(filename, function(err, content) {
    if (err) {
      return cb(err);
    }
    var counter = 0;
    for (var i=0; i < content.length; i++) {
      if (String(content).split('')[i] === letter) {
        counter++;
      }
    }
    cb(null, counter);
    });
  };

function writeOut(err, counter){
  console.log(err, counter);
}

charCounter('majom.txt', 'm', writeOut)
charCounter('majom.txt', 'r', writeOut)
charCounter('majom.txt', 'a', writeOut)
charCounter('majom.txt', 'x', writeOut)
