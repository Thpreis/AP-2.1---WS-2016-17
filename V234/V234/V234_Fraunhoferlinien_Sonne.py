#identify Fraunhoferlines in solarspectrum
#this cell is independent from all others to be executed in Visual Studio for using the cusor

import matplotlib.pyplot as plt
import numpy as np

def comma_to_float(valstr):
    return float(valstr. decode("utf-8"). replace(',', '.'))

lamb_ds, inten_ds= np. loadtxt('Sonnedireckt2811.txt', skiprows=17,
    converters= {0:comma_to_float,1:comma_to_float},
    comments= '>', unpack= True)

plt. plot(lamb_ds, inten_ds, label = "Direkektes Sonnenlicht")
plt. title('direktes Sonnenspektrum')
plt. xlabel('Wellenlaenge / nm')

plt. ylabel('Intensitaet / b.E.')
plt. ylim((0, 70000))
plt. xlim((200, 900))
plt. title('Fraunhoferlinien')
plt. xlabel('Wellenlaenge / nm')
plt. ylabel('Intensitaet / b.E.')
plt. legend()
plt. grid()
plt. ylim((0, 70000))
plt. xlim((200, 900))
plt. savefig("Plots/Himmel_m_o_G.pdf", format= "pdf")
plt. savefig("plots/Fraunhofer.pdf", format= "pdf")
plt.show()
#plt.close()