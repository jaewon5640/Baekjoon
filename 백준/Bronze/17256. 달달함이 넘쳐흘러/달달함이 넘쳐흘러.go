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
	var ax, ay, az int
	var cx, cy, cz int
	fmt.Fscanln(reader, &ax, &ay, &az)
	fmt.Fscanln(reader, &cx, &cy, &cz)
	fmt.Fprintln(writer, cx-az, cy/ay, cz-ax)
}
