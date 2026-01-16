# SDR-FM-Demodulation
SDR project: FM demodulation using Python (FFT + filtering). 
## Goals
- Load recorded IQ samples
- Plot FFT spectrum
- Extract (demodulate) FM audio signal

## Tools
- Python 3.11
- NumPy, Matplotlib

## Progress
-  Day 1: Setup Python + Git + GitHub 
-  Day 2: FFT spectrum plot from IQ file
-  Day 3: FM demodulation pipeline
-  Day 4: Save audio (.wav) output

## How to Run (will update)
```bash
pip install numpy matplotlib
python fft_spectrum.py
```
## Output
![FFT Spectrum](spectrum.png)
## FM Demodulation
The IQ sample used was a SDRangel radar`.sdriq` recording (not broadcast FM).
So the generated `output.wav` may contain noise/tones instead of music.
This output is included to validate the FM demodulation pipeline.

Generated audio output:
- outputs/output.wav
