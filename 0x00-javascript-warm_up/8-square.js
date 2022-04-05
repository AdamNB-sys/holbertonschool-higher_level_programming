#!/usr/bin/node
const size = process.argv[2];
let square = '';

if (Number(size)) {
  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      square += 'X';
    }
    square += '\n';
  }
  console.log(square);
} else {
  console.log('Missing number of occurrences');
}
