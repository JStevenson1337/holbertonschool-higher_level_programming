#!/usr/bin/node
module.exports = class Rectangle {
  constructor (_w, _h) {
    if ( _w > 0 && _h > 0 ) {
      this.width = _w;
      this.height = _h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log("X".repeat(this.width));
    }
  }
};
