package main

import "fmt"

func main() {
	var a, b rune
	fmt.Scan(&a)
	fmt.Scan(&b)

	fmt.Println(a * (b % 10))
	fmt.Println(a * ((b % 100) / 10))
	fmt.Println(a * (b / 100))
	fmt.Println(a * b)
}
