#!/usr/bin/node
const request = require('request');
const id = '/18/';
let iterador = 0;
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
      for (const pelicula of JSON.parse(body).results){
        for (const coincidencia of pelicula.characters){    
            if (coincidencia.includes(id)) {
                iterador++;
            }
        }
    }
      console.log(iterador);
  }
});
