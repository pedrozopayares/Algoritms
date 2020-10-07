
/* 
<< Insertion Sort Algorithm >>
Insertion sort is a simple sorting algorithm that builds the final sorted array 
(or list) one item at a time.  It is much less efficient on large lists than 
more advanced algorithms such as quicksort, heapsort, or merge sort. 

However, insertion sort provides several advantages: 
- Efficient for (quite) small data sets, much like other quadratic sorting algorithms
- Adaptive, stable, in-place, online.

More info: https://en.wikipedia.org/wiki/Insertion_sort
Ptyhon 3 version: https://colab.research.google.com/drive/1bSSMi8pzMevl_xg34rkRU-_POSQXsADk?usp=sharing
*/
function insertionSort() {
  // Getting a set of digits in JavaScript
  const number = window.prompt("Enter a number with several digits: ");
  let digits = number.split('');               // Convert number in an array of digits
  const digitsLength = digits.length;          // Get string lenght
  let aux = 0;                                 // To temporary store smaller value

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
