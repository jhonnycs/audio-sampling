# audio-sampling
Experimento de gravação e reamostragem de voz em Python (4kHz, 8kHz, 16kHz)

## Sumário

- [Sobre a atividade](#sobre-a-atividade)
- [Como executar](#como-executar)


## Sobre a atividade
A atividade é da disciplina processamento digital de sinais. Ela consiste no seguinte:

Gravar 3 amostras de voz falando uma frase. Uma amostra deve ter 4 kHz; outra amostra deve ter 8 kHz; outra, 16 kHz.

Depois de gravar as amostras, devemos transformas as amostras de 4 kHz e de 16 kHz em 8 kHz e comparar elas.

Comparamos as amostras gravadas com as amostras originais, e dizemos qual a diferença.

### Resultados
Depois de fazer as gravações, essas foram as constatações:

#### 4 kHz original
O áudio em 4 kHz original apresentou uma qualidade extremamente baixa. O áudio ficou extremamente abafado.

#### 8 kHz original
O áudio em 8 kHz fica um pouco mais claro. Ele ainda é abafado, mas é levemente mais compreensível.

#### 16 kHz original
O áudio em 16 kHz já é extremamente claro. Dá pra entender com mais clareza o que está sendo dito; não é abafado.

#### 8 kHz vindo de 4 kHz
Apesar de ser em 8 kHz, o áudio está bastante semelhante ao 4 kHz original. Bastante abafado, não muito claro. Não se assemelha ao 8 kHz original.

#### 8 kHz vindo de 16 kHz
Se assemelha ao áudio em 8 kHz. Está levemente menos abafado que o áudio original em 8 kHz, mas bastante parecido.

## Como executar

Para rodar, clone ou baixe o repositório, e dentro da pasta do projeto, prossiga.

### Bibliotecas
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

### Rodando o projeto

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
