#!/usr/bin/node
let firstArg = process.argv[2];
if (!firstArg || isNaN(firstArg)) {
  console.log('Not a number');
} else {
  firstArg = parseInt(firstArg);
  console.log('My number: ' + firstArg);
}
// It shows 2 arguments given, in this order: “ is ”
