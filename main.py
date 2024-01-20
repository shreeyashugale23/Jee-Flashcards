import os
import random
import json
import sys, signal

subj=input("enter phy or maths:\n")

def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    with open(subj+".json", "w") as write_file:
        json.dump(json_dict, write_file, indent=1)
    temp=input("Press any key to continue...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

path=".\\"+subj+"\\"
spath=".\\"+subj+"soln\\"
json_dict={}
Q=[]
with open(subj+".json", 'r') as openfile:
    json_dict = json.load(openfile)
for key in json_dict:
    if json_dict[key]==0:
        Q.append(key)

for i in range(len(Q)):
    d=random.choice(Q)
    img_path=path+d
    soln_path=spath+"soln-"+d
    command="\"C:\\Program Files\\nomacs\\bin\\nomacs.exe\""+" -t "+soln_path+" -t "+img_path
    temp_dump_for_pause=os.popen(command).read()
    Q.remove(d)
    json_dict[d]=1

print("All files have been read pls run reset.py")
