import sys


fail = False

for modl in ["numpy","matplotlib","matplotlib.pyplot","pandas","seaborn","jupyter","sklearn"]:

    try:
        print("import %s"%modl)
        __import__(modl)
    except:
        print("FAILURE -- You don't have %s installed!"%modl)
        fail = True

    

print("")
if not fail:
    print("SUCCESS -- You have all the modules you need!")
