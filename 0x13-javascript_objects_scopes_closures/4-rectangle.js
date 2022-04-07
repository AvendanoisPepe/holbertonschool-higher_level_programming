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

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const temporal = this.width;
    this.width = this.height;
    this.height = temporal;
  }
};
