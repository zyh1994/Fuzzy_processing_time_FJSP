import matplotlib.pyplot as plt

def Fuzzy_Gantt(JS):
    for i in range(len(JS.Machines)):
        plt.hlines(i,xmin=0,xmax=JS.C_max,colors="black")
        ST=JS.Machines[i].start
        for j in range(len(ST)):
            y=[i,i-0.2,i]
            plt.fill_between(ST[j],y,[i,i,i])
            plt.text(x=ST[j][1],y=i-0.35,s='O'+str(JS.Machines[i]._on[j][0]+1)+str(JS.Machines[i]._on[j][1]+1),size=9)
            plt.text(x=ST[j][1], y=i - 0.1, s=ST[j],size=9)
        ET=JS.Machines[i].end
        for j in range(len(ET)):
            y=[i,i+0.2,i]
            plt.fill_between(ET[j],y,[i,i,i])
            plt.text(x=ET[j][1],y=i+0.35,s='O'+str(JS.Machines[i]._on[j][0]+1)+str(JS.Machines[i]._on[j][1]+1),size=9)
            plt.text(x=ET[j][1], y=i + 0.1, s=ET[j],size=9)
    plt.show()