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
	fmt.Fscan(reader, &n)
	for i := 1; i <= 9; i++ {
		fmt.Fprintln(writer, n, "*", i, "=", n*i)
	}
}
