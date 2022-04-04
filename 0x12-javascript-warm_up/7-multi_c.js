#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
    for (let iterador = 0; iterador < process.argv[2]; iterador++) {
        console.log('C is fun');
    }
}