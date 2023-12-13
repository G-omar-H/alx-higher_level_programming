#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    let X = 'X';
    if (c) {
      X = 'c';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(X.repeat(this.width));
    }
  }
};
