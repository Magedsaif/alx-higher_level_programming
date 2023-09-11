#!/usr/bin/node
const number1 = process.argv[2];
const number2 = process.argv[3];
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
console.log(add(number1, number2));
