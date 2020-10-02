/*
<< Bubble Sort Algorithm >>
Sometimes referred to as sinking sort, 
is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements and swaps them if they are in the wrong order. 
The pass through the list is repeated until the list is sorted. 
The algorithm, which is a comparison sort, 
is named for the way smaller or larger elements "bubble" to the top of the list.
More info -> https://en.wikipedia.org/wiki/Bubble_sort.
*/
// Getting a set of digits in Javacsri3
function bubbleSort() {
  const number = window.prompt("Enter a number with several digits: ");
  let digits = number.split('');                      // Convert number in an array of digits
  const digitsLength = digits.length;                 // Get string length
  let aux = 0;                                        // This is to the interchange min and max position

  // Bubble Sort Algorithm implementation
  for (let i = 0; i < digitsLength-1; i++) {          // For each digit in number
    for (let j = 0; j < ((digitsLength-1) - i); j++){ // For each digit in unordered sublist
      if (digits[j] > digits[j+1]) {                  // If digit in lower position is greater than the next digit ...
        aux = digits[j];                              // Temporary copy the grater digit to auxiliar position
        digits[j] = digits[j+1];                      // Copy the lower digit to lower position
        digits[j+1] = aux;                            // Copy the grater digit to greater index in list
      }                          
    }
  }


alert('Digits ordered from lower to greater:' + digits) // Print ordered list
}

