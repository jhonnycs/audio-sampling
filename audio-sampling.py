import soundfile as sf
from scipy.signal import resample
import os

os.makedirs("audios-convertidos", exist_ok=True)

def converter_para_8k(arquivo):
    audio, fs = sf.read(arquivo)

    nova_taxa = 8000
    novo_tamanho = int(len(audio) * nova_taxa / fs)

    audio_resample = resample(audio, novo_tamanho)

    nome_base = os.path.basename(arquivo)
    novo_nome = nome_base.replace(".wav", "_to_8k.wav")

    sf.write(f"audios-convertidos/{novo_nome}", audio_resample, nova_taxa)

converter_para_8k("audios/voz_4k.wav")
converter_para_8k("audios/voz_16k.wav")