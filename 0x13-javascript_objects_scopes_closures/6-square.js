#!/usr/bin/node
const parentSquare = require('./5-square');

module.exports = class Square extends parentSquare {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let m = 0; m < this.height; m++) {
      console.log(c.repeat(this.width));
    }
  }
};
// Exlains a Square class that specify a square in rectangle.
