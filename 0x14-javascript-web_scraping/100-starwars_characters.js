#!/usr/bin/node
/**
 * script that prints all characters of a Star Wars movie
 */

const req = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  res = JSON.parse(body);
  for (const i in res.characters) {
    const char = res.characters[i];
    req(char, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }
      res = JSON.parse(body);
      console.log(res.name);
    });
  }
});
