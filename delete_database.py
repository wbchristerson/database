import json

# Double-clicking this file will open a window confirming that the user wishes
# to delete all entries in the database. If the user responds with any of 'y',
# 'Y', 'yes', 'Yes', or 'YES', then all database entries will be deleted and
# the database will be replaced with an empty list. If the user responds with
# anything else, the proposed deletions will be canceled. A final status
# statement will show up along with a request to close the window by pressing
# 'enter'.

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


