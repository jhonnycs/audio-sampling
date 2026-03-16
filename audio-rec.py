import sounddevice as sd
import soundfile as sf
import os

duracao = 3
taxas = [4000, 8000, 16000]

os.makedirs("audios", exist_ok=True)

for fs in taxas:
    print(f"\nGravando com taxa {fs} Hz")
    print("Fale a frase...")

    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()

    nome = f"audios/voz_{fs//1000}k.wav"
    sf.write(nome, audio, fs)

    print(f"Arquivo salvo: {nome}")