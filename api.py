"Importe le module requests qui permet de faire des requetes au serveur"
import requests

def lister_parties(idulenchaine):
    "permet au joueur de parcourir l'historique de ses 20 dernières parties"
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(url_base+'lister/', params={'idul':idulenchaine})
    if rep.status_code == 200:
        rep = rep.json()
    try:
        if rep.get('message'):
            raise RuntimeError
        return rep
    except RuntimeError:
        return rep['message']

def débuter_partie(idulenchaine):
    "Permet au joueur de débuter une partie avec son idul"
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idulenchaine})
    rep = rep.json()
    try:
        if rep.get('message'):
            raise RuntimeError
        return rep
    except RuntimeError:
        return rep['message']

def jouer_coup(id_p, type_c, pos):
    "permet au joueur de jouer un coup dans sa partie avec le type de coup et le point"
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'jouer/', data={'id': id_p, 'type': type_c, 'pos': pos})
    a = rep.json()
    try:
        if a.get('message'):
            raise RuntimeError
        if a.get('gagnant'):
            raise StopIteration
        return a
    except RuntimeError:
        return a['message']
    except StopIteration:
        return a['gagnant']
