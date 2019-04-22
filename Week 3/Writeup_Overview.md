## Comparison Golden Section vs. Successive Quadratic

Both implementations were very clean and executed without issue. I think both methods are acceptable. 

### Pros:
Golden Section: Has a built in limiter that quarantines your results to a finite interval. This can be useful when trying to find a local min/max.

Quadratic: Unlike the Golden Section you don't technically need to plot the original function to understand how to bound the problem to search a specific area. You could initialize your guesses and the algorithm should find the correct solution. 

### Cons:

Golden Section: Need to define an area to search which means you already have to plot the function and have a graphical representation of the model, and if you have the ability to graph the function you have the ability to do a 'min'/'max' search in a program such as excel, so in my opinion it kind of defeats the point of the exercise.

Quadratic: No cons identified during testing. I'm sure the algorithm could get itself into trouble with equations that are much more obscure then the one we were tasked with developing the algorithm for.

### Overal
I think the golden section is a more useful algorithm as it could be coded to identify multiple local minima/maxima along an obscure function, and although this requires additional coding could be quite useful
