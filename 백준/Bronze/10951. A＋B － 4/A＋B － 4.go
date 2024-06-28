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
	var a, b int
	for {
		v, _ := fmt.Fscanln(reader, &a, &b)
		if v != 2 {
			break
		}
		fmt.Fprintln(writer, a+b)
	}
}
