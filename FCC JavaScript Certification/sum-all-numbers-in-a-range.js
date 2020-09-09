function sumAll(arr) {
  let sum = 0;
  let i = 0
  for(i = Math.min(...arr); i <= Math.max(...arr); i++){
    sum += i;
  }
  return sum;
}

sumAll([1, 4]);
