#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 && (h = parseInt(h)) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let iterador = 0;
    while (iterador < this.height) {
      console.log('X'.repeat(this.width));
      iterador++;
    }
  }
};
