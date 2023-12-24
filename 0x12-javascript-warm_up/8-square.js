#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  let y = parseInt(process.argv[2]);
  while (y > 0) {
    let z = x;
    while (z > 0) {
      process.stdout.write('X');
      z--;
    }
    console.log();
    y--;
  }
}
