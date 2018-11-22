from class_spectra import Spectrum
import argparse
import astropy
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="This program reads a given SDSS"+
                                 " spectrum and plots it.",
                                 usage="read_SDSS.py <filename>")

parser.add_argument('-f', '--file',
                    help="File to open.")
args = parser.parse_args()


spec1 = Spectrum(args.file)


plt.figure()
x = spec1.wavelength
y = spec1.flux

plt.plot(x,y)

plt.xlabel("Wavelength")
plt.ylabel("Flux")
plt.show()
