import datetime
import os
import sys

ENV='C:\\Users\\Aliaz\\Desktop\\aicup2022\\Envs\\AiCup01\\Scripts\\activate'
KERNEL="C:\\Users\\Aliaz\\Desktop\\aicup2022\\Kernel\\src\\main.py"
a=datetime.datetime.now().time()
os.makedirs("logs\\"+str(a).replace(":","").replace(".",""), exist_ok=True)
r=1
if len(sys.argv)<=1:
    r=int(input("enter repeat count: ").strip())
else:
    r=int(sys.argv[1])
settings=[]
maps=[]
clients=[]
for (dirpath, dirnames, filenames) in os.walk("settings"):
    settings.extend(filenames)
for (dirpath, dirnames, filenames) in os.walk("maps"):
    maps.extend(filenames)
for (dirpath, dirnames, filenames) in os.walk("clients"):
    clients.extend(filenames)

for i in range(1,r+1):
    for s in settings:
        for m in maps:
            ls1=[]
            for c1 in clients:
                ls1.append(c1)
                for c2 in clients:
                    if c2 not in ls1 :
                        path=f"logs\{str(a).replace(':','').replace('.','')}\{str(i)}\{s[:-5]}\{m[:-5]}\{c1[:-3]}_{c2[:-3]}"
                        os.makedirs(path, exist_ok=True)
                        pyc=f"python {KERNEL} -p1 ..\..\..\..\..\..\clients\{c1} -p2 ..\..\..\..\..\..\clients\{c2} --setting ..\..\..\..\..\..\settings\{s} --log .\ --map ..\..\..\..\..\..\maps\{m}"
                        os.system(f'cmd /c "call {ENV} && cd {path} && {pyc} && move Clients\logs\* .\ "')
