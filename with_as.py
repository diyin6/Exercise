class open1:
    def __init__(self, name):
        self.name = "123"
    def __enter__(self):
        print "enter"
        return "aaas2s"
    def __exit__(self, exc_type, exc_val, exc_tb):
        print exc_type
        print exc_val
        print exc_tb
        print "exit"
        return True
with open1("aaa") as f:
    print f
    print sss
    print "555"
    pass

print "llllllllllllll"