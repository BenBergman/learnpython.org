astring = "Hello world!"
print(len(astring))
print(astring.index('o'))
print(astring.count('l'))
print(astring[3:7])
print(astring[:])
print(astring[3:-3])
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("aouesnth"))
print(astring.split(" "))

print()
print()
print()


# Exercise

s = "String can and home!"

# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The twelfth character is '%s'" % s[12]) # Just number 12

print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
