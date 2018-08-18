
import matplotlib.pyplot as plt
import numpy as np


def comma_to_float(valstr):
    return float(valstr. decode("utf-8"). replace(',', '.'))
#import measuremnts direct sunlight
#lamb_ds wavelength in nm
#inten_ds intensity in counts
lamb_ds, inten_ds= np. loadtxt('laser2811.txt', skiprows=17,
    converters= {0:comma_to_float,1:comma_to_float},
    comments= '>', unpack= True)
plt. plot(lamb_ds, inten_ds, color="green")
plt. title('Spektrum eines Gruenen lasers')
plt. xlabel('Wellenlaenge / nm')
plt. ylabel('Intensitaet / b.E.')
plt. ylim((0, 25000))
plt. xlim((200, 900))
plt. savefig("Plots/Laserspektrum.pdf", format= "pdf")
plt.close()