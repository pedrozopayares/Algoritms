/* 
<< Selection Sort Algorithm >>
In computer science, selection sort is an in-place comparison sorting algorithm. 
It has an O(n2) time complexity, which makes it inefficient on large lists, 
and generally performs worse than the similar insertion sort. 
Selection sort is noted for its simplicity and has performance advantages over 
more complicated algorithms in certain situations, 
particularly where auxiliary memory is limited.
More info: https://en.wikipedia.org/wiki/Selection_sort
*/
function selectionSort() {
  // Getting a set of digits in JavaScript
  const number = window.prompt("Enter a number with several digits: ");
  let digits = number.split('');               // Convert number in an array of digits
  const digitsLength = digits.length;          // Get string lenght
  let aux = 0;                                 // To temporary store smaller value
  let smaller = 0                              // To store the index of smaller number

  // Selection Sort Algorithm implementation
  for (i=0; i < digitsLength; i++) {            // For each digit in number
    smaller = i;                                // I assume the item in the first potition of list is the smaller
    for (j=i+1; j < digitsLength; j++) {         // For each digit in unordered sublist
      if (digits[j] < digits[smaller]) {         // If digit in j position is smaller than the actual ...
        smaller = j;                            // Update index position of smaller digit
      }
    }        
    aux = digits[i];                            // Copy the digit to be replaced to temp variable
    digits[i] = digits[smaller];                 // Copy the grater digit to greater index in list
    digits[smaller] = aux;                  // Copy the grater digit to greater index in list 
  }          
    

  alert('Digits ordered from lower to greater:' + digits) // Print ordered list
}
