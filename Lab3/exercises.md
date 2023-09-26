# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- *edit your response*
    The MObject is a concrete class. Because according to Python, abstract classes are designed to be extended through subclassing, as well as for supplying sepcific implementations for the abstract methods with the subclasses. A good indicator of abstract class will be a "@abstractmethod" decorator within the entire code. However, within oop.py, there is no such a decorator. Therefore, MObject is a concrete class.

1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- *edit your response*
	According to the provided link, it is a finalizer/destructor, and it is automatically called when an object is going to be destroyed. As this method is commented, it will not work, and therefore, will not affect either the Image class or its instances.
1. What class does Texture inherit from?
	- *edit your response*
	The Image class
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- *edit your response*
	It inherit the init constructor from Image, the getwidth(self) method, 
getHeight(self) method, getPixelColorR(self, x, y) method, getPixels(self) method, setPixelsToRandomValue(self) method, with attributes includes: m_width, m_height,m_colorChannels and m_Pixels.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- *edit your response*
	I think Inheritance is sufficient enough for Texture class for the most cases. Becauce inheritance allows us to create a specialized version of "Texture" as a subclass of "Image" with additional methods specific to the specialized type. This helps encapsulate the certain behavior while maintain the core functionality from the base class. Allows us to reuse the existing code and behavior, also promote the ability of Polymorphism, where we can use "Texture" objects as "image" objects when needed, which can be helpful for condition where you need to work with both classes without creating a new class or substance.

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- *edit your response*
       That's one of the best features about python, that even though you did not declare a constructor, python will help you create a default constructor. However, the default constructor does not have any attributes yet, which is also a good feature so that we can custom our own constructor later if needed, allow flexibility.
## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

*edit the code directly*  
 In Python, singletons are typically not inherently thread-safe because they can be accessed and modified by multiple threads concurrently. To ensure thread safety, additional measures such as using synchronization mechanisms like locks or carefully controlling object creation need to be implemented. The specific method used to create a singleton, whether it's through module-level variables, metaclasses, or decorators, can impact its thread safety.
