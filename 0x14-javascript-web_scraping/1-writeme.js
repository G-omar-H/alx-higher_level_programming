#!/usr/bin/node
/**
 * script to write a string to a file
 */

const file = process.argv[2];
const string = process.argv[3];

const fs = require('node:fs');

fs.writeFile(file, string, err => {
  if (err) {
    console.log(err);
  }
});
