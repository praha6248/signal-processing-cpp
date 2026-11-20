import sys
sys.path.append("../build")  # katalog z modułem cmake_example
import cmake_example as lib
wave =lib.sawtooth(3,2,100,2)
lib.plot(wave)
dft_wave=lib.DFT(wave)
lib.plot(dft_wave)
lib.plot(lib.IDFT(wave))