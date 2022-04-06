#!/usr/bin/node
let logg = 0;
exports.logMe = function (item) {
  console.log(`${logg}: ${item}`);
  logg++;
};
