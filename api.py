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
    a = rep.json()
    try:
        if a.get('message') == True:
            if a['message'][0,4] == 'Votr':
                raise RuntimeError
        if a.get('gagnant') == True:
            raise StopIteration
    except RuntimeError:
        return(a['message'])
    except StopIteration:
        return(a)
    return a