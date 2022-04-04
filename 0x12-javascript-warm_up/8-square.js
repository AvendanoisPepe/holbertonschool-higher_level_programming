#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let iterador = 0; iterador < process.argv[2]; iterador++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
