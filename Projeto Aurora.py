import gtts
from playsound import playsound
import speech_recognition as sr
import webbrowser

# esse comando para você escolher entre os microfones disponíveis, caso tenha mais de um e opte por mudar:
# print(sr.Microphone().list_microphone_names())


# 1. variável 'rec' recebe o reconhecedor de voz para ser identificada por ela
rec = sr.Recognizer()


# 2. Faz a captação do audio e o transforma em texto para ser analisado. A assistente responde pelo nome "Aurora"
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)  # comando para reduzir ruído
    print('\033[35mAguardando comando...\033[m')
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language='pt-BR')

    # 3. Caso o comando seja reconhecido, a assistente retorna com a saudação
    if texto in 'Aurora':
        teste = 'Olá Ranilo! Em que posso ajudar?'
        f1 = gtts.gTTS(teste, lang='pt-br')
        f1.save('f1.mp3')
        playsound('f1.mp3')

    # 4. Repete-se o processo de captação e análise. A assistente aguarda o comando "pesquisa para mim por" + termo de pesquisa
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)  # comando para reduzir ruído
            print('\033[35mAguardando comando...\033[m')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')

    # 5. Caso o comando seja reconhecido, será feita a pesquisa no Google usando o navegador
        if 'pesquisa para mim por' in texto:
            search_term = texto.split("por")[-1]
            print('Pesquisar por\033[35m' + search_term)
            url = "https://www.google.com/search?q=" + search_term
            webbrowser.get().open(url)
            retorno = ("Isso foi o que eu encontrei por " + search_term + 'no google')
            f2 = gtts.gTTS(retorno, lang='pt-br')
            f2.save('f2.mp3')
            playsound('f2.mp3')
