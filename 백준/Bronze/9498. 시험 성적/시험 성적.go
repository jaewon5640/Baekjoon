package main

import "fmt"

func main() {
	var score uint8
	fmt.Scan(&score)
	if score >= 90 {
		fmt.Println("A")
	} else if score < 90 && score >= 80 {
		fmt.Println("B")
	} else if score < 80 && score >= 70 {
		fmt.Println("C")
	} else if score < 70 && score >= 60 {
		fmt.Println("D")
	} else {
		fmt.Println("F")
	}
}
