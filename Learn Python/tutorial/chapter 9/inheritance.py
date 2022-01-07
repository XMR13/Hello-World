#mengontol ygy
class Restaurant:
    def __init__(self,name,cuisinetype):
        self.name = name
        self.tipe_menu = cuisinetype
        self.number_served = 0

    def describe_restaurant(self):
        print(f'nama restaurant adlah {self.name}')
        print(f'tipe menu yang disediakan adlah {self.tipe_menu}')

    def banyak_pesanan(self):
        print(f'banyak pesanan hari ini adalah {self.number_served}')
    
    def set_banyakpesanan(self,banyak):
        if banyak >= self.number_served:
            self.number_served = banyak
        else:
            print("besar tetapan tidak boleh lebih kecil dari nilai awal")
        

    def inrement_served(self,tambah):
        self.number_served += tambah

    
class Ice_Cream_Stand(Restaurant):
    def __init__(self, name, cuisinetype):
        super().__init__(name, cuisinetype)
        self.flavor = ['coklat','vanilla','strawberry','blueberry']

    
    def menampiklan_rasa(self):
        print("rasa eskrim yang ada pada resto ini adalah")
        for rasa in self.flavor:
            print(rasa)


ice_unclemutu = Ice_Cream_Stand('uncle mutu','ice cream')
ice_unclemutu.describe_restaurant()
ice_unclemutu.menampiklan_rasa()

    

