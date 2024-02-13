#!/usr/bin/node
const request = require('request');
const args = process.argv;

if (args.length === 3) {
  request(
`https://swapi-api.alx-tools.com/api/films/${args[2]}`,
(error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;

    for (const ch of characters) {
      request(ch, (err, res, data) => {
        if (!err && res.statusCode === 200) {
          console.log(JSON.parse(data).name);
        } else {
          console.error('Error:', err);
        }
      });
    }
  } else {
    console.error('Error:', error);
  }
}
  );
}
