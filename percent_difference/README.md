The average IQ-testing difference between two different tests for one individual is 10.9 and the difference 
between two different individuals are 17.1(both in percent, correlation 0.6 between tests and standard deviation 15).
The percent difference is defined for a pair a and b as  100\*abs(a-b)/((a+b)/2). 
To avoid division by zero and other problems in code(the probability for that in this case is very low)
it is best to use 200*(|a-b|)+E)/(((|a|+|b|)/2)+E) where || is absolute value and E=10^-10 for example.
[https://en.wikipedia.org/wiki/Relative_change#Domain]. 

The Fortran program uploaded is mostly for illustration it is probably not much faster in this case.
