function palindrome(str) {
  let symbols = /[\W_]/g;
  let cleanStr = str.replace(symbols, "").toLowerCase();
  let reverseStr = str.replace(symbols, "").split("").reverse().join("").toLowerCase();
  return cleanStr === reverseStr;
}

