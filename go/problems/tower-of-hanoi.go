package main

import "fmt"

func main() {
	var towerB, towerC []int

	towerA := []int{2, 3, 4}

	fmt.Println(towerA, towerB, towerC)
	moveBlocks(3, &towerA, &towerC, &towerB)
	fmt.Println(towerA, towerB, towerC)
}

func moveBlocks(n int, src *[]int, destination *[]int, interim *[]int) {
	if n > 0 {
		moveBlocks(n-1, src, interim, destination)
		moveFirstBlock(src, destination)
		moveBlocks(n-1, interim, destination, src)
	}
}

func moveFirstBlock(src *[]int, destination *[]int) {
	*destination = append([]int{(*src)[0]}, (*destination)...)
	*src = (*src)[1:]
}
