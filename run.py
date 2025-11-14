import os
print("press q to exit")
os.system("yolo detect predict model=best.pt source=0 show=True conf=0.65")