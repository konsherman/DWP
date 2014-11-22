
class HouseDataObject():
    def __init__(self):
        self.name = ''
        self.sigil = ''
        self.motto = ''
        self.color1 = ''
        self.color2 = ''
        self.head = ''
        self.image = ''


class Data(object):
    def __init__(self):
        l = HouseDataObject()
        l.name = "Lannister"
        l.sigil = "Lion"
        l.motto = "Hear Me Roar"
        l.color1 = "#FFA319"
        l.color2 = "#800000"
        l.head = "Tywin Lannister"
        l.image = "lannister.jpg"

        s = HouseDataObject()
        s.name = "Stark"
        s.sigil = "Dire Wolf"
        s.motto = "Winter is Coming"
        s.color1 = "#CECECE"
        s.color2 = "#FFFFFF"
        s.head = "Eddard Stark"
        s.image = "stark.jpg"

        b = HouseDataObject()
        b.name = "Baratheon"
        b.sigil = "Stag"
        b.motto = "Ours is the Fury"
        b.color1 = "#000000"
        b.color2 = "#FFD119"
        b.head = "Robert Baratheon"
        b.image = "baratheon.jpg"

        g = HouseDataObject()
        g.name = "GreyJoy"
        g.sigil = "Kraken"
        g.motto = "We Do Not Sow"
        g.color1 = "#FFDF5E"
        g.color2 = "#000000"
        g.head = "Euron Greyjoy"
        g.image = "greyjoy.jpg"

        tg = HouseDataObject()
        tg.name = "Targaryen"
        tg.sigil = "Three headed dragon"
        tg.motto = "Fire and Blood"
        tg.color1 = "#000000"
        tg.color2 = "#800000"
        tg.head = "Danaerys Targaryen"
        tg.image = "targaryen.jpg"

        tl = HouseDataObject()
        tl.name = "Tully"
        tl.sigil = "Leaping Trout"
        tl.motto = "Family, Duty, Honor"
        tl.color1 = "#0066CC"
        tl.color2 = "#990000"
        tl.head = "Hoster Tully"

        self.__houses = [l, s, b, g, tg, tl]


    @property
    def houses(self):
        return self.__houses

    @houses.setter
    def houses(self,new):
        self.__houses = new
