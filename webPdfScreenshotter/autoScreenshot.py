import pyautogui
import time
from datetime import datetime

start=datetime.now()
pageTotal=int(input("Number of page to be sc: "))
print("Change to window with the image you want to capture in 3 seconds")
time.sleep(3)
for loop in range(pageTotal):
    image=pyautogui.screenshot(region=(1048,354, 798, 1030))
 
    with open(str(loop+1)+'.png','wb') as f:
        image.save(f)
    pyautogui.leftClick(1317,328)
    # time.sleep(1)
end=datetime.now()
print("runtime:")
print(end-start)

import img2pdfConverter