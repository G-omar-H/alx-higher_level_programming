#!/usr/bin/node
/**
 * script to return number of movies where the character "Wedge Antille"
 * is present
 */

const req = require('request');

const url = process.argv[2];

req(url, async function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  res = JSON.parse(body).results;
  console.log(res.map((char) => char.characters).flat().filter((url) => url.includes('18')).length);
});
