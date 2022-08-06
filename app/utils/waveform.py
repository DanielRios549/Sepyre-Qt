from numpy import frombuffer, linspace
from wave import open
from pathlib import Path
from matplotlib.pyplot import plot, savefig


def WaveForm(folder: str, file: str, size: int = 16):
    spf = open(f'{file}.wav', 'r')

    # Extract Raw Audio from WAV File
    signal = spf.readframes(-1)
    signal = frombuffer(signal, f'Int{size}')
    frames = spf.getframerate()
    spf.close()

    time = linspace(0, len(signal) / frames, num=len(signal))

    # Create PEAKS folder
    peaks = Path(f'{folder}/__PEAKS__')

    if peaks.is_dir() is False:
        peaks.mkdir(0o775, False, False)

    # Save image
    plot(time, signal)
    savefig(f'{peaks}/{file}.png')
