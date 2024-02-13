#!/usr/bin/node
const request = require('request');
const args = process.argv;

const fetchCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, data) => {
      if (!err && res.statusCode === 200) {
        const character = JSON.parse(data);
        resolve(character.name);
      } else {
        reject(err);
      }
    });
  });
};

if (args.length === 3) {
  request(
`https://swapi-api.alx-tools.com/api/films/${args[2]}`,
(err, res, data) => {
  if (!err && res.statusCode === 200) {
    const characters = JSON.parse(data).characters;

    const fetchPromises = characters.map((url) =>
      fetchCharacter(url)
    );
    Promise.all(fetchPromises)
      .then((names) => {
        names.forEach((name) => console.log(name));
      })
      .catch((err) => console.error('Error:', err));
  } else {
    console.error('Error:', err);
  }
}
  );
}
