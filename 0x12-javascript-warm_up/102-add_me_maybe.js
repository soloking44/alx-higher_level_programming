#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
// It runs a function 'x' number of times.
