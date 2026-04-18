                          #data-types
          #mutable                          #imutable
'''Mutable-Datatype
-------------------------
In Python, a mutable data type is one whose internal state or contents can be changed after it has been created
without changing its identity.

--->example
Common Mutable Types
---------------------
Lists: [1, 2, 3] (can append or change items).

Dictionaries: {"a": 1} (can add or update keys).

Sets: {1, 2, 3} (can add or remove elements).

Bytearrays: A mutable version of bytes.
---> immutable data type
----------------------------
An immutable data type is one whose content or state cannot be changed after it is created.
If you attempt to modify an immutable object, Python creates a completely new object in memory with the new value.

Key Characteristics
Fixed State: Once defined, the data inside the object cannot be altered.

Hashable: Because they don't change, most immutable types can be used as keys in a dictionary.

Memory Behavior: Modifying the variable results in a new memory address (id()).

---> examples Common Immutable Types
------------------------
Numbers: int, float, complex.

Integer (int)
---------------
Whole numbers without decimals.

Example: x = 10

Behavior: If you do x += 1, Python creates a new integer object 11 and assigns x to it.
The original 10 remains unchanged in memory until cleared.

2. Float (float)
------------------
Numbers containing a decimal point.

Example: price = 99.99

Behavior:
Changing the price to 100.0 doesn't modify the existing float; it allocates a new space in memory for the new value.

3. Complex (complex)
--------------------
Numbers with a real and an imaginary part (denoted by j).

Example: z = 3 + 5j

Behavior: You cannot modify z.real or z.imag directly. To change the value, you must redefine the entire variable.

indexing: this is used to get the pitcular substring,item from string list and tuple by calling with index postion
---------
syntax: variable_name[index_position]

any = "python is a programming language"
print(any[11])

concatenation: a plus + symbol will acts as different ways,if we are adding 2 integers its acts like adding in other cases such
--------------  list,string and tuplr its act like concatenation
so = "live"
im = "life"
print(so + im)

String or str: String is a collection of charecters that are enclosed in ('',"",''' ''') it is immutable datatype
--------------
"hello" (you cannot change a single character in-place).

---------
Tuples: (1, 2, 3) (a fixed sequence).
--------
Frozen Sets: An immutable version of a set.
-----------
Bytes: Immutable sequences of single bytes.
---------
'''
# String Methods :
'''String or str: String is a collection of charecters that are enclosed in ('',"",''' ''') it is immutable datatype
   --------------
"hello" (you cannot change a single character in-place).

split() method breaks a string into a list of substrings based on a specified delimiter (defaulting to any whitespace).
syntax:  variable_name.split()
syntax :  varaiable_name.replace("old string","new string"))
-------
py = "bhargav kiran mutchu"
print(py.replace("bhargav kiran mutchu","Mbk"))
print(py)
 
strip() : 
splity="Bhargav Kiran Mutchu"
print(splity.strip("Kiran Mut"))

join() :

spl="Bhargav Kiran Mutchu"
print("__".join(spl ))
output: B__h__a__r__g__a__v__ __K__i__r__a__n__ __M__u__t__c__h__u

lower()
spl="Bhargav Kiran Mutchu"
print(spl.lower( ))

upper()
spl="Bhargav Kiran Mutchu"
print(spl.upper( ))
output:BHARGAV KIRAN MUTCHU

replace()

'''
num = int(input(" please enter a number"))
print(f"{num} is a even number")
      


















