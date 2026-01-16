import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter

# ========= SETTINGS =========
iq_file = "data/sample.sdriq"
fs = 6000               # IQ sample rate (Hz) for radar sample
dtype = np.int32        # SDRangel sdriq packed 24-bit in int32
audio_fs = 12000        # output audio sample rate
N = 0                   # 0 = use full file
# ============================

def lowpass(x, cutoff, fs, order=5):
    b, a = butter(order, cutoff/(fs/2), btype="low")
    return lfilter(b, a, x)

# Read sdriq as int32 interleaved IQ
raw = np.fromfile(iq_file, dtype=dtype)
I = raw[0::2].astype(np.float32)
Q = raw[1::2].astype(np.float32)
x = I + 1j * Q

if N > 0:
    x = x[:N]

# FM demod using phase difference
phase = np.angle(x[1:] * np.conj(x[:-1]))

# Low-pass filter the demodulated signal (audio-ish)
audio = lowpass(phase, cutoff=2000, fs=fs, order=5)

# Resample (simple)
# Make ratio close; this is basic method for now
ratio = int(audio_fs / fs)
if ratio > 1:
    audio = np.repeat(audio, ratio)

# Normalize to int16
audio = audio - np.mean(audio)
audio = audio / (np.max(np.abs(audio)) + 1e-9)
audio_int16 = (audio * 32767).astype(np.int16)

wavfile.write("output.wav", audio_fs, audio_int16)
print("Saved output.wav")
