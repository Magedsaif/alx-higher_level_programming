#!/usr/bin/node
// Script that reads and prints the content of a file.
// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

// fs = file system module to perform file operations in js (like read, write, append, delete, etc)
// fs.readFile() method is used to read files on your computer.
// This method takes two arguments, the path of the file and a callback function.
// The callback function has two arguments (err, data), where data is the content of the file.
// If no error occurred, err is null and data is the content of the file.
// If an error occurred, err would be of type error.

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) { console.log(err); } else { console.log(data); }
}
);
