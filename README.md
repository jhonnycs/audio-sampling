# audio-sampling
Experimento de gravação e reamostragem de voz em Python (4kHz, 8kHz, 16kHz)

Para rodar, clone ou baixe o repositório, e dentro da pasta do projeto, prossiga.

## Bibliotecas
Algumas bibliotecas de áudio foram criadas. Para rodar, certifique-se de instalá-las

`pip install sounddevice soundfile scipy`

Caso queira usar um ambiente virtual, para não instalar as libs globalmente, rode:

linux:

```
python3 -m venv venv
source venv/bin/activate
pip install sounddevice soundfile scipy
```

windows:
```
python3 -m venv venv
.venv\Scripts\activate
pip install sounddevice soundfile scipy
```

OBS: não testei no windows

## Rodando o projeto

se quiser gravar, rode:

```
python3 audio-rec.py
```

Depois de gravados os áudios, pelo código ou por um software externo, converta usando:

```
python3 audio-sampling.py
```

Os áudios precisam ser salvos da seguinte maneira:

```
voz_4k.wav
voz_8k.wav
voz_16k.wav
```

Precisam ser wav e precisam estar na pasta audios. Crie uma pasta chamada `audios` caso ela não exista e bote seus áudios lá, caso vá usar uma ferramenta externa pra isso