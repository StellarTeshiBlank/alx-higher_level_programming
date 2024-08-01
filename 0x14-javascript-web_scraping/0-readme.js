#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, contents) => {
  if (err) {
    console.error('Error reading file:', err);
  } else {
    console.log(contents);
  }
});
