import os
import csv

rootdir = 'elib/'

file_names = []

for subdir, dirs, files in os.walk(rootdir):
    for f in files:
        file_names.append(os.path.join(subdir, f))

with open('content_table.csv', 'w') as csvfile:
    fwriter = csv.writer(csvfile, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    fwriter.writerow(['Name', 'Description', 'Path'])

    for path in file_names:
        fwriter.writerow(['', '', path])

