#!/usr/bin/node
const x = process.argv

if (Number(x[2])) {
  for (let i = 0; i < x[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
