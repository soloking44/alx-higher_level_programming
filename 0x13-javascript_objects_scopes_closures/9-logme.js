#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
// It shows the value of arguments that has been displayed.
