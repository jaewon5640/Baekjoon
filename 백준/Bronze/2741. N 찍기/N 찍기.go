package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n uint32
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscanln(reader, &n)
	for i := uint32(1); i <= n; i++ {
		fmt.Fprintln(writer, i)
	}
}
