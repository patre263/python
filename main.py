"Argphase permet d'appeler le main dans la bare de commande et d'avoir une option help"
"Permet d'utiliser les fonctions faites dans le fichier api"
import argparse 
import api 

def analyser_commande():
    "Initialise le argparse"
    parser = argparse.ArgumentParser(description='Donne un nom au joueur')
    parser.add_argument('idul', help='un nom pour le joueur')
    parser.add_argument('-l', '--lister', action='store_true',
                        help='Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    print(analyser_commande())

def afficher_damier_ascii(dico):
    "Afiche le jeu avec un dictionnaire état"
    deb = 'Légende: 1='+str(dico['joueurs'][0]['nom'])+' 2=automate'+'\n'+'   '+35*'-'+'\n'
    sui = ''
    for i in range(8):
        sui += str(9-i)+' | '+8*'.   '+'. |'+'\n'+'  |                                   |'+'\n'
    fin = '1 |' + ' .  '*8 + ' . |'+'\n'+'--|' + '-'*35 + '\n'
    fin2 = '  | 1   2   3   4   5   6   7   8   9'
    tot = list(sui+fin+fin2)
    for j in range(len(dico)):
        tot[40*(18-2*dico['joueurs'][j]['pos'][1])+4*dico['joueurs'][j]['pos'][0]] = str(j+1)
    for i in dico['murs']['horizontaux']:
        for ading in range(7):
            tot[40*(19-2*i[1])+4*i[0]-1+ading] = '-'
    for place in dico['murs']['verticaux']:
        for adding in range(3):
            tot[40*(18-adding-2*place[1])+4*place[0]-2] = '|'
    return deb + ''.join(tot)

if analyser_commande().lister:
    print(api.lister_partie(analyser_commande().idul))
else:
    IDUL = analyser_commande().idul
    v = api.debuter_partie(IDUL)
    print(afficher_damier_ascii(v['état']))
    CTE = v['id']
    v = 0
    while v < 1:
        b = input('type de coup ? D, MH ou MV ')
        c = input('point ? (x, y) ')
        a = api.jouer_coup(CTE, b, c)
        if a.get('message'):
            print(a)
        elif a.get('gagnant'):
            print(afficher_damier_ascii(a['état']))
            print(str(a['gagnant']) + ' GAGNE!!')
            v += 1
        else:
            print(afficher_damier_ascii(a['état']))
