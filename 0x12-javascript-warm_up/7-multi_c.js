#!/usr/bin/node
let firstArg = process.argv[2];
if (!firstArg || isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  firstArg = parseInt(firstArg);
  for (let j = 0; j < firstArg; j++) {
    console.log('C is fun');
  }
}
// It shows 3 lines: (in this way 1-multi_languages.js)
// Employ an array of string and iterate with a loop
