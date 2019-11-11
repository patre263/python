import argparse

def analyser_commande():
    parser = argparse.ArgumentParser(description='Donne un nom au joueur')
    parser.add_argument('i', 'idul',  metavar='idul', type=str, help='un nom pour le joueur')
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
    k = 0
    for j in range(len(dict)):
        k +=1
        tot[40*(18-2*dict['joueurs'][j]['pos'][1])+4*dict['joueurs'][j]['pos'][0]] = str(k)
    for i in dict['murs']['horizontaux']:
        tot[40*(19-2*i[1])+4*i[0]-1] = '-'
        tot[40*(19-2*i[1])+4*i[0]] = '-'
        tot[1+40*(19-2*i[1])+4*i[0]] = '-'
        tot[2+40*(19-2*i[1])+4*i[0]] = '-'
        tot[3+40*(19-2*i[1])+4*i[0]] = '-'
        tot[4+40*(19-2*i[1])+4*i[0]] = '-'
        tot[5+40*(19-2*i[1])+4*i[0]] = '-'
    for l in dict['murs']['verticaux']:
        tot[40*(18-2*l[1])+4*l[0]-2] = '|'
        tot[40*(17-2*l[1])+4*l[0]-2] = '|'
        tot[40*(16-2*l[1])+4*l[0]-2] = '|'
    return deb + ''.join(tot)

import requests

def lister_partie(idulenchaine): 
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(url_base+'lister/', params={'idul':idulenchaine})
    if rep.status_code == 200:
        rep = rep.json()
        return(rep)
    else:
        return(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")

def debuter_partie(idulenchaine):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idulenchaine})
    return(rep.json())

def jouer_coup(id_partie, type_coup, position):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'jouer/', data={'id': id_partie, 'type': type_coup, 'pos': position})
    return(rep.json())

    
