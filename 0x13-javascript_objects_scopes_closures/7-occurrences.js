#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let m = 0; m < list.length; m++) {
    if (list[m] === searchElement) {
      count++;
    }
  }
  return count;
};
// A process that yields the digit of instances in series.
