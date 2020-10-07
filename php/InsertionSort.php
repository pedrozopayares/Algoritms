<?php
    // Getting a set of digits in PHP
    $number = $_GET["number"]; // <- Replace this number in the URL. http://localhost:80/BubbleSort.php?number=454646464;
    $digits  = array_map('intval', str_split($number)); // Map number in an array of digits
    $digitsLength = count($digits);                     // Get string length
    $aux = 0;                                           // This is to the interchange min and max position
  
    // Bubble Sort Algorithm implementation
    for ($i = 0; $i < $digitsLength-1; $i++) {           // For each digit in number
      for ($j = 0; $j < (($digitsLength-1) - $i); $j++){ // For each digit in unordered sublist
        if ($digits[$j] > $digits[$j+1]) {               // If digit in lower position is greater than the next digit ...
          $aux = $digits[$j];                            // Temporary copy the grater digit to auxiliar position
          $digits[$j] = $digits[$j+1];                   // Copy the lower digit to lower position
          $digits[$j+1] = $aux;                          // Copy the grater digit to greater index in list
        }                          
      }
    }
    echo 'Digits ordered from lower to greater: <br/>';
    print_r ($digits); // Print ordered list
?>