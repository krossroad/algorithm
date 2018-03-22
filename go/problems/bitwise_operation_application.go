package problems

func AddWithoutPlusOperator(a int, b int) int {
	for b != 0 {
		carry := a & b
		a = a ^ b
		b = carry << 1
	}

	return a
}

func SubtractionWithooutMinusOperator(a int, b int) int {
	for b != 0 {
		carry := (^a) & b
		a = a ^ b
		b = carry << 1
	}

	return a
}

func UniqueElement(coll []int) int {
	sum := 0

	for _, num := range coll {
		sum = sum ^ num
	}

	return sum
}
