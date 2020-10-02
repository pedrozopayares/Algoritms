<?php
    // Getting a set of digits in PHP
    $number = $_GET["number"]; // <- Replace this number in the URL. http://localhost:80/SelectionSort.php?number=654658864368921;
    $digits  = array_map('intval', str_split($number)); // Map number in an array of digits
    $digitsLength = count($digits);                     // Get array length
    $aux = 0;                                           // To temporary store smaller value
    $smaller = 0;                                       // To store the index of smaller number
  
    // Selection Sort Algorithm implementation
    for ($i=0; $i < $digitsLength; $i++) {              // For each digit in number
      $smaller = $i;                                    // I assume the item in the first potition of list is the smaller
      for ($j=($i+1); $j < $digitsLength; $j++) {       // For each digit in unordered sublist
        if ($digits[$j] < $digits[$smaller]) {          // If digit in j position is smaller than the actual ...
          $smaller = $j;                                // Update index position of smaller digit
        }
      }        
      $aux = $digits[$i];                               // Copy the digit to be replaced to temp variable
      $digits[$i] = $digits[$smaller];                  // Copy the grater digit to greater index in list
      $digits[$smaller] = $aux;                         // Copy the grater digit to greater index in list 
    }
    echo 'Digits ordered from lower to greater: <br/>';
    print_r ($digits); // Print ordered list
?>