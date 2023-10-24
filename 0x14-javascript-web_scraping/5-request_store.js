#!/usr/bin/node
// a script that fetches the content of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

// Get the URL and the file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    // Write the content to the file
    fs.writeFile(filePath, body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
