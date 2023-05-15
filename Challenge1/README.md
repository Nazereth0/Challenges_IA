## Chall 1 Programmation :

Contraintes: 

- Pas résolvable sans IA

But :
- Mettre en place un réseau de Deep learning
- Sortir un flag


Idées :

- Serveur netcat qui envoie des phrases à trous / questions / ... 
  Le joueur doit répondre dans un temps imparti ( pour empecher chatGPT ... ) et après 100-200 réponses correctes le serveur envoie le flag 

- Donner au joueur directement les questions ( mais beaucoup plus ~ 1000-3000 ) dans un zip, les numéroter et pour chaque question le joueur concatene la réponse qui génère le flag en format png, zip ou autre.
  par exemple si réponse 1 = True puis réponse 2 = False alors la réponse = 10 ( ou alors en héxadécimal ) et avec 1000 réponse en binaire ou pourra générer un fichier de 1ko (binaire) ou de 16ko (hexa) 
