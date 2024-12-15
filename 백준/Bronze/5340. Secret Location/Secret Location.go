package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	x1, _ := reader.ReadString('\n')
	x2, _ := reader.ReadString('\n')
	x3, _ := reader.ReadString('\n')
	x4, _ := reader.ReadString('\n')
	x5, _ := reader.ReadString('\n')
	x6, _ := reader.ReadString('\n')

	fmt.Fprintf(writer, "Latitude %d:%d:%d\n", len(strings.TrimSpace(x1)), len(strings.TrimSpace(x2)), len(strings.TrimSpace(x3)))
	fmt.Fprintf(writer, "Longitude %d:%d:%d\n", len(strings.TrimSpace(x4)), len(strings.TrimSpace(x5)), len(strings.TrimSpace(x6)))
}
