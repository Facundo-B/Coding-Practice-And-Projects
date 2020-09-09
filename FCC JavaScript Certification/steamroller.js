function steamrollArray(arr) {
  let flattenedArray = [];
  let flatten = (array) => {
    if (!Array.isArray(array)) {
      flattenedArray.push(array);
    } else {
      for (let a in array) {
        flatten(array[a]);
      }
    }
  }
  arr.forEach(flatten);
  return flattenedArray;
}

console.log(steamrollArray([1, [2], [3, [[4]]]]));
