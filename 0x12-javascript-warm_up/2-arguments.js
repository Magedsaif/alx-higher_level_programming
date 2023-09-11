#!/usr/bin/node
if (!process.argv[2]) {
  console.log('No argument');
}
if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
}
