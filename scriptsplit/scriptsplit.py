import re
import os

cdir = os.path.dirname(__file__)
script_file = open(os.path.join(cdir, 'megamind.txt'), 'r')
script = script_file.read()
script_file.close()



pars = re.split(r'\n\n+', script, maxsplit=0)  # The 'r' at the start of the pattern string 
# designates a python "raw" string which passes through backslashes without change
d = {}



# Source: https://stackoverflow.com/questions/57273215/how-to-parse-movie-script-in-a-dictionary
for p in pars:
    # Capture the name (anchored to the beginning of line and all capitals)
    # and the rest of the paragraph - (.*)
    regex = re.search(r'^([A-Z]+ [A-Z]+|[A-Z]+)(.*)', p, re.S + re.M)

    if not regex:  # Avoid calling group() on null results
        continue

    name, txt = regex.group(1, 2) 

    # Each sentence as a list item
    if name in d:
        d[name] += txt.strip().split('\n')
    else:
        d[name] = txt.strip().split('\n')


print(d.keys()) # Check which names are captured
print(d['MASTER MIND']) # check that the main character's lines are captured



# Regex guide: https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/
