import re
import pprint
import os

cdir = os.path.dirname(__file__)
script_file = open(os.path.join(cdir, 'megamind.txt'), 'r')
script = script_file.read()
script_file.close()

#print(script[2000:2200]) <- uncomment to make sure the script imported right

pars = re.split(r'\n\n+', script, maxsplit=0) #re.S + re.M) <- part of original code (link below) not sure why it was included?
d = {}

# Checking that the split works
print(pars[100])
print(len(pars))
print(pars[1825])

# Source: https://stackoverflow.com/questions/57273215/how-to-parse-movie-script-in-a-dictionary
for p in pars:
    # Capture the name (anchored to the beginning of line and all capitals)
    # and the rest of the paragraph - (.*)
    regex = re.search(r'^([A-Z]+):(.*)', p, re.S + re.M)

    if not regex:  # Avoid calling group() on null results
        continue

    name, txt = regex.group(1, 2) # FIXME: 'NoneType' object has no attribute 'group'
                                                                         # I think the regex search is bogged
                                                                         # Will just redo it on my own using the same logic

    # Each sentence as a list item
    if name in d:
        d[name] += txt.strip().split('\n')
    else:
        d[name] = txt.strip().split('\n')

pprint.pprint(d)  

# FIXME: this code may not work exactly as intended once regex line is fixed,
#  since there are parts of the script with no 'speaker' (it's just describing
#  the scene). Just make sure to test that this is accounted for

# Regex guide: https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/
