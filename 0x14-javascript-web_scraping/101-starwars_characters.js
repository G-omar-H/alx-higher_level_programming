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
  const char = JSON.parse(body).characters;
  printchar(char, 0);
});

function printchar (characters, index) {
  req(characters[index], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
    }
    if (index + 1 < characters.length) {
      printchar(characters, index + 1);
    }
  });
}
