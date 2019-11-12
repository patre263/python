import requests

def lister_partie(idulenchaine):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(url_base+'lister/', params={'idul':idulenchaine})
    if rep.status_code == 200:
        return rep.json()
    return f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}."

def debuter_partie(idulenchaine):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idulenchaine})
    return rep.json()

def jouer_coup(id_p, type_c, pos):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'jouer/', data={'id': id_p, 'type': type_c, 'pos': pos})
    a = rep.json()
    try:
        if a.get('message'):
            if a['message'][0, 4] == 'Votr':
                raise RuntimeError
        if a.get('gagnant'):
            raise StopIteration
        return a
    except RuntimeError:
        return a['message']
    except StopIteration:
        return a
