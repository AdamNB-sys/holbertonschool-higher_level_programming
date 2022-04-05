#!/usr/bin/node
const size = process.argv[2];
// let square = '';

if (Number(size)) {
  for (let x = 0; x < size; x++) {
    console.log('X'.repeat(size));
  }
  // console.log(square);
} else {
  console.log('Missing size');
}
