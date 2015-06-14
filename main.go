package main

import "fmt"

func main() {
	fizzbuzz(100)
}

func fizzbuzz(top int) {
	for i := 0; i < top+1; i++ {
		if i%5 == 0 && i%3 == 0 {
			fmt.Println("FizzBuzz")
		} else if i%3 == 0 {
			fmt.Println("Fizz")
		} else if i%5 == 0 {
			fmt.Println("Buzz")
		} else {
			fmt.Println(i)
		}
	}
}
