"""_summary_

A string is a fundamental data type in most programming languages. 
It represents a sequence of characters. 
These characters can be letters, numbers, symbols, or whitespace. 
The concept of a string is similar to a word, sentence, or paragraph in human language.

Here are some key points about strings:

    1. Immutable: In many programming languages, like Python, strings are immutable. 
        This means once a string is created, its content cannot be changed. 
        However, you can create a new string by combining or modifying existing strings.

    2. Enclosed in Quotes: Strings are typically enclosed in quotes.
        Depending on the language, you might use single (`'`), double (`"`), or even triple 
        (`'''` or "" " in Python) quotes to define a string.

        string1 = 'Hello, world!'
        string2 = "Hello, world!"

    3. Escape Sequences: Strings can contain special characters, which are represented using escape sequences.
        For example, in many languages, `\n` represents a newline, and `\t` represents a tab.

    
        string_with_newline = "Hello,\nworld!"
    

    4. Operations: You can perform various operations on strings. Common operations include 
        concatenation (joining two strings), slicing (extracting a portion of a string), and
        various transformation methods like converting to uppercase or lowercase.


        string1 = "Hello"
        string2 = "World"
        
        combined_string = string1 + " " + string2  # "Hello World"


    5. Indexed: The characters in a string are indexed, usually starting from zero. 
        This allows you to access individual characters or slices of the string using this index.

    
        greeting = "Hello"
        first_char = greeting[0]  # This will be 'H'
   

    6. Multiline Strings: Some languages, like Python, allow for the definition of multiline strings.
        In Python, this is done using triple quotes.

    Strings are versatile and are used in almost every aspect of programming, from representing simple
        messages to being the primary data type for text processing tasks.
        
    Strings have a rich set of operations and methods available.
    
Operations
    
    1. Concatenation: Combining two strings together.

        first_name = "John"
        last_name = "Doe"
        full_name = first_name + " " + last_name  
        
        Output:  "John Doe"
        
    2. Length: Determining the number of characters in a string.

        length = len("Hello")  
        
        Output: 5

    3. Uppercase and Lowercase:

        "hello".upper()  
        
        Output: "HELLO"
        
        "HELLO".lower()  
        
        Output: "hello"

    4. Title Case:

        "hello world".title()

        Output: "Hello World"
        
    5. String Replacement:

        "Hello, world!".replace("world", "Python")  

        Output: "Hello, Python!"

    6. String Splitting: Converts a string into a list by splitting it based on a delimiter.

        "apple,banana,orange".split(",")  
        
        Output: ['apple', 'banana', 'orange']

    7. String Joining: Combines a list of strings into a single string.

        "-".join(['apple', 'banana', 'orange'])  
        
        Output: 'apple-banana-orange'
        
    8. String Stripping: Removes whitespace (or specified characters) from the beginning and end of a string.
        Related methods include rstrip() (to remove trailing whitespace) and lstrip() (to remove leading whitespace).

        "  Hello  ".strip()  
        
        Output: "Hello"

    9. Finding Substrings find(): Returns the index of the first occurrence of a substring or -1 if not found.

        "Hello, world!".find("world")  
        
        Output: 7
        
    10. rfind(substring, start, end): Returns the highest index where the substring is found. Returns -1 if not found.

        "hello world".rfind("l")  # 9
        
    10. Checking Start and End: Check if a string starts or ends with a certain substring.

        "Hello".startswith("Hel")  
        
        Output: True
        
        "Hello".endswith("lo")     
        
        Output: True
        
    11. Counting Substrings:

        "Hello, world, world!".count("world")  
        
        Output: 2
        
    12. String Slicing: Extracting parts of a string using indices.

        text = "Hello, world!"
        slice1 = text[7:12]  
        
        Output: "world"
        
    13. Character Testing: Check the character nature of the string.

        "12345".isdigit()     Output: True
        
        "hello".isalpha()     Output: True
        
        "hello123".isalnum()  Output: True
        
        "HELLO".isupper()     Output: True
        
        "hello".islower()     Output: True
        
        "   ".isspace()       Output: True

        "12345".isnumeric()   Output: True
        
        "3.14".isdecimal()    Output: False (because of the decimal point)
        
    14. String Centering: Place the string in the center of a field of a given width.

        "hello".center(11, '*')  Output: "***hello***"
        
    15. String Zfill: Pads the original string with zeros to fill a width.

        "42".zfill(5)           Output: "00042"
    
    16. String Partitioning: Splits the string at the first occurrence of the delimiter.

        "hello-world".partition("-")  
        
        Output: ('hello', '-', 'world')
        
    17. rpartition(separator): Like partition(), but searches for the last occurrence of the separator.

        "hello_world_python".rpartition("_")  
        
        Output : ("hello_world", "_", "python")
        
    18. 
        
    19. capitalize(): Returns a copy of the string with its first character capitalized and the rest lowercased.

        "hello".capitalize()    
        
        Output : "Hello"
        
    20. ljust(width, [fillchar]) and rjust(width, [fillchar]): 
            Return the string left-justified or right-justified in a string of length width, respectively. 
            Padding is done using the specified fillchar (default is whitespace).

        "hello".ljust(10, '-')  
        
        Output : "hello-----"
        
        "hello".rjust(10, '-')  
        
        Output : "-----hello"
     
    21. expandtabs([tabsize]): Replaces tab characters with the specified number of whitespaces. 
        Default tab size is 8.

        "hello\tworld".expandtabs(4)    Output :  "hello    world"

    22. swapcase(): Converts uppercase characters to lowercase and lowercase characters to uppercase.

        "HeLLo WoRLd".swapcase()  Output : "hEllO wOrlD" 
        
    23. encode(encoding='UTF-8',errors='strict'): Returns an encoded version of the string using the 
        specified encoding.

        "hello".encode('utf-8')  Output : b'hello'

    24. casefold(): Returns a case-folded version of the string, which can be used for caseless comparisons.

        "HELLO".casefold()  Output : "hello"   
        
        
    25. index(substring, start, end): Similar to find(), but raises a ValueError if the substring is not found.
        
        "hello".index("lo")  Output: 3
        
    26. 
    
    27. 
rindex(substring, start, end): Like rfind(), but raises a ValueError if the substring is not found.

python
Copy code
"hello world".rindex("l")  # 9
splitlines([keepends]): Splits the string at line breaks and returns a list of lines. If keepends is provided and True, line breaks are also included.

python
Copy code
"hello\nworld".splitlines()  # ["hello", "world"]
maketrans(x[, y[, z]]) and translate(table[, deletechars]): Create a translation table (with maketrans()) and then use it with translate() to replace certain characters.

python
Copy code
# Replace 'h' with 'j' and 'world' with 'morld'
trans = str.maketrans({"h": "j", "w": "m"})
"hello world".translate(trans)  # "jello morld"
isalnum(): Checks if all characters in the string are alphanumeric (either letters or numbers).

python
Copy code
"hello123".isalnum()  # True
isidentifier(): Checks if the string is a valid Python identifier (e.g., variable name).

python
Copy code
"hello_world".isidentifier()  # True
isprintable(): Checks if all characters in the string are printable or the string is empty.

python
Copy code
"hello".isprintable()  # True
"\t".isprintable()    # False
lstrip([chars]) and rstrip([chars]): Remove leading and trailing characters, respectively. If chars is provided, it specifies which characters to remove.

python
Copy code
"   hello   ".lstrip()  # "hello   "
rsplit(sep=None, maxsplit=-1): Similar to split(), but splits from the right.

python
Copy code
"hello world program".rsplit(" ", 1)  # ['hello world', 'program']
format(*args, **kwargs): Format the string by replacing placeholders with specified values.

python
Copy code
"{} world".format("Hello")  # "Hello world"
format_map(mapping): Format the string using a given mapping (like a dictionary).

python
Copy code
"{greeting} world".format_map({"greeting": "Hello"})  # "Hello world"
The above list, combined with the previously mentioned methods, gives a fairly comprehensive overview of string methods in Python. Strings are versatile and rich in functionality, enabling developers to handle text-based data efficiently.


isascii(): (Python 3.7+) Checks if all characters in the string are ASCII characters.

python
Copy code
"apple".isascii()  # True


"""

# Multiline String

multiline_string = """
   This is a string
   that spans multiple
   lines.
   """
   