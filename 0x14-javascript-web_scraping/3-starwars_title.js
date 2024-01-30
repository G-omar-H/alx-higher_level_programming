#!/usr/bin/node
/**
 * script to print the title of a start war movie
 * where episode number match given integer as argument
 */

const req = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
