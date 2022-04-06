#!/usr/bin/node
exports.converter = function (base) { 
    return function convertir(numerito) {
        return numerito.toString(base);
    };
};
