#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request(`https://swapi.dev/api/films/${id}/`, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    try {
      const json = JSON.parse(body);
      console.log(json.title);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error fetching data:', error || `Status Code: ${response.statusCode}`);
  }
});
