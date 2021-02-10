#Afin de comprendre comment cela fonctionne, entrez le code suivant dans votre éditeur de texte et sauvegardez le fichier sous le nom file-output.py
#Personnellement, j'utiliserais le nom Exercice_1.py

#Lorsque vous lancez le programme ci-dessus, la méthode open indique à votre ordinateur de créer un nouveau fichier helloworld.txt dans le répertoire où se trouve file-output.py. 
#(pour nous, Exercice_1.py)
# Le paramètre ‘wb‘ spécifie que le fichier ouvert est destiné à l’écriture (write) de contenus par Python.
#Dans le programme ci-dessus, f est un objet de type fichier (file object) et open, write et close sont des méthodes sur fichier (file methods). En d’autres termes, “open”, 
# “write” et “close” agissent sur l’objet f qui dans le cas présent est défini comme un fichier ‘.txt’.
#Source : https://programminghistorian.org/fr/lecons/travailler-avec-des-fichiers-texte
#Après avoir obtenu l'erreur a bytes-like object is required, not 'str', j'ai recherché des solutions et j'ai trouvé de changer wb par w, cela fonctionne
#Source : stackoverflow
f = open('helloworld.txt','w')
f.write("hello world")
f.close()
