function uniteUnique(arr) {
  let arrays = Array.from(arguments);
  let result = [];
  for (let i = 0; i < arrays.length; i++){
    for (let j = 0 ; j < arrays[i].length; j++){
      result.push(arrays[i][j]);
    }
  }
  return [...new Set(result)]
}

uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);
