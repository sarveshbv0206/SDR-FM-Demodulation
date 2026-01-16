import numpy as np
import matplotlib.pyplot as plt

# ===== SETTINGS =====
filename = "data/sample.sdriq"
fs = 6000  # from SDRangel table: 6k sample rate
dtype = np.int32
header_bytes = 0
N = 131072
# ====================

raw = np.fromfile(filename, dtype=dtype)

# SDRangel .sdriq often stores 24-bit IQ packed in 32-bit signed int:
# I, Q, I, Q ... interleaved
I = raw[0::2].astype(np.float32)
Q = raw[1::2].astype(np.float32)
x = I + 1j * Q

# limit samples
x = x[:N] if len(x) >= N else x

# FFT with window
w = np.hanning(len(x))
X = np.fft.fftshift(np.fft.fft(x * w))
P = 20 * np.log10(np.abs(X) + 1e-12)

f = np.linspace(-fs/2, fs/2, len(P))

plt.figure()
plt.plot(f, P)
plt.title("FFT Spectrum (.sdriq)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.tight_layout()
plt.savefig("spectrum.png", dpi=200)
plt.show()
