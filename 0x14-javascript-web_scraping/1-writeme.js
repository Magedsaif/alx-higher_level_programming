#!/usr/bin/node
// a script that writes a string to a file.

const fs = require('fs');
const data = process.argv[3];
try {
  fs.writeFileSync(process.argv[2], data, 'utf-8');
} catch (err) {
  console.error(err);
}
