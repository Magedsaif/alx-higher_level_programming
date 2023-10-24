#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// You must use the module request
const request = require('request');
const url = process.argv[2];
const completedTasks = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    // Get the completed tasks for each user ID and store them in an object with
    // the user ID as the key and the number of completed tasks as the value
    const results = JSON.parse(body);
    for (const task of results) {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
