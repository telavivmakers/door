import random
import matplotlib.pyplot as plt
# missing: f3000, f370, f590, FA80, FC00  LET THE CHINESE FLOW

alphabets = ['2600','260','2650','1F600','0900','0A80','F15']
lengths =  [  100,   60,     60,     60,    50,     50,      50]
vals = [int(a,base=16) for a in alphabets]

fig1, ax1 =  plt.subplots()
#fig2, ax2 =  plt.subplots()
plt.ion()
plt.axis('off')


for v,n in zip(vals,lengths):
    print('alphabet',v,'length',n)
    for i in range(v,v+n):
        x,y = random.random(),random.random()
        angle = random.random()*360
        print(i,hex(i),chr(i))
#        fig1.clf()
        # fig1.text(.5, .5, chr(i), fontsize=16, rotation=angle)
        # fig1.show()
#        plt.show()
        try:
            fig1.text(x, y, chr(i), fontsize=16, rotation=angle)
            plt.draw()
            plt.pause(0.01)
        except RuntimeWarning as e:
            print(i,hex(i),'not avail',e)
    #    input('rtc')
plt.savefig('door.ps', format='ps')
plt.show()
