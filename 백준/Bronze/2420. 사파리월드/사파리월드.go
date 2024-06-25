package main

import (
	"fmt"
	"math"
)

func main() {
	var n, m float64
	fmt.Scan(&n, &m)
	fmt.Print(int64(math.Abs(n - m)))
}
