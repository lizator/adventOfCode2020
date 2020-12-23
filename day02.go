package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Enter input: ")

	res := 0
	i := 0
	for i < 1000 {
		inp, _ := reader.ReadString('\n')
		ls := strings.Split(inp, " ")
		min, _ := strconv.Atoi(strings.Split(ls[0], "-")[0])
		max, _ := strconv.Atoi(strings.Split(ls[0], "-")[1])
		letter := ls[1][0]
		pass := ls[2]
		first, second := false, false
		if pass[min-1] == letter{
			first = true
		}
		if pass[max-1] == letter{
			second = true
		}
		if first != second {
			res++
		}
		i++
	}

	fmt.Println(res)

}
