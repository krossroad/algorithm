package problems

//ContainsString foo
func ContainsString(test string, source string) bool {
	return looper(test, source, 0, 0, false)
}

func looper(needle string, haystack string, i int, j int, acc bool) bool {
	needleLen := len(needle)
	hayLen := len(haystack)

	if i >= needleLen || j >= hayLen {
		return acc
	}

	if needle[i] == haystack[j] {
		return looper(needle, haystack, i+1, j+1, true)
	}

	if !acc {
		j++
	}

	return looper(needle, haystack, 0, j, false)
}
