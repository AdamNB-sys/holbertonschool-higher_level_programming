#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log(body.title);
});
