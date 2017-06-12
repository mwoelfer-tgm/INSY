from django.db import models

class Kunde(models.Model):
    knr = models.IntegerField()
    name = models.CharField(max_length=255)
    pw = models.CharField(max_length= 24)

    def __str__(self):
        return 'Knr: {}, Name: {}'.format(self.knr, self.name)

class Land(models.Model):
        name = models.CharField(max_length=255, primary_key=True)

        def __str__(self):
            return 'Name: {}'.format(self.name)

class Adresse(models.Model):
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE)
    strasse = models.CharField(max_length=255)
    hnr = models.IntegerField()
    plz = models.CharField(max_length=20)
    ort = models.CharField(max_length=255)
    land = models.ForeignKey(Land,on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}, {} {} - {}'.format(self.strasse, self.hnr, self.plz, self.ort, self.land)

class Artikel(models.Model):
    anr = models.IntegerField(primary_key=True)
    abez = models.CharField(max_length=255)
    npreis = models.DecimalField(max_digits=7,decimal_places=2)
    vstueck = models.IntegerField()
    info = models.CharField(max_length=1000)

    def __str__(self):
        return 'Anr: {} , Abez: {}'.format(self.anr, self.abez)


class Bestellung(models.Model):
    bdatum = models.DateField()
    kunde = models.ForeignKey(Kunde,on_delete=models.CASCADE)
    bnr = models.IntegerField()
    lieferadrbez = models.CharField(max_length=255)
    rechnadrbez = models.CharField(max_length=255)
    artikel = models.ManyToManyField(Artikel, through="Bestellartikel")
    bstatus = models.CharField(max_length=255, default="")

    def __str__(self):
        return 'Kunde: {} , Bestellnummer: {}, Adresse: {}, ' \
               'Datum: {}, Artikel: {}'.format(self.kunde, self.bnr, self.lieferadrbez, self.bdatum, self.artikel)

class Bestellartikel(models.Model):
    artikel = models.ForeignKey(Artikel,on_delete=models.CASCADE)
    bestellung = models.ForeignKey(Bestellung,on_delete=models.CASCADE)
    bstueckz = models.IntegerField()

    def __str__(self):
        return 'Artikel: {} , Bestellung: {}, ' \
               'Bestelle stückzahl: {}'.format(self.artikel, self.bestellung, self.bstueckz)


class Feedback(models.Model):
    kunde = models.ForeignKey(Kunde,on_delete=models.CASCADE)
    bestellartikel = models.ForeignKey(Bestellartikel,on_delete=models.CASCADE)
    fdatum = models.DateField()
    fbemerk = models.CharField(max_length=255)

    def __str__(self):
        return 'Kunde: {} , Artikel: {}, Bemerkung: {}'.format(self.kunde, self.bestellartikel, self.fbemerk)

class Bluray(Artikel):
    regisseur = models.CharField(max_length=255)
    jahr = models.IntegerField()
    genre = models.CharField(max_length=255)

    def __str__(self):
        return super().__str__() + 'regisseur: {} , jahr: ' \
                                 'Genre: {}'.format(self.regisseur, self.jahr, self.genre)

class Buch(Artikel):
    autor = models.CharField(max_length=255)
    verlag = models.CharField(max_length=255)
    ISBN = models.IntegerField()

    def __str__(self):
        return super().__str__() + ', Autor: {} , Verlag: ' \
                                 'ISBN: {}'.format(self.autor, self.verlag, self.ISBN)

class SonstigerArtikel(Artikel):
    pass