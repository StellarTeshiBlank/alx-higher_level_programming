#!/usr/bin/node
const request = require('request');
let nFilms = 0;

request(process.argv[2], (err, response, body) => {
  if (!err && response.statusCode === 200) {
    try {
      const resp = JSON.parse(body);
      const results = resp.results;
      results.forEach(film => {
        film.characters.forEach(character => {
          if (character.includes('18')) {
            nFilms++;
          }
        });
      });
      console.log(nFilms);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error:', err || `Status code: ${response.statusCode}`);
  }
});
