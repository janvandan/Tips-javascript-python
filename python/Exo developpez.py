# https://python.developpez.com/exercices/?page=Les-chaines-de-caracteres#Rechercher-un-caractere-particulier-dans-une-chaine-de-caracteres

import unittest

def EstCarChaine(c: str, chaine: str) -> bool:
    for i in chaine:
        if i == c:
            return True
    return False

def AjoutCarChaine(c: str, chaine: str) -> str:
    res=''
    for i in chaine:
        if res != '':
            res += '*' + i
        else:
            res += i
#    return res
    return c.join(chaine)

def InverseChaine(chaine: str) -> str:
    res = ''
    for i in range(len(chaine),0,-1):
        res += chaine[i-1]
    return res

class ExercicesPython(unittest.TestCase):

    def test_EstCarChaine(self):
        self.assertEqual(False,EstCarChaine('a',"hello"))
        self.assertEqual(True,EstCarChaine('e',"hello"))

    def test_AjoutCarChaine(self):
        self.assertEqual('g*a*s*t*o*n',AjoutCarChaine('*','gaston'))

    def test_InverseChaine(self):
        self.assertEqual('bulgroz',InverseChaine('zorglub'))
        self.assertEqual('kivardnavnaj',InverseChaine('janvandravik'))

if __name__ == '__main__':
    unittest.main()