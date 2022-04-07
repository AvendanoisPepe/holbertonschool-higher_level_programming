#!/usr/bin/node
exports.esrever = function (list) {
  const nuevo = [];
  while (list.length) {
    nuevo.push(list.pop());
  }
  return (nuevo);
};
