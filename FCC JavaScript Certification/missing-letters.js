function fearNotLetter(str) {
  for (var i = 0; i < str.length; i++) {
    var code = str.charCodeAt(i);
    if (i != str.length - 1 &&str.charCodeAt(i+1) - code != 1) {
      return String.fromCharCode(code + 1);
    }
  }
  return undefined;
}

fearNotLetter("abcdefghijklmnopqrstuvwxyz");
