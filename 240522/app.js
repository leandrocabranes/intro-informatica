console.log(llamar(1, 3));
console.log(llamar(5, 0));
console.log(llamar(6, 4));
console.log(llamar(1, 2));
console.log(llamar(8, 3));

function llamar(numero1, numero2) {
  return suma(numero1, numero2);
}

function suma(numero1, numero2) {
  return numero1 + numero2
}