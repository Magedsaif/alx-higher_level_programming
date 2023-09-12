#!/usr/bin/node
const ImportedSquare = require('./5-square');

class Square extends ImportedSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
