"""_summary_

What is Iterable?
    
    An object capable of returning its members or elements one at a time. Examples of iterables are all sequence types
        (such as list, str, and tuple) and  non sequence types (dict, file objects).
        Common iterables in Python include lists, strings, and dictionaries. 
        So, if you have a list of numbers or a string of text, you can go through each item or character one by one.
    
    The magic behind iterables is the __iter__ method. 
        When an object has this method, Python knows it can fetch items from it sequentially.
    
    In loops given block of code is repeated. 
    Example: A sequence of elements seperated by comma(,).
    
        [10,11,12,13] --> List
    
        10,11,12,13 --> the members or elements of list.
        In 1st iteration, when the loop starts to run for the first time "10" is going to be returned.
        In 2nd iteration, when the loop starts to run for the second time "11" is going to be returned.
        In 3rd iteration, when the loop starts to run for the third time "12" is going to be returned.
        In 4th iteration, when the loop starts to run for the fourth time "13" is going to be returned.
        
    When we are going to use iterables, the loop is going to run as many times as number of elements in the data.

        if "n" elements are in the data structure then loop iterates "n" times.
        
    For making posssible to iteration the element needs to be qualified as member and it may differ data types.
    
    One of the most common ways to access elements in an iterable is using a for loop. 
        It's like saying, "For each chocolate in the box, take it out and enjoy it!"
    
    Characteristics of Iterables:
        1. Sequential Access: An iterable provides items one by one, in sequence. 
            This does not necessarily mean it has to be a sequential data structure like a list; 
            even sets and dictionaries are iterable in Python, despite being unordered collections.

        2. Membership: An object needs to have multiple members to be iterable. 
            For instance, a number like "5" is not iterable, but a list like "[1, 2, 3, 4, 5]" is.

        3. Protocol Adherence: In Python, for an object to be considered iterable, 
            it must implement the "__iter__()" method, which returns an iterator. 
            This is known as adhering to the iterable protocol.

        Common Python Iterables:
        
        Lists: e.g., [1, 2, 3, 4]
        Strings: e.g., 'Hello' (You can iterate over each character)
        Tuples: e.g., (1, 2, 3, 4)
        Dictionaries: e.g., {'a': 1, 'b': 2} (You can iterate over keys, values, or key-value pairs)
        Sets: e.g., {1, 2, 3, 4}
        Files: When you open a file in Python, you can iterate over its lines.
        
        Relation to Iterators:
        It's worth noting the difference between "iterable" and "iterator". 
            An iterable is an object that can be looped over, but to do the looping, it uses an iterator. 
            An iterator is an object that keeps state and produces the next value when you call the next() function 
            on it. All iterators are iterables, but not all iterables are iterators.

        Example: Consider this simple loop:

        for i in [1, 2, 3, 4]:
            print(i)
            
        Here, the list [1, 2, 3, 4] is an iterable. When the for loop starts, Python internally obtains an 
            iterator from this list. For each iteration of the loop, the next() function is called on 
            this iterator to get the next value until there are no more items left.


        Common examples of iterables in programming include:
        
        Lists: A list in Python or an array in many other programming languages is an iterable. 
            You can loop through its elements using a for loop, extracting each item one at a time.

            my_list = [1, 2, 3, 4, 5]
            for item in my_list:
                print(item)
            
        Strings: Strings are sequences of characters, and you can iterate through the characters in a string.

        my_string = "Hello"
        for char in my_string:
            print(char)
            
        Tuples: Tuples are similar to lists but are immutable, meaning their elements cannot be changed after 
            creation. They are also iterables.

        my_tuple = (1, 2, 3)
        for item in my_tuple:
            print(item)
            
        Dictionaries: In Python, dictionaries are iterables where you can iterate through keys, 
            values, or key-value pairs.

        my_dict = {'a': 1, 'b': 2, 'c': 3}
        for key, value in my_dict.items():
            print(key, value)
            
        Sets: Sets are collections of unique elements and are also iterable.

        my_set = {1, 2, 3}
        for item in my_set:
            print(item)
            
        In essence, an iterable provides a way to access its elements sequentially, 
        making it a crucial concept in loops and various other programming constructs.
        
        Understanding iterables is crucial because they form the backbone of loops and many 
        other operations in Python, allowing you to work with collections of items efficiently and intuitively.

"""

# Using For Loop 

# Iterating a List

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print("Iteration using List and the members are ",item)
    
print("********************************************************************************\n")
    
# Iterating a String

my_string = "Hello"
for char in my_string:
    print("Iteration using String and the characters are ",char)
    
print("********************************************************************************\n")
    
# Iterating a Tuple

my_tuple = (1, 2, 3)
for item in my_tuple:
    print("Iteration using Tuple and the members are ",item)
    
print("********************************************************************************\n")

# Iterating a Dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Iteration using List are {key} : {value}")  
    
print("********************************************************************************\n")
    
# Iterating a set

my_set = {1,2,3}
for item in my_set:
    print("Iteration using set and the members are ",item)
