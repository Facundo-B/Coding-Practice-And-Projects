function truthCheck(collection, pre) {
  return collection.every((obj) => obj.hasOwnProperty(pre) && obj[pre]);
}

console.log(truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy", "sex": "male"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex"))
