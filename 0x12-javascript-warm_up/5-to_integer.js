#!/usr/bin/node
if (!isNaN(parseInt(process.argv[2], 10))) {
  console.log('My number:' + ' ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
