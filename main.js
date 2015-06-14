#!/usr/bin/env node

function fizzbuzz (top) {
	console.log("top: ", top)
	for (var i = 1; i <= parseInt(top); i++) {
		if (i%3 == 0 && i%5 == 0) {
			console.log('fizzbuzz')
		} else if (i%3 == 0) {
			console.log('fizz')
		} else if (i%5 == 0) {
			console.log('buzz')
		} else {
			console.log(i)
		}
	}
}

fizzbuzz(process.argv[2])
