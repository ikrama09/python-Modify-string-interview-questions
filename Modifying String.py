'''1. upper()
Given the string:
text = "hello world"
Print the string in uppercase.'''
from dataclasses import replace

a = "Hello, world!"
print(a.upper())

'''2. lower()
Given: text = "PYTHON IS AWESOME"
Convert the string into lowercase.'''

b = "PYTHON IS AWESOME"
print(b.lower())

'''3. title()
Given:
text = "my name is ikrama"
Convert the first letter of every word to uppercase.'''

c = "my name is ikrama"
print(c.title())

'''4. capitalize()
Given:
text = "python programming"
Capitalize only the first letter of the sentence.'''

d = "python programming"
print(d.capitalize())

'''5. strip()
Given:
text = "     Hello Python     "
Remove the extra spaces from both sides.'''

e = "     Hello Python     "
print(e.strip())

'''6. lstrip()
Given:
text = "      Coding"
Remove spaces only from the left side.'''

f = "       Coding"
print(f.lstrip())

'''7. rstrip()
Given:
text = "Python      "
Remove spaces only from the right side.'''

g = "Python     "
print(g.rstrip())

'''8. replace()
Given:
text = "I like Java"
Replace "Java" with "Python".'''

h = "I like java"
print(h.replace("java" , "Python"))

'''9. replace() (Multiple Occurrences)
Given:
text = "apple apple mango apple"
Replace every "apple" with "banana".'''

i = "apple apple mango apple"
print(i.replace("apple" , "banana"))

'''10. split()
Given:
text = "Python Java C++ JavaScript"
Split the string into a list of words.'''

j = "Python Java C++ JavaScript"
print(j.split())

'''11. split() Using a Custom Separator
Given:
text = "red,green,blue,yellow"'''

k = "red,green,blue,yellow"
print(k.split(","))

'''12. Chained Methods
Given:
text = "   python programming   "
Remove extra spaces and convert the text to uppercase.'''

l = "   python programming   "
print(l.strip().upper())

'''13. Chained Methods
Given:
text = "  HELLO PYTHON  "
Remove spaces and convert the text into lowercase'''

m = "  HELLO PYTHON  "
print(m.strip().lower())

'''14. replace() + upper()
Given:
text = "good morning"
Replace "morning" with "evening" and convert the entire string to uppercase.'''

n = "good morning"
print(n.replace("morning","evening").upper())

'''15. Real-Life Practice Question

Given:
email = "    IKRAMA123@GMAIL.COM    "
Perform the following operations:
Remove extra spaces.
Convert the email to lowercase.
Replace "gmail" with "outlook".'''

email = "    IKRAMA123@GMAIL.COM    "
print(email.strip().replace("gmail","outlook").lower())

'''Bonus Challenge (Interview Level)
Given:
text = "   python,is,fun,to,learn   "
Perform all of the following:
Remove extra spaces.
Convert the string to uppercase.
Replace commas with spaces.
Split the string into a list.'''

text = "   python,is,fun,to,learn   "
print(text.strip().upper().replace(","," ").split())


