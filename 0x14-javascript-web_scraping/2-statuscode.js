#!/usr/bin/node
/***
 * script to display the status code of a request
 */

const req = require('request');

const url = process.argv[2];

req(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});
