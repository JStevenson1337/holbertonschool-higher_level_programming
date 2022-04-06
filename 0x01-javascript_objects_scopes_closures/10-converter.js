#!/usr/bin/node
exports.converter = function (base) {
  return function toBase (number) {
    return number.toString(base);
  };
};
