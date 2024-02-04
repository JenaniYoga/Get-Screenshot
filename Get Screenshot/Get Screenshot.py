import pyscreenshot as sc
import time

time.sleep (5)

k=sc.grab()

k.save('Sample_Screenshot.png')

k.show()