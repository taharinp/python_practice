class parent:
    def show (self):
        print('parent show')

class child(parent):
    def show(self):
        super().show()
        print('child show')



c=child()
c.show()