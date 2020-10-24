import random
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager
fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
for font in fonts:
    print(font)
#input('rtc')
# missing: f3000, f370, f590, FA80, FC00  '0A80', '0900
def changefont(fontname):
    print('setting font ',fontname)
    matplotlib.rcParams.update({  # Use mathtext, not LaTeX
        'text.usetex': False,
        'font.family': fontname,
  #      'font.serif': 'cmr10',
#        'mathtext.fontset': 'cm',
        # Use ASCII minus
 #       'axes.unicode_minus': False,
    })

#('0590',10,'Arial')
# start of unicode block, how many chars in alphabet, font (if needed)
alphabets = [ ('4E70',100,'PingFang'),#CHinese
            ('FB1D',30,'Arial'), #hebrew
             ('0679',70,'GeezaPro'),#arabic
             ('2600',100,None),
             ('260',60,None),
             ('2650',60,None),
             ('1F600',60,None),
             ('F15',10,None)]

fig1, ax1 =  plt.subplots()
#fig2, ax2 =  plt.subplots()
plt.ion()
plt.axis('off')

for hexval,n,fontname in alphabets:
    v = int(hexval,base=16)
    print('alphabet',v,'length',n)
    if fontname is not None:
        changefont(fontname)
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
 #   break
plt.savefig('door.ps', format='ps')
plt.show()
#input('rtc')
