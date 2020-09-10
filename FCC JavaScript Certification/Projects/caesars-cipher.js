function rot13(str) {
  return str.replace(/[A-Z]/g, (letter) =>
    String.fromCharCode(letter.charCodeAt() % 26 + 65)
    );
}

console.log(rot13("GUVF VF RAPBQRQ!"));


function rot13Encode(str){
  return str.replace(/[A-Z]/g, (letter) =>
    String.fromCharCode(letter.charCodeAt() % 26 - 65)
    );
}

console.log(rot13("THIS IS ENCODED!"));