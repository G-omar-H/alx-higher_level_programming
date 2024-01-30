#!/usr/bin/node
/**
 * script that gets the contents of a webpage and stores it in a file.
 */

const req = require('request');

const fs = require('fs');

const url = process.argv[2];

const path = process.argv[3];

req(url).pipe(fs.createWriteStream(path));
