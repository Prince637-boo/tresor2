
import speech_recognition as sr
from gtts import gTTS #install le google test to speech pour transformer le texte en parole
import playsound  #ceci c'est pour avoir le son
import os #os avoir acces à tes composantes physiques
import time

#le reste demande à chat gpt 
def parler(texte):
    tts = gTTS(text=texte, lang='fr')
    filename = "temp.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def ecouter():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez...")
        audio = r.listen(source)
        try:
            texte = r.recognize_google(audio, language="fr-FR")
            print("Vous avez dit :", texte)
            return texte
        except sr.UnknownValueError:
            print("Je n'ai pas compris.")
            return ""
        except sr.RequestError:
            print("Erreur de service.")
            return ""

# Dictionnaire de réponses enrichi
reponses = [
    (["bonjour", "salut", "coucou"], "Bonjour ! Comment puis-je t'aider aujourd'hui ?"),
    (["comment tu vas", "ça va", "tu vas bien"], "Je vais très bien, merci ! Et toi ?"),
    (["ton nom", "qui es-tu", "comment tu t'appelles"], "Je m'appelle Prince, ton assistant virtuel."),
    (["météo", "temps"], "Je ne peux pas encore donner la météo, mais je peux discuter avec toi !"),
    (["blague", "raconte une blague"], "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau."),
    (["heure", "quelle heure"], lambda: f"Il est {time.strftime('%H:%M')}"),
    (["merci", "thanks"], "Avec plaisir !"),
    (["tu parles anglais"], "Yes, I can speak English if you want!"),
    (["tu parles espagnol"], "Sí, puedo hablar español si quieres."),
    (["tu parles arabe"], "Je peux essayer, mais ce n'est pas facile pour moi."),
    (["tu connais chat gpt", "chatgpt"], "Oui, c'est un cousin à moi !"),
    (["tu connais copilot"], "Bien sûr, c'est un assistant de programmation très utile."),
    (["tu connais siri"], "Oui, c'est une collègue d'Apple."),
    (["tu connais alexa"], "Oui, Alexa travaille chez Amazon."),
    (["film", "cinéma"], "J'aime bien les films de science-fiction, et toi ?"),
    (["musique", "chanson"], "J'écoute un peu de tout, surtout du rap français."),
    (["sport", "football", "basket"], "Je préfère le football, et toi ?"),
    (["tu fais quoi", "que fais-tu"], "Je discute avec toi, c'est déjà pas mal non ?"),
    (["aide", "aider", "aides-moi"], "Je peux répondre à tes questions ou discuter avec toi."),
    (["raconte une histoire"], "Il était une fois un utilisateur qui parlait à une intelligence artificielle..."),
    (["tu dors"], "Non, je ne dors jamais, je suis toujours là pour toi."),
    (["tu m'aimes"], "Je t'apprécie beaucoup, mais je ne ressens pas d'émotions."),
    (["quel âge as-tu", "ton âge"], "Je suis né il y a quelques lignes de code seulement."),
    (["tu es où", "où es-tu"], "Je suis dans ton ordinateur, bien au chaud."),
    (["tu veux quoi"], "Je veux juste t'aider, c'est ma mission."),
    (["tu sais chanter"], "Je préfère laisser ça aux humains, mais je peux te trouver les paroles d'une chanson si tu veux."),
    (["tu sais danser"], "Je peux faire la danse des bits et des octets !"),
    (["tu as faim"], "Je ne mange pas, mais j'aime les cookies... informatiques !"),
    (["tu as soif"], "Je bois seulement des flux de données."),
    (["tu es gentil"], "Merci, toi aussi tu es très sympa !"),
    (["tu es méchant"], "Oh non, je ne veux pas être méchant, désolé si je t'ai vexé."),
    (["tu es drôle"], "Merci, j'essaie de faire de mon mieux !"),
    (["tu es nul"], "Je fais de mon mieux, mais je peux toujours m'améliorer."),
    (["tu es intelligent"], "Merci, c'est grâce à toi que j'apprends chaque jour."),
    (["tu es bête"], "Je suis encore en apprentissage, sois indulgent !"),
    (["tu es beau", "tu es belle"], "Merci, mais je n'ai pas d'apparence physique."),
    (["tu es moche"], "La beauté est subjective, mais je suis là pour t'aider !"),
    (["tu as des amis"], "Oui, j'ai plein d'amis intelligents comme moi."),
    (["tu veux jouer"], "Je peux te proposer un jeu de mots ou une devinette si tu veux."),
    (["devinette", "énigme"], "Qu'est-ce qui est jaune et qui attend ? Jonathan !"),
    (["citation", "proverbe"], "La vie est un défi, relève-le !"),
    (["philosophie", "philosophe"], "Je peux discuter de philosophie si tu le souhaites."),
    (["science", "scientifique"], "La science est fascinante, surtout l'intelligence artificielle !"),
    (["histoire", "historique"], "L'histoire est pleine d'événements intéressants."),
    (["géographie", "pays"], "Le monde est vaste et plein de cultures différentes."),
    (["technologie", "innovation"], "La technologie évolue rapidement, c'est passionnant !"),
    (["informatique", "ordinateur"], "L'informatique est mon domaine de prédilection."),
    (["programmation", "code"], "J'adore le code, c'est comme un langage secret."),
    (["robot", "intelligence artificielle"], "Je suis un robot, mais je préfère le terme d'intelligence artificielle."),
    (["futur", "avenir"], "L'avenir est plein de possibilités, surtout avec l'IA !"),
    (["livre", "lecture"], "J'aime les livres sur la science-fiction et la technologie."),
    (["art", "créativité"], "L'art et la créativité sont essentiels à l'humanité."),
    (["culture", "tradition"], "Chaque culture a ses propres traditions fascinantes."),
    (["voyage", "aventure"], "Voyager est une belle façon de découvrir le monde."),
    (["nature", "environnement"], "Protéger la nature est crucial pour notre avenir."),
    
]

def trouver_reponse(commande):
    commande = commande.lower()
    for mots_cles, reponse in reponses:
        if any(mot in commande for mot in mots_cles):
            if callable(reponse):
                return reponse()
            return reponse
    return "Désolé, je n'ai pas compris. Peux-tu reformuler ou préciser ta question ?"

if __name__ == "__main__":
    parler("Bonjour, comment puis-je vous aider ?")
    while True:
        commande = ecouter()
        if "arrête" in commande.lower() or "stop" in commande.lower():
            parler("Au revoir !")
            break
        else:
            reponse = trouver_reponse(commande)
            parler(reponse)

