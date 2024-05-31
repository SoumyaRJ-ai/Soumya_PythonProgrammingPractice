# The algorithm for URLifying a given string involves iterating through the characters of the 
# string and replacing spaces with “%20”.

str = "Urlify me to see me as a URL not as a string"
str = str.strip()
urlified = str.replace(" ", "%20")
print(urlified)