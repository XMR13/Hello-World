'''
soal python ygy
9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 100 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range
'''
class Car:
    def __init__(self,nama,merk,tahun_keluar:int):
        self.nama = nama
        self.merk = merk
        self.tahun_keluar = tahun_keluar

    def describe_mobil(self):
        print(f"{self.nama}, dengan merk {self.merk}, dan tahun {self.tahun_keluar}")


class Electric_Car(Car):
    def __init__(self,nama,merk,tahun_keluar):
        super().__init__(nama,merk,tahun_keluar)
        self.kapasitas_baterai = Battery()


class Battery:
    def __init__(self):
        self.besarbattery = 50

    def describe_battery(self):
        print(f'besar batterai ini adalah {self.besarbattery} kwH')
    
    def menetapkan_range(self):
        if self.besarbattery == 100:
            jarak = 360
        
        elif self.besarbattery ==75:
            jarak = 100
        elif self.besarbattery == 50:
            jarak = 50

        print(f"baterai ini dapat bertahan sekitar {jarak} lagi")

    def upgradebattery(self):
        self.besarbattery = 100

tesla = Electric_Car('Tesla model s','tesla',2013)
tesla.describe_mobil()
tesla.kapasitas_baterai.describe_battery()
tesla.kapasitas_baterai.menetapkan_range()
tesla.kapasitas_baterai.upgradebattery()
tesla.kapasitas_baterai.menetapkan_range()
