#Program Name: collection.py
# Purpose of a program:
# Create a collection of authors and the years they died using a dictionary.
# Print the collection in the following format:

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889



authors = {

    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"}

#item functions of a dictionary returns a pair of data (key, value)
#Use two loop variables to retrieve each pair of data in the dictionary authors.
#for key, date in authors.items():
#    print("%s" % key + " dies in " + "%s." % date)

for item in authors.items():
        print(item[0] + ', ' + item[1])
