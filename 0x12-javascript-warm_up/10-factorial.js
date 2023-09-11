#!/usr/bin/node
const number1 = process.argv[2];
if (!isNaN(process.argv[2])) {
  function factorial (a) {
    if (a === 0) {
      return 1;
    } else {
      return a * factorial(a - 1);
    }
  }
  console.log(factorial(Number(number1)));
} else {
  console.log(1);
}
