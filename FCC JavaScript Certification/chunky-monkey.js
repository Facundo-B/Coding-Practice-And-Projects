function chunkArrayInGroups(arr, size) {
  let groups = [];
  for(let i = 0; i < arr.length; i+=size){
    groups.push(arr.slice(i, i+size));
  }
  return groups;
}

chunkArrayInGroups(["a", "b", "c", "d"], 2);
