import shutil
import os
from datetime import datetime, timedelta


source = "/Users/Swarnali/Desktop/folder B/"
destination = "/Users/Swarnali/Desktop/folder A/"
files = os.listdir(source)

for i in files:
    m_time=os.path.getmtime(source+i)
    mod_time = datetime.fromtimestamp(m_time)
    current_time = datetime.now()
    tw_hrs_ago= current_time - timedelta(hours=24)
    print (tw_hrs_ago)
    if mod_time > tw_hrs_ago:
        shutil.move (source+i, destination)
