import sys
import os
import analytics
j = 0
for i in sys.argv:
    if ".json" in i:
        print(i)
        analytics.analytics(sys.argv[j-1], i)
        break
    else:
        pass
    j += 1
os.remove(i)