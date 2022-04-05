#!/usr/bin/node
// prints arg to stdout if it is a number
if (Number(process.argv[2])) {
    console.log(`My number: ${process.argv[2]}`);
} else {
    console.log('Not a number');
}
