package main

import "fmt"

var M, N int

func dfs(m1 [][]bool, m2 [][]bool, x, y int) {
	if x < 0 || x >= M || y < 0 || y >= N {
		return
	}

	if !m1[x][y] || m2[x][y] {
		return
	}
	m2[x][y] = true

	dfs(m1, m2, x+1, y)
	dfs(m1, m2, x-1, y)
	dfs(m1, m2, x, y+1)
	dfs(m1, m2, x, y-1)
}

func main() {
	var T, K int
	fmt.Scan(&T)

	for i := 0; i < T; i++ {
		fmt.Scan(&M, &N, &K)

		m1 := make([][]bool, M)
		m2 := make([][]bool, M)
		for i := range m1 {
			m1[i] = make([]bool, N)
			m2[i] = make([]bool, N)
		}

		for i := 0; i < K; i++ {
			var x, y int
			fmt.Scan(&x, &y)
			m1[x][y] = true
		}

		cnt := 0
		for i := 0; i < M; i++ {
			for j := 0; j < N; j++ {
				if m1[i][j] && !m2[i][j] {
					dfs(m1, m2, i, j)
					cnt++
				}
			}
		}
		fmt.Println(cnt)
	}
}
