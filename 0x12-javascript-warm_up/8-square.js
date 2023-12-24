#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  let y = parseInt(process.argv[2]);
  while (y) {
    let z = x;
    while (z) {
      process.stdout.write('X');
      z--;
    }
    console.log();
    y--;
  }
}
