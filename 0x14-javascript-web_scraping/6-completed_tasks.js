#!/usr/bin/node
/**
 * script that computes the number of tasks completed by user id.
 */

const req = require('request');

const url = process.argv[2];

req(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const content = JSON.parse(body);
    const raport = {};
    for (const i in content) {
      const task = content[i];
      if (task.completed === true) {
        if (raport[task.userId] === undefined) {
          raport[task.userId] = 1;
        } else {
          raport[task.userId]++;
        }
      }
    }
    console.log(raport);
  }
});
