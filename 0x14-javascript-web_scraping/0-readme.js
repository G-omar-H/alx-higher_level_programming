#!/usr/bin/node
/**
 * script to read and print from a file
 */

const file = process.argv[2];

const fs = require('node:fs');

try {
  const data = fs.readFileSync(file, 'utf-8');
  console.log(data);
} catch (err) {
  console.error(err);
}
