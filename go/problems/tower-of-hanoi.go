package problems

func MoveBlocks(n int, src *[]int, destination *[]int, interim *[]int) {
	if n > 0 {
		MoveBlocks(n-1, src, interim, destination)
		moveFirstBlock(src, destination)
		MoveBlocks(n-1, interim, destination, src)
	}
}

func moveFirstBlock(src *[]int, destination *[]int) {
	*destination = append([]int{(*src)[0]}, (*destination)...)
	*src = (*src)[1:]
}
