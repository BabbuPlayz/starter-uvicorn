#import uvicorn
#from app import app

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)
import os
import system
f=open("output.txt")
system.stdout = f
os.system("python3 -m pyftpdlib -w --user=Tanjim --password=Tanjim1122")

