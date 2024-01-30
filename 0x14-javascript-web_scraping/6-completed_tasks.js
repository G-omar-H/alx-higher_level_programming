#!/usr/bin/node
/**
 * script that computes the number of tasks completed by user id.
 */

const req = require('request');

const url = process.argv[2];

req(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const content = JSON.parse(body);
  const raport = {};
  let count = 0;
  let id = 1;
  for (const i in content) {
    if (content[i].userId !== id) {
      id += 1;
      count = 0;
    }

    if (content[i].userId === id) {
      if (content[i].completed === true) {
        count += 1;
        raport[content[i].userId] = count;
      }
      console.log('>>', content[i].userId);
      console.log('...', id);
      console.log('completed=', content[i].completed);
      console.log('count=', count);
    }
  }
  console.log(raport);
});
