#!/usr/bin/node
// a script that prints the number of movies where the character “Wedge Antilles” is present.
// The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
// Wedge Antilles is character ID 18
// You must use the module request
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    for (const film of results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
