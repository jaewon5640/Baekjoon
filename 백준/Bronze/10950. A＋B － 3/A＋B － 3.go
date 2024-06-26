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

	t := 0
	fmt.Fscanln(reader, &t)

	for i := 0; i < t; i++ {
		var a, b int
		fmt.Fscanln(reader, &a, &b)
		fmt.Fprintln(writer, a+b)
	}
}
