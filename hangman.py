import time
import getpass
print """

                  _______  _        _______  _______  _______  _
        |\     /|(  ___  )( (    /|(  ____ \(       )(  ___  )( (    /|
        | )   ( || (   ) ||  \  ( || (    \/| () () || (   ) ||  \  ( |
        | (___) || (___) ||   \ | || |      | || || || (___) ||   \ | |
        |  ___  ||  ___  || (\ \) || | ____ | |(_)| ||  ___  || (\ \) |
        | (   ) || (   ) || | \   || | \_  )| |   | || (   ) || | \   |
        | )   ( || )   ( || )  \  || (___) || )   ( || )   ( || )  \  |
        |/     \||/     \||/    )_)(_______)|/     \||/     \||/    )_)








             }-----{+} Made with LOVE by kutaygs =) {+}-----{
            }--------{+} kutayyavuz03@hotmail.com {+}--------{
         }-----{+} Program python dilinde yapilmistir. {+}-----{




  """


name = raw_input("Ismin nedir? ")
print"""
"""
print "Selam, " + name, "hadi oynamaya baslayalim!"
print """
"""
time.sleep(1)
print "Basla..."
time.sleep(0.5)
print "Tahmin edilecek kelime ne olsun? "
word = getpass.getpass("Yazdiktan sonra enter'e bas...")
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print char,
        else:
            print "_",
            failed += 1
    if failed == 0:
        print """
Kazandin!!!"""
        break
    print
    guess = raw_input("Bir harf tahmin et : ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print """Yanlis
"""
        print "Hala", + turns, 'hakkin var!'
        if turns == 0:
            print """Kaybettin...
"""
