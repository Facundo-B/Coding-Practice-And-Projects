function translatePigLatin(str) {
  if(/^[^aeiou]/i.test(str)){
    let consonantRegex = /([^aeiou]+)(\w+)?/i;
    return str.replace(consonantRegex, "$2$1")+"ay";
  } else {
    return str + "way";
  }
  
}

translatePigLatin("consonant");
