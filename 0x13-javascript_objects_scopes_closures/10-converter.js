#!/usr/bin/node
exports.converter = function (base) {
  return (num) => {
    return num.toString(base);
  };
};
// It changes a value from base 10 to other base given.
