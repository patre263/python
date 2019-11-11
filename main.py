import argparse

def analyser_commande():
    parser = argparse.ArgumentParser(description='Donne un nom au joueur')
    parser.add_argument('idul', help='un nom pour le joueur')
    parser.add_argument('-l', '--lister', action='store_true' , help='Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    print(analyser_commande())

def afficher_damier_ascii(dict):
    deb = 'Légende: 1='+str(dict['joueurs'][0]['nom'])+' 2=automate'+'\n'+'   '+35*'-'+'\n'
    sui = ''
    for i in range(8):
        sui += str(9-i)+' | '+8*'.   '+'. |'+'\n'+'  |                                   |'+'\n'
    fin = '1 | .   .   .   .   .   .   .   .   . |'+'\n'+'--|-----------------------------------'+'\n'+'  | 1   2   3   4   5   6   7   8   9'
    tot = list(sui+fin)
    for j in range(len(dict)):
        tot[40*(18-2*dict['joueurs'][j]['pos'][1])+4*dict['joueurs'][j]['pos'][0]] = str(j+1)
    for i in dict['murs']['horizontaux']:
        for b in range(7):
            tot[40*(19-2*i[1])+4*i[0]-1+b] = '-'
    for l in dict['murs']['verticaux']:
        for c in range(3):
            tot[40*(18-c-2*l[1])+4*l[0]-2] = '|'
    return deb + ''.join(tot)

from api import *


if analyser_commande().lister:
    print(lister_partie(analyser_commande().idul))
else:
    IDUL = analyser_commande().idul
    v = debuter_partie(IDUL)
    print(afficher_damier_ascii(v['état']))
    id = (v['id'])
    v = 0
    while v < 1:
        b = input('type de coup ? D, MH ou MV ')
        c = input('point ? (x, y) ')
        a = jouer_coup(id, b, c)
        if a.get('message'):
            print(a)
        elif a.get('gagnant'):
            print(afficher_damier_ascii(a['état']))
            print(str(a['gagnant']) + ' est l\'ultime champion!!')
            v += 1
        else:
            print(afficher_damier_ascii(a['état']))