#!/usr/bin/node
module.exports = class Rectangle {
  constructor (_w, _h) {
    this.width = _w;
    this.height = _h;
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log("X".repeat(this.width));
    }
  }
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
