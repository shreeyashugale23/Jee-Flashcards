import os
import json

def cleardict(subj):
    path=".\\"+subj
    files=os.listdir(path)
    json_dict={}
    for i in files:
        json_dict[i]=0
    with open(subj+".json", "w") as write_file:
        json.dump(json_dict, write_file, indent=1)
        
cleardict(input("enter phy or maths to clear:\n"))
temp=input("Press any key to continue...")
