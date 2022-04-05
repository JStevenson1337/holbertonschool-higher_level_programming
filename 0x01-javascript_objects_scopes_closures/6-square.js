#!/usr/bin/node
class Rectangle = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c) {
      if (c.length === 1) {
        this.char = c;
      } else {
        for (let i = 0; i < c.length; i++) {
          if (c[i] === '\n') {
            this.char = '\n';
            break;
          }
        }
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(this.char.repeat(this.width));
    }
  }
};

