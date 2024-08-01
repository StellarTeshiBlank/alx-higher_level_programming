#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request(`https://swapi.dev/api/films/${id}/`, (error, response, body) => {
  if (error) {
    console.error('Request failed:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  try {
    const json = JSON.parse(body);
    console.log(json.title);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
