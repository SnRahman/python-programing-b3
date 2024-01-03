from vehicle import Vehicle

class Suzuki(Vehicle):

    def __init__(self,model,color,transmission ):
        super().__init__('suzuki',model,color,transmission)

    def suzuki_history(self):
        print('Suzuki Kabushiki gaisha) is a Japanese multinational mobility manufacturer headquartered in Hamamatsu, Shizuoka.')


class EMehran(Suzuki):

    def __init__(self,color):
        super().__init__("eMehran", color,'Auto')

    def up_coming(self):
        print('Trying to reach 1000 miles goal in single charge.')





# s1 = Suzuki('Mehran','Grey','Auto')
# s1.display_all()


# em1 = EMehran('Transparent')
# em1.display_all()
# em1.suzuki_history()
# em1.up_coming()