#!/usr/bin/node
/**
 * script to read and print from a file
 */

const file = process.argv[2];

const fs = require('fs');

fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
