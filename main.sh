#!/usr/bin/env bash

fizzbuzz () {
	for i in `seq 0 $1`;
	do
		if (( $i % 5 == 0 && $i % 3 == 0 ))
		then
			echo "FizzBuzz"

		elif (( $i % 3 == 0 ))
		then
			echo "Fizz"
		
		elif (( $i % 5 == 0 ))	
		then
			echo "Buzz"
		
		else
			echo $i
		fi
	done
}

fizzbuzz 100
