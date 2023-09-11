#!/usr/bin/node

if (process.argv.length !== 3 || isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    let square = '';
    for (let j = 0; j < parseInt(process.argv[2], 10); j++) {
      square += 'x';
    }
    console.log(square);
  }
}
