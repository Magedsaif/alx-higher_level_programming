#!/usr/bin/node
if (process.argv[2] && process.argv[3]) {
  console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]);
} else {
  console.log(process.argv[2] + ' ' + 'is' + ' ' + 'undefined');
}
