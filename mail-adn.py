import smtplib
import csv
from random import shuffle

def distribution():
    famille=[]
    l1=[]
    with open("liste.csv", 'r') as fichier:
      liste = csv.reader(fichier)
      for el in liste:
          famille.append(el)
    shuffle(famille)
    for i in range(len(famille)):
        if i !=len(famille)-1:
            l1.append([famille[i][0],famille[i+1]])
        else:
            l1.append([famille[i][0],famille[0]])
    assert len(l1)==len(famille)
    return(l1)

def envoyer_mail(personne_cadeau, receveur):
    sender = "Asso <asso@adn-bzh.org>"
    
    message = f"""\
Subject: Pere Noel Secret
To: {receveur}
From: {sender}

Oh oh oh ! Le pere Noel te charge d'offrir un cadeau a {personne_cadeau}. En esperant que la magie de Noel puisse t'influencer dans tes idees..."""

    with smtplib.SMTP("", 587) as server:
        server.login("", "")
        server.sendmail(sender, receveur, message)

if __name__ == "__main__":
    liste_famille = distribution()
    for el in liste_famille:
        envoyer_mail(el[0], el[1][1])
