# Question 1#
import re

#a
Information = {
    "Name" : "MorrisMarvellous",
    "Course" :"Computer Science",
    "Level" : "200",
    "Gender" : "Male"
}
pattern= r"l"
Matching_value= [value for value in Information.keys() if re.search(pattern ,value)]

#b
replaced_dict = {}
for key,value in Information.items():
    replaced_value = re.sub(pattern, "g",value)
    replaced_dict[key] = replaced_value
    print (replaced_dict)

    #Question 2#

Set = "Male132"
print (Set[::-1])
print (Set[0:4])