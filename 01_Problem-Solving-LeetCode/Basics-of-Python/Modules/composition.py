class CPU:
    def __init__(self,RAM,ROM):
        self.RAM = RAM
        self.ROM = ROM
    def cpu(self):
        return "CPU details: "+ self.RAM + self.ROM
class OS:
    def __init__(self,name,version):
        self.name = name
        self.version = version
    def os(self):
        return "OS details: "+ self.name + self.version
class Compture:
    def __init__(self,Cname,Cprize,obj_cpu, obj_os):
        self.Cname = Cname
        self.Cprize = Cprize
        self.obj_cpu = obj_cpu
        self.obj_os = obj_os
    def T_Com(self):
        return self.obj_cpu + self.obj_os + self.Cname + str(self.Cprize)

obj_cpu = CPU(16,256)
obj_os = OS('Ubuntu', 20)
com = Compture('acer',56000,obj_cpu,obj_os)
print(com.T_Com())








