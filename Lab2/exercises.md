# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*Edit your responses here*
	Yes, in Python, the names of dictionary and list methods correlate well with their action, and also easy to understand. For example, in dictionary class, the dict.keys() meaning the action of obtaining all keys, the dict.values() describes the action of retrieving all values. Another example will be list.append(x), where the name "append" precisely describes the action of adding an element to the end of the list.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)
*Edit your response here*

	Dictionary is used for mapping hashable keys to arbitrary values and are display using curly braces or the dict() constructor, while list is mutable sequences, used to store collections of homogenous items, and are defined using square brackets or the list() constructor.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Edit your response here*
Yes, list allows for random access, we can access any element by specifying its index using square brackets. Let's say the there is a list named "Alist", we can access the element at its index 7 using "Alist[7]"

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Edit your response here*
Pros:
-Allows code to be reused, which reducing the need to customize a specialized structure.
-More flexible, allowing us to work with different data sets without restrictio
-Code looks less complex in general, as we can work with different data type, a lot of codes could be simplified into more concised codes.

Cons:
1.Memory Usage: Multiple data type in use can increase memory usage
2.Potentially impact the performance, it may not be as efficient as data structrure that are specialized. And it slowers the overall operation for type conversions.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*Edit your responses here*
I think the simple the function named, the easy for us to understand, for example,requests.get(url, params=None, **kwargs), I think it is a well named functions in the Requests module, from the word "get", the params "url", we know that it is taking a specific url, or optional arguments that request takes, to retreive thcontent from the webpage.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*Edit your responses here*
The resolve_redirects(resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs) takes 9 parameters


3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*Edit your responses here*
**kwargs is a special syntax used to pass a variable-length list of keyword argument to a function. It allows us to pass a dictionary of keyword-value pairs to a function, where the keys are treated as the argument names, and the values are the corresponding argument values. The good side of **kwargs is provides flexibility because it allows us to pass any number of keyword arguments to a function.It is powerful when the function need to accept a variable set of parameters. It also makes the function clear of what each argument represents in the function call.
However, it creates difficulties to validate input parameters since any keyword can be passed; it also make code harder to understanding when there are many optional keyword arguments.
 
4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


*Edit your responses here*
Arguments that are set to "None" meaning it is default value, it allows flexibility for users to choose whether or not to provide specific values when making requests.Also for future extension of specific method, with the argument in "None", the existing argument will not lose its place within the method, while adding new arguments into the method. Besides "None", you can also set data to "False","True".
