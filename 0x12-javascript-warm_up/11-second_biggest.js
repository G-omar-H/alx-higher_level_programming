#!/usr/bin/node
const list = [];
for (let i = 2; i < process.argv.length; i++) {
  list.push(parseInt(process.argv[i]));
}
let max = 0;
let second = 0;
for (let i = 0; i < list.length; i++) {
  if (list[i] > max) {
    max = list[i];
  }
  for (let j = 0; j < list.length; j++) {
    if (list[j] > second && list[j] < max) {
      second = list[j];
    }
  }
}
console.log(second);
