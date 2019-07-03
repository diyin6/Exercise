import os,time

currentPath = os.path.dirname(os.path.abspath(__file__))
print(currentPath)
print os.getcwd()
print os.chdir(currentPath)
print os.environ['HOME']
print os.path.expandvars('HOME')
print os.path.expanduser('~')
print os.path.split(os.path.abspath(__file__))[1]
print os.path.basename(__file__)
print os.getpid()
print os.getgid(),os.getppid(),os.getegid()
print __file__
strrr = "e"
print strrr.join("'python'")

def hh():
    return False,"ssdd"

print hh()[1]
passwd = "123"
str2 = "echo %s| sudo -S /home/nvidia/jetson_clocks.sh" % passwd

print str2
a = {"server":[133,0.3455]}
a.update({"main":[3232,0.43434]})
print a["main"][0]


clientSysTimeOffset = 8888
def timeStamp2string(nowtime):
    return time.strftime('tri_%Y%m%d_%H%M%S_', time.localtime(nowtime - clientSysTimeOffset)) + \
             "%03d" % int((nowtime - int(nowtime)) * 1000 )




print timeStamp2string(3423423.00555)

class aa():
    def verif_args(self,cmd):
        if hasattr(self, cmd):
            func = getattr(self,cmd)
            func("asdas")
        else:
            print "cmd not exist"

    def done(self,tt):
        print "done"
        print tt

a2 = aa()
a2.verif_args("done2")
# change 2
