package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	n := 0
	fmt.Fscanln(reader, &n)
	factorialNum := 1
	for i := 1; i <= n; i++ {
		factorialNum *= i
	}
	fmt.Fprintln(writer, factorialNum)
}
