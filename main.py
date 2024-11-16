import argparse
from Instance.base_instance import *
from Algorithm.GA_single_objective import GA
parser = argparse.ArgumentParser()

#params for FJSPF:
parser.add_argument('--n',default=10,type=int,help='job number')
parser.add_argument('--m',default=8,type=int,help='Machine number')
parser.add_argument('--O_num',default=[3,6,4,3,2,3,4,3,5,2],type=list,help='Operation number of each job')
parser.add_argument('--Machine_Info',default=Machine_Info,type=list,help='Information of processing Machine ')
parser.add_argument('--Processing_Machine',default=Processing_Machine,type=list,help='processing machine of operations')
parser.add_argument('--Fuzzy_Processing_Time',default=Fuzzy_Processing_Time,type=list,help='fuzzy processing machine of operations')

#Params for GA
parser.add_argument('--pop_size',default=200,type=int,help='Population size of the genetic algorithm')
parser.add_argument('--gene_size',default=200,type=int,help='generation size of the genetic algorithm')
parser.add_argument('--pc',default=0.8,type=float,help='Crossover rate')
parser.add_argument('--pm',default=0.1,type=float,help='mutation rate')
parser.add_argument('--N_elite',default=10,type=int,help='Elite number')
args = parser.parse_args()
ga=GA(args)
ga.main()
