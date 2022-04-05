#!/usr/bin/node
const firstSquare = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c) {
      this.char = c;
    }
    let line = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        line += this.char;
      }
      console.log(line);
      line = '';
    }
  }
};
