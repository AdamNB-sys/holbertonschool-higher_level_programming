#!/usr/bin/node
// prints a message based on number of args passed
const args = process.argv.length

if (args <= 2) {
    console.log('No argument')
} else if (args === 3) {
    console.log('Argument found')
} else {
    console.log('Arguments found')
}

/*if (process.argv.length <= 3) {
    console.log('Argument found')
}
console.log(process.argv[0])
console.log(process.argv[1])
console.log(process.argv[2])
console.log(process.argv[3])*/
