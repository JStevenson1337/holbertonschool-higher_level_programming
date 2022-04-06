#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const occurencesLength = list.filter(n => n === searchElement);
  return occurencesLength.length;
};
