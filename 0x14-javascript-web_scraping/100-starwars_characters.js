#!/usr/bin/node
const request = require('request');
const url = `http://swapi.dev/api/films/${process.argv[2]}/`;

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) {
        reject(err);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch data. Status code: ${response.statusCode}`));
      } else {
        resolve(body);
      }
    });
  });
}

async function main() {
  try {
    const body = await fetchUrl(url);
    const resp = JSON.parse(body);
    const characters = resp.characters;

    // Output the number of characters
    console.log(`Number of characters: ${characters.length}`);
  } catch (err) {
    console.error('Error fetching film:', err);
  }
}

main();
