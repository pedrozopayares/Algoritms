<?php
    /* 
    << Insertion Sort Algorithm >>
    Insertion sort is a simple sorting algorithm that builds the final sorted array 
    (or list) one item at a time.  It is much less efficient on large lists than 
    more advanced algorithms such as quicksort, heapsort, or merge sort. 

    However, insertion sort provides several advantages: 
    - Efficient for (quite) small data sets, much like other quadratic sorting algorithms
    - Adaptive, stable, in-place, online.

    More info: https://en.wikipedia.org/wiki/Insertion_sort
    See running: https://paiza.io/projects/e/npQ98Ovw0NuIz9lXXdW33w?theme=twilight
    JavaScript version: https://codepen.io/pedrozopayares/pen/QWEWwvd
    Ptyhon 3 version: https://colab.research.google.com/drive/1bSSMi8pzMevl_xg34rkRU-_POSQXsADk?usp=sharing
    */
    // Getting a set of digits in PHP
    $number = $_GET["number"]; // <- Replace this number in the URL. http://localhost:80/InsertionSort.php?number=454646464;
    $digits  = array_map('intval', str_split($number));// Map number in an array of digits
    $digitsLength = count($digits);                    // Get string length
    $aux = 0;                                          // This is to the interchange min and max position
  
    // Insertion Sort Algorithm implementation
    for ($i = 0; $i < $digitsLength; $i++) {           // Unordered list starts at 2nd position
      $j = $i;                                         // Get first element from unordered list
      while ($j > 0 && $digits[$j-1] > $digits[$j]) {  // For each digit in unordered sublist
        $aux = $digits[$j-1];                          // Temporary copy the grater digit to auxiliar position
        $digits[$j-1] = $digits[$j];                   // Copy the lower digit to lower position
        $digits[$j] = $aux;                            // Copy the grater digit to greater index in list                  
        $j--;                                          // Move to left
      }
    }
    echo 'Digits ordered from lower to greater: <br/>';
    print_r ($digits); // Print ordered list
?>