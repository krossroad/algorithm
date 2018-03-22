package problems

import (
	"algorithm/go/stack"
)

var openingBraces = map[string]string{
	"(": ")",
	"{": "}",
	"[": "]",
}

var closingBraces = map[string]string{
	")": "(",
	"}": "{",
	"]": "[",
}

func BalancedBraces(inputStr string) bool {
	holder := stack.Construct(len(inputStr))

	for _, str := range inputStr {
		literal := string(str)

		if _, ok := openingBraces[literal]; ok {
			holder.Push(literal)
		}

		if openingBrace, ok := closingBraces[literal]; ok {
			if holder.Peek() == openingBrace {
				holder.Pop()
				continue
			}

			return false
		}
	}

	return holder.IsEmpty()
}
