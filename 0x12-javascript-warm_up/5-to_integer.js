#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[2].match(/^\s*?([0-9]+)\.?([0-9]+)?\s*?$/) === null) {
  console.log('Not a number');
} else {
  console.log('My number:', process.argv[2].trim());
}
