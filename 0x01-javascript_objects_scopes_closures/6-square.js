#!/usr/bin/node
const Square2 = require('./5-square');

module.exports = class Square extends Square2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let x = 0; x < this.width; x++) {
        console.log(c.repeat(this.width));
      }
    } else {
      for (let x = 0; x < this.width; x++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
