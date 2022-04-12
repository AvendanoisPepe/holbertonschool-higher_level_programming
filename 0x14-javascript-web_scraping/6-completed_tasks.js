#!/usr/bin/node
const request = require('request');
const usarioslista = {};
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    for (const usuario of JSON.parse(body)) {
      if (usuario.completed === true) {
        if (!usarioslista[usuario.userId]) {
          usarioslista[usuario.userId] = 1;
        } else {
          usarioslista[usuario.userId] += 1;
        }
      }
    }
    console.log(usarioslista);
  }
});
