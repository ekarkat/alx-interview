#!/usr/bin/node

const request = require('request');
const movId = process.argv[2];

function film (movieId) {
  return new Promise((resolve, reject) => {
    request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        const data = JSON.parse(body);
        resolve(data.characters);
      }
    });
  });
}

function charName (peopleId) {
  return new Promise((resolve, reject) => {
    request(peopleId, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        const data = JSON.parse(body);
        resolve(data.name);
      }
    });
  });
}

async function result (movieId, charId) {
  const chars = await film(movieId);
  for (const link of chars) {
    const name = await charName(link);
    console.log(name);
  }
}

result(movId);
