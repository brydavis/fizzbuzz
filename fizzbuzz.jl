#!/usr/bin/env julia 

function fizzbuzz(top)  
	for i in range(1,int(top))
		s = ""
		s *= (i % 3 == 0)? "Fizz" : ""
		s *= (i % 5 == 0)? "Buzz" : ""
		s == ""? println(i): println(s)
	end
end


fizzbuzz(ARGS[1])
