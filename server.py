#import uvicorn
#from app import app

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)
import os
import sys
import time

f=open("/var/task/outputs.txt")
sys.stdout = f
os.system("pip install pyftpdlib --target /pythonpackages")
time.sleep(10)
print("slept 10 secs")
time.sleep(10)
print("slept 20 secs")
time.sleep(10)
print("slept 30 secs. hopefully installation done coz starting FTP with --user=Tanjim --password=Tanjim1122" )
os.system("python3 -m pyftpdlib -w --user=Tanjim --password=Tanjim1122")

