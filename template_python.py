"""Docstring d'une ligne décrivant brièvement ce que fait le programme.

Template issu de https://python.sdv.univ-paris-diderot.fr/15_bonnes_pratiques/

Usage:
======
    python nom_de_ce_super_script.py argument1 argument2

    argument1: un entier signifiant un truc
    argument2: une chaîne de caractères décrivant un bidule
"""

__authors__ = ("Johny B Good", "Hubert de la Pâte Feuilletée")
__contact__ = ("johny@bgood.us", "hub@pate.feuilletee.fr")
__copyright__ = "MIT"
__date__ = "2030-01-01"
__version__= "1.2.3"

import module_interne
import module_interne_2

import module_externe

UNE_CONSTANTE = valeur
UNE_AUTRE_CONSTANTE = une_autre_valeur


class UneSuperClasse():
    """Résumé de la docstring décrivant la classe.

    Description détaillée ligne 1
    Description détaillée ligne 2
    Description détaillée ligne 3
    """

    def __init__(self):
        """Résumé de la docstring décrivant le constructeur.

        Description détaillée ligne 1
        Description détaillée ligne 2
        Description détaillée ligne 3
        """
        [...]

    def une_méthode_simple(self):
        """Docstring d'une ligne décrivant la méthode."""
        [...]

    def une_méthode_complexe(self, arg1):
        """Résumé de la docstring décrivant la méthode.

        Description détaillée ligne 1
        Description détaillée ligne 2
        Description détaillée ligne 3
        """
        [...]
        return un_truc


def une_fonction_complexe(arg1, arg2, arg3):
    """Résumé de la docstring décrivant la fonction.

    Description détaillée ligne 1
    Description détaillée ligne 2
    Description détaillée ligne 3
    """
    [...]
    return une_chose


def une_fonction_simple(arg1, arg2):
    """Docstring d'une ligne décrivant la fonction."""
    [...]
    return autre_chose


if __name__ == "__main__":
    # ici débute le programme principal
    [...]
