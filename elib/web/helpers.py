#this file contains a set of helper functions
import os 
import csv


    
rootdir = 'Content/'    
def create_file_db(rootdir):
    file_names = []
    for subdir, dirs, files in os.walk(rootdir):
        for f in files:
            file_names.append(os.path.join(subdir, f))
    with open('content_table.csv', 'w') as csvfile:
        fwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fwriter.writerow(['description','keywords','location'])
        for path in file_names:
            print(path)
            if "content.csv" in path:
                print("yaya")
                pass 
            else:
                print("yes")
                fwriter.writerow(['','', path])


root="Content/"

def create_file_dir(root):
    #recursively creates a file containing the contents(files or dirs) of each single directory
    folder_contents=os.listdir(root)
    filename=root+"content.csv"
    with open(filename,'w') as csvfile:

        fwriter=csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fwriter.writerow(['Content List'])
        for path in folder_contents:
            if path=="content.csv":
                pass
            else:
                fwriter.writerow([path])

    try:
        for path in folder_contents:
            create_file_dir(root+path+'/')
    except:
        return
'''
def populate_db():
    #helps populate the db when give a base directory
    with open('content_table.csv', 'r') as csvfile:
        freader = csv.reader(csvfile)
        File.objects.all().delete()
        for row in freader:
            print(row)
            filesave=File(Description=row[0], keywords=row[1], location=row[2])
            filesave.save()
'''
if __name__ == "__main__":
    #run updates
    create_file_db(rootdir)
    #populate_db()
    create_file_dir(root)




        
    