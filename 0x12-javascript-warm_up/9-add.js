#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined || isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(NaN);
} else {
  const sum = parseInt(process.argv[2]) + parseInt(process.argv[3]);
  console.log(sum);
}
