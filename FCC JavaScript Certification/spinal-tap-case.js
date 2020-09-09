function spinalCase(str) {
  var regex = /\s+|_+/g;
  str = str.replace(/([a-z])([A-Z])/g, "$1 $2");
  return str.toLowerCase().split(/\s+|_+/g).join("-")
}

spinalCase('This Is Spinal Tap');
