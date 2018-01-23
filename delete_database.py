import json

#tag = []
#topic = []
#source = []
#statement = []
#sol_no_late = []
#sol_late = []
#note = []

#s = {'tags': tag, 'topics': topic, 'sources': source, 'statements': statement,
#     'sol_no_latex': sol_no_late, 'sol_latex': sol_late, 'notes': note}
#s = [{'hello': 'hola', 'welcome': 'bienvenidos'}, {'bread':'aran', 'water':'uisce'}]

confirm = input("\nAre you sure that you want to delete all entries from " \
                + "storage? (y/n) ")

if (confirm in ('y', 'Y', 'yes', 'Yes', 'YES')):
    s = []
    with open('database/resources.json', 'w') as fp:
        json.dump(s, fp)
    fp.close()
    print("\nAll data entries have been deleted.\n")
else:
    print("\nCanceling request for deletion of all entries.\n")

input("\n\nPress the enter key to exit.")


