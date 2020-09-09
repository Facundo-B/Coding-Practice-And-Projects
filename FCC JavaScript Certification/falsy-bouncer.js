function bouncer(arr) {
  for(let i = 0; i < arr.length; i++){
    console.log(arr);
    if(!arr[i]){
      arr.splice(i,1);
      i--;
    }
  }
  return arr;
}

bouncer([7, "ate", "", false, 9]);
