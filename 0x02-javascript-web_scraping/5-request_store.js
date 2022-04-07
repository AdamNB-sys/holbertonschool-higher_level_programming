#!/usr/bin/node
const request = require('request');
const fs = require('fs');
// const fileWriter = fs.createWriteStream(process.argv[3]);

request(process.argv[2], { json: true }, (err, res, body) => {
  if (err) {
    return console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', err => {
      if (err) { return console.log(err); }
    });
  }
});
