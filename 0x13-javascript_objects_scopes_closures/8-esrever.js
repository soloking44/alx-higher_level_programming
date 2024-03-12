#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let m = list.length - 1; m >= 0; m--) {
    newList.push(list[m]);
  }
  return newList;
};
// A process that yields the inversed version in series.
