#import uvicorn
#from app import app

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)
import os
import sys
f=open("/var/task/output.txt")
sys.stdout = f
os.system("python3 -m pyftpdlib -w --user=Tanjim --password=Tanjim1122")

