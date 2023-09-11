#!/usr/bin/node

if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    console.log('X'.repeat(parseInt(process.argv[2], 10)));
  }
}
