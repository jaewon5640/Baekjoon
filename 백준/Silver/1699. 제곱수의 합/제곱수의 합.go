package main

import (
	"container/list"
	"fmt"
)

type Queue struct {
	v *list.List
}

func NewQueue() *Queue {
	return &Queue{list.New()}
}

func (q *Queue) Push(v interface{}) {
	q.v.PushBack(v)
}

func (q *Queue) Pop() interface{} {
	front := q.v.Front()
	if front == nil {
		return nil
	}

	return q.v.Remove(front)
}

func (q *Queue) IsEmpty() bool {
	return q.v.Len() == 0
}

func main() {
	num := 0
	fmt.Scan(&num)
	queue := NewQueue()
	queue.Push(num)
	cnt := 1
	visit := make([]bool, num+1)

OuterLoop:
	for {
		if queue.IsEmpty() {
			break
		}

		tempQueue := NewQueue()
		for !queue.IsEmpty() {
			squareN := 1
			x := queue.Pop().(int)

			for (squareN * squareN) <= x {
				node := x - (squareN * squareN)

				// 탈출조건
				if node == 0 {
					break OuterLoop
				}

				if !visit[node] {
					tempQueue.Push(node)
					visit[node] = true
				}

				squareN++
			}
		}
		queue = tempQueue
		cnt++
	}

	fmt.Println(cnt)
}
