#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const fileWriter = fs.createWriteStream(process.argv[3]);

request(process.argv[2], { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  // console.log(body);
  fileWriter.write(body, 'utf-8');
});
