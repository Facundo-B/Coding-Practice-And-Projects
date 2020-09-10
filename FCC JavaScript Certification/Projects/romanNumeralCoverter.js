function convertToRoman(num) {
 let rom = ["I", "V", "X", "L", "C", "D", "M"]

 //Split the number into its digits
 let digits = num.toString().split("").map(Number);

 //Create an index that we will use to move across the roman numerals
 //for units, tens, hundreds and thousands
 let romIndex = 2*digits.length;
 console.log(digits)
 for (let i = 0; i < digits.length; i++){
   switch(digits[i]){
      case 0:
        digits[i]="";
        break;
      case 1:
        digits[i] = rom[romIndex-2];
        break;
      case 2:
        digits[i] = rom[romIndex-2]+rom[romIndex-2];
        break;
      case 3:
        digits[i] = rom[romIndex-2]+rom[romIndex-2]+rom[romIndex-2];
        break;
      case 4:
        digits[i] = rom[romIndex-2]+rom[romIndex-1];
        break;
      case 5:
        digits[i] = rom[romIndex-1];
        break;
      case 6:
        digits[i] = rom[romIndex-1]+rom[romIndex-2];
        break;
      case 7:
        digits[i] = rom[romIndex-1]+rom[romIndex-2]+rom[romIndex-2];
        break;
      case 8:
        digits[i] = rom[romIndex-1]+rom[romIndex-2]+rom[romIndex-2]+rom[romIndex-2];
        break;
      case 9:
        digits[i] = rom[romIndex-2]+rom[romIndex];
        break;
      default:
        break;
    }
    romIndex-=2;
    console.log(digits);
  }
  return digits.join("")
}


//Another Solution

function convertToRomanAlt(num) {
  var decimalValue = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  var romanNumeral = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "XC",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I"
  ];

  var romanized = "";

  for (var index = 0; index < decimalValue.length; index++) {
    while (decimalValue[index] <= num) {
      romanized += romanNumeral[index];
      num -= decimalValue[index];
      console.log(romanized);
    }
  }

  return romanized;
};

convertToRomanAlt(1234)
