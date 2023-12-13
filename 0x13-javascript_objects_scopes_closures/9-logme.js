#!/usr/bin/node
let ins = 0;
exports.logMe = function (item) {
  console.log(ins + ': ' + item);
  return ins++;
};
