function titleCase(str) {
  let cap_words = str.toLowerCase().split(" ");
  console.log(cap_words);
  cap_words = cap_words.map(word => word[0].toUpperCase() + word.slice(1,))
  console.log(cap_words);
  return cap_words.join(" ");
}

titleCase("I'm a little tea pot");
