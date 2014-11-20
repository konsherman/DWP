#Konner Sherman
#today
#dynamic-stie


class Cat(object): #super classss
    def __init__(self):
        self.cat_name = ""
        self.cat_type = ""
        self.cat_color = ""
        self.cat_image = ""


class Orange(Cat):
    def __init__(self):
        Cat.__init__(self) #calling in the super class
        self.cat_name = "Orange Cat"
        self.cat_type = "American Short Hair"
        self.cat_color = "Orange"
        self.cat_image = '<img src="http://upload.wikimedia.org/wikipedia/commons/1/1b/Mr._Maji,_a_long-haired_orange_cat_with_white_muzzle.jpg" width="300px" height="300px">'
    def show(self):
        return "<p>"+ self.cat_name+ "</p>"+ "<p>"+self.cat_type+"</p>" + "<p>"+self.cat_color+"</p>"+self.cat_image #function that adds everything up for spesific cat and returns it 



class Black(Cat):
    def __init__(self):
        Cat.__init__(self)
        self.cat_name = "Black Cat "
        self.cat_type = "Bombay "
        self.cat_color = "Black "
        self.cat_image = '<img src="http://blog.hepcatsmarketing.com/wp-content/uploads/2013/07/Cat-of-the-Day-Bombay-3.gif" width="300px" height="300px"/>'

    def show(self):
        return "<p>"+ self.cat_name+ "</p>"+ "<p>"+self.cat_type+"</p>" + "<p>"+self.cat_color+"</p>"+self.cat_image



class Bengal(Cat):
    def __init__(self):
        Cat.__init__(self)
        self.cat_name = "Bengal Cat "
        self.cat_type = "Bengal "
        self.cat_color = "Mix "
        self.cat_image = '<img src="http://www.royalcanin.com.au/var/royalcanin/storage/images/breeds/cat-breeds/bengal/18927210-13-eng-GB/bengal.jpg" width="300px" height="300px"/>'

    def show(self):
        return "<p>"+ self.cat_name+ "</p>"+ "<p>"+self.cat_type+"</p>" + "<p>"+self.cat_color+"</p>"+self.cat_image


class Burmese(Cat):
    def __init__(self):
        Cat.__init__(self)
        self.cat_name = "Burmese "
        self.cat_type = "Burmese "
        self.cat_color = "White-ish Grey "
        self.cat_image = '<img src="http://www.royalcanin.in/var/royalcanin/storage/images/breeds/cat-breeds/burmese/19254976-17-eng-GB/burmese.jpg" width="300px" height="300px"/>'


    def show(self):
        return "<p>"+ self.cat_name+ "</p>"+ "<p>"+self.cat_type+"</p>" + "<p>"+self.cat_color+"</p>"+self.cat_image



















