#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2] || 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Request failed:', err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  try {
    const tasks = JSON.parse(body);
    const userCompletedTasks = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (!userCompletedTasks[task.userId]) {
          userCompletedTasks[task.userId] = 0;
        }
        userCompletedTasks[task.userId]++;
      }
    });

    // Print only users with completed tasks
    for (const [userId, count] of Object.entries(userCompletedTasks)) {
      console.log(`User ${userId} has completed ${count} tasks.`);
    }

  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
