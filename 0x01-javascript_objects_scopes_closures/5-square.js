#!/usr/bin/node
import Rectangle from './4-rectangle';
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
