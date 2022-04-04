#!/usr/bin/node
function facturameESTA (numerito) {
  if (numerito === 0 || isNaN(numerito)) {
    return (1);
  }
  return (numerito * facturameESTA(numerito - 1));
}
console.log(facturameESTA(Number(process.argv[2])));
