#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let contador = 0;
    for (let iterador = 0; iterador < list.length; iterador++){
        if (list[iterador] === searchElement){
            contador++;
        }
    }
    return (contador)
}