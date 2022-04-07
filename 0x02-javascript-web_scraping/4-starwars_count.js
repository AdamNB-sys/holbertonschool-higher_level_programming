#!/usr/bin/node
const request = require('request');

request(process.argv[2], { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  // console.log(body.results);
  const response = (body.results);
  // console.log(response);
  let wedgeCount = 0;
  for (const movies in response) {
    const characters = response[movies].characters;
    // console.log(characters);
    for (const Wedge in characters) {
      if (characters[Wedge].includes('/18/')) {
        // console.log(`Wedge found! : ${characters[Wedge]}`);
        wedgeCount += 1;
      }
    }
  }
  console.log(wedgeCount);
});
