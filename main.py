'''
Programme testant si une chaine de caractères est un palyndrome ou pas.
'''

#### Fonction secondaire


def ispalindrome(s):

    # votre code ici``

    '''
    Retourne si la chaine de caractères est un palyndrome ou pas.

    Args:
        s: chaine de caractères.

    Returns:
        True: Booléen, si s es un palyndrome.
        False: Booléen, si s n'est pas un palyndrome.
    '''
    n = len (s)
    l = ''
    for i in range(n-1, -1, -1):
        l += s[i]
    if l == s:
        return True

    return False

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    '''
    Fonction principale
    '''

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
