import sounddevice as sd
import soundfile as sf
import os
import time

duracao = 4
taxas = [4000, 8000, 16000]

os.makedirs("audios", exist_ok=True)

def wait_time():
    print("Fale em")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

for fs in taxas:
    print(f"\nGravando com taxa {fs} Hz")
    wait_time()
    print("Gravando...")

    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()

    nome = f"audios/voz_{fs//1000}k.wav"
    sf.write(nome, audio, fs)

    print(f"Arquivo salvo: {nome}")