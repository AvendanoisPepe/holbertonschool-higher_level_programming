#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    try {
      fs.writeFile(process.argv[3], body, 'utf8', function (err, result) {
        if (err) {
          console.log(err);
        }
      });
    } catch (err) {
      console.log(err);
    }
  }
});
