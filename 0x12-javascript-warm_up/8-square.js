#!/usr/bin/node
let firstArg = process.argv[2];
if (!firstArg || isNaN(firstArg)) {
  console.log('Missing size');
} else {
  firstArg = parseInt(firstArg);
  for (let j = 0; j < firstArg; j++) {
    console.log('X'.repeat(firstArg));
  }
}
// This displays an square
