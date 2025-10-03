"""Utilisation des classes et de l'héritage
*une classe mère Contact
*deux classes enfants : PersonneSuivante et Organisation

ATENTION : pour les classes enfants la gestion des
__del__ des variables de classe de la classe mère doit
être faite manuellement !

*la dernière partie 'if __name__ == "__main__":'
permet d'exécuter du code quand le module est lancé comme un script principal
et non comme un module utilisé dans un autre script."""


class Contact:
    nbre_contacts = 0

    def __init__(self, tel, ad, pays="France"):
        self._telephone = tel
        self._adresse = ad
        self._pays = pays
        Contact.nbre_contacts += 1

    def __del__(self):
        Contact.nbre_contacts -= 1

    def _get_tel(self):
        return self._telephone

    def _get_ad(self):
        return self._adresse

    def _get_pays(self):
        return self._pays

    def _set_tel(self, valeur):
        self._telephone = valeur

    def _set_ad(self, valeur):
        self._adresse = valeur

    def _set_pays(self, valeur):
        self._pays = valeur

    def __repr__(self):
        return f"tel: {self._telephone}, adr: {self._adresse}, pays: {self._pays}"

    @classmethod
    def combien(cls):
        print("Il y a", cls.nbre_contacts, "éléments")

    telephone = property(_get_tel, _set_tel)
    adresse = property(_get_ad, _set_ad)
    pays = property(_get_pays, _set_pays)


class PersonneSuivante(Contact):
    nbre_personne = 0

    def __init__(self, tel, ad, pays="France", nom="Doe", prenom="John", age=33):
        self._nom = nom
        self._prenom = prenom
        self._age = age
        super().__init__(tel, ad, pays)
        PersonneSuivante.nbre_personne += 1

    def __del__(self):
        PersonneSuivante.nbre_personne -= 1
        super().__del__()

    @classmethod
    def combienTotal(cls):
        super().combien()

    def combien(cls):
        print("Il y a", cls.nbre_personne, "personne(s)")


class Organisation(Contact):
    def __init__(self, tel, ad, pays="France", raison_sociale="World Company"):
        self._raison_sociale = raison_sociale
        super().__init__(tel, ad, pays)


if __name__ == "__main__":
    from class_carnet import Contact, PersonneSuivante

    c1 = Contact(6, "Place", "Allemagne")
    print(c1.adresse)
    print(c1.pays)
    print(c1.telephone)
    print(c1)
    print(c1.combien())

    c2 = Contact(7, "rue")
    print(c2.adresse)
    print(c2.combien())

    print("delete 1 contact")
    del c2
    print(Contact.combien())

    print("add a personne)")
    p1 = PersonneSuivante(nom="Mich", prenom="Arth", age=37, tel=643, ad="place An")
    print("Nom:", p1._nom)
    print("age", p1._age)
    print(p1.adresse)
    print(p1.combienTotal())
    print(p1.combien())

    print("add a personne)")
    p2 = PersonneSuivante(nom="Nono", prenom="Papa", age=51, tel=711, ad="Nizza")
    print(p2.combienTotal())
    print(p2.combien())
    del p1
    print("delete 1 personne")
    print(p2.combienTotal())
    print(p2.combien())

    o1 = Organisation(raison_sociale="Tutur Company", tel=9, ad="Middle East")
    print("Orga 1 :", o1._raison_sociale)
    print(o1._adresse)
    o2 = Organisation(tel=10, ad="Worldwide")
    print("Orga 2 :", o2._raison_sociale)
    print(o2._adresse)
