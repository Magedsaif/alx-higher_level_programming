#!/usr/bin/node
// a script that display the status code of a GET request.
// The first argument is the URL to request (GET)
// The status code must be printed like this: code: <status code>

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
