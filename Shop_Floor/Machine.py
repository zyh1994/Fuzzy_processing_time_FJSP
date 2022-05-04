'''
Code Time: 2022/5/4 10:34
by: Aihong-Sun
use for: Machine describe
'''
from Shop_Floor.Fuzzy_time_operator import *

class Machine:
    def __init__(self,idx,Mach_Info):
        self.idx=idx
        self.pro_power=Mach_Info[0]    #运行功率
        self.unload_power=Mach_Info[1]      #空载功率
        self.unit_price=Mach_Info[2]     #加工单价
        self.start=[]
        self.end=[]
        self._on=[]

    def update(self,s,e,Job):
        self.start.append(s)
        self.start.sort(key=lambda u:u[1])
        self.end.append(e)
        self.end.sort(key=lambda u:u[1])
        idx=self.start.index(s)
        self._on.insert(idx,Job)

    def find_start(self,s,o_pt):
        if self.end==[]: return [0,0,0]
        else:
            if Measure(s,self.end[-1]):return s
            else:
                if Measure(self.end[-1],s):end=self.end[-1]
                else:end=s
                l = len(self.end) - 2
                while l>=0:
                    if Measure(s,self.start[l+1]):
                        break
                    if Measure(self.end[l],s):
                        end_find=add(self.end[l],o_pt)
                        if Measure(self.start[l+1],end):
                            end=end_find
                    else:
                        end_find=add(s,o_pt)
                        if Measure(self.start[l+1],end_find):
                            end=end_find
                    l-=1
                return end







