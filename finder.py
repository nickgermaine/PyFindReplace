import simplejson as json
import fileinput, sys, os


project = input("Enter project directory (ex. C:/Users/Me/Projects/NewProject): ")

def replaceAll(file, findexp, replaceexp):
    for line in fileinput.input(file, inplace=1):
        if findexp in line:
            line = line.replace(findexp, replaceexp)
        sys.stdout.write(line)

'''
    I open my language json and replace instances of the english terms with a dynamic php conditional
    json looks like {"Administration": {"en": "Administration", "de": "De Term"}, etc..
'''

with open("lang.json", "r") as file:
    cont = json.loads(file.read())
    for k in cont:
        tr = cont[k]["en"]

        rp = "<?php echo ($_GET['lang'] == 'de') ? $translations['" + tr + "']['de'] : $translations['" + tr + "']['en']; ?>"

        files = os.listdir(project)
        for file in files:
            if ".php" in file:
                newfile = os.path.join(project, file)
                replaceAll(newfile, tr, rp)