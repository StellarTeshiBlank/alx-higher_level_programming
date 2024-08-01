#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error('Request failed:', err);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  try {
    fs.writeFileSync(filePath, body);
    console.log(`Data written to ${filePath}`);
  } catch (writeErr) {
    console.error('Failed to write file:', writeErr);
  }
});
