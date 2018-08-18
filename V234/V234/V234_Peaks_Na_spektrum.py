import matplotlib.pyplot as plt
import numpy as np

def comma_to_float(valstr):
    return float(valstr. decode("utf-8"). replace(',', '.'))


##IX.2 Auswertung des Natriumspektrums
#file "Natriumlinks2811" ist required containing data for sodium spectrum
#import data for sodium spectrum(total)
# lamb_sod wavelenght of spectrum in nm
#inten_sod intensity in counts
lamb_sod, inten_sod= np. loadtxt('data_Na/Natriumlinks2811.txt', skiprows=17,
    converters= {0:comma_to_float,1:comma_to_float},
    comments= '>', unpack= True)

#RebAbb9
#plot whole sodium spectrum
plt. plot(lamb_sod, inten_sod)
plt. title('Natriumspektrum starke Intensiaet')
plt. xlabel('Wellenlaenge / nm')
plt. ylabel('Intensitaet / b.E.')
plt. yscale('log')#logarithmic scale
plt. ylim((1, 80000))
plt. xlim((350, 800))
#plt.savefig("Plots/Natriumspektrum_gesamt.pdf", format= "pdf")
plt.show()
plt.close()

##IX.2 Auswertung des Natriumspektrums
#file "Natriumlinks2811" ist required containing data for sodium spectrum





##IX.2 Auswertung des Natriumspektrums
#file "Natriumlinks2811" ist required containing data for sodium spectrum
#RebAbb10
#plot sodium spectrum in range 300 to 540 nm
plt. plot(lamb_sod, inten_sod)#In case xlim does not work, correct input data
plt. title('Natriumspektrum geringer Intensitaet kurze Wellenlaengen')
plt. xlabel('Wellenlaenge / nm')
plt. ylabel('Intensitaet / b.E.')
plt. yscale('log')#logarithmic scale
plt. ylim((0, 60000))
plt. xlim((350, 540))
plt.show()
plt.close()
#plt.savefig("Plots/Natriumspektrum_kurz.pdf", format= "pdf")

#RebAbb11
#plot sodium spectrum in range 600 to 850 nm
plt. plot(lamb_sod, inten_sod)#In case xlim does not work, correct input data
plt. title('Natriumspektrum geringer Intensitaet lange Wellenlaengen')
plt. xlabel('Wellenlaenge / nm')
plt. ylabel('Intensitaet / b.E.')
plt. yscale('log')#logarithmic scale
plt. ylim((0, 60000))
plt. xlim((600, 850))
#plt.savefig("Plots/Natriumspektrum_lang.pdf", format= "pdf")
plt.show()
plt.close()

lamb_ds, inten_ds= np. loadtxt('Sonnedireckt2811.txt', skiprows=17,
    converters= {0:comma_to_float,1:comma_to_float},
    comments= '>', unpack= True)

plt. plot(lamb_ds, inten_ds, label = "Direkektes Sonnenlicht")
plt. title('Fraunhoferlinien')
plt. xlabel('Wellenlaenge / nm')
plt. ylabel('Intensitaet / b.E.')
plt. legend()
plt. grid()
plt. ylim((0, 70000))
plt. xlim((200, 900))
plt. savefig("plots/Fraunhofer.pdf", format= "pdf")
plt.show()
#plt.close()