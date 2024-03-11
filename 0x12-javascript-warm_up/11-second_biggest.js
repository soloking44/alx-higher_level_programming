#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  console.log(arr.sort((x, m) => x - m)[arr.length - 2]);
}
// Identifies the 2nd largest value within the given set of arguments
