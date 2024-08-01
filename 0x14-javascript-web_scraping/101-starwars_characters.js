#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.dev/api/films/';
const id = parseInt(process.argv[2], 10);

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
    const results = resp.results;

    let filmId = id < 4 ? id + 3 : id - 3;
    const film = results.find(film => film.episode_id === filmId);

    if (film) {
      const characters = film.characters;

      for (const characterUrl of characters) {
        try {
          const characterBody = await fetchUrl(characterUrl);
          const character = JSON.parse(characterBody);
          console.log(character.name);
        } catch (characterErr) {
          console.error('Error fetching character:', characterErr);
        }
      }
    } else {
      console.log('Film not found');
    }
  } catch (err) {
    console.error('Error fetching films:', err);
  }
}

main();
