import random
import numpy as np
import matplotlib.pyplot as plt
population=[]
chorom=[]
fitness_list=[]
chorom_after_mutate=[]
max_fitness=[]
avaragef=[]
def random_chorom():
    populations=[]
    s=0
    while(s<50):
        a=np.random.randint(1,20,4)
        if sum(a)==20:
            populations.append(list(a))
            s+=1        
    chorom=populations.pop(0) 
    return chorom,populations

def fitness(choromosomeA,population):
     fitness_value=0
     for choromosome in population:
          #print('choromosome',choromosome)
          winA=0
          winB=0
          for i in range(4):
               #print('choromosomeA[i]',choromosomeA[i])
               if choromosomeA[i]==choromosome[i]:
                    winA+=1
               elif choromosomeA[i]>choromosome[i]:      
                    winA+=2
          winB=8-winA
          if winA>=winB:
               fitness_value+=1
          #if winA==winB:
           #    fitness_value+=1
     return(fitness_value)

def tselect(population):
     parent=[]
     parents_fitness=[]
     parent1=[]
     parents_fitness1=[]
     k=list(np.random.randint(0,49,5))
     #print('k',k)
     for i in k:
          parent.append(population[i])
     #print('parent=',parent)
     for k in parent:
         x=fitness(k,population)
         parents_fitness.append(x)
     #print('parents_fitness=',parents_fitness)
     max1_fitness=max(parents_fitness)
     best_chorom1=parent[parents_fitness.index(max1_fitness)]

     k1=list(np.random.randint(0,49,5))
     for i in k1:
          parent1.append(population[i])
     for k1 in parent1:
         x=fitness(k1,population)
         parents_fitness1.append(x)
     max2_fitness=max(parents_fitness1)
     best_chorom2=parent1[parents_fitness1.index(max2_fitness)]
   
     return best_chorom1,best_chorom2
    
def recombination(choromosome1,choromosome2):
    child1=[]
    child2=[]
    crossover=random.randint(0,3)
    #print('crossover_point:',crossover)
    child1.extend(choromosome1[0:crossover+1])
    child2.extend(choromosome2[0:crossover+1])
    while len(child1)!=4:
        for i in range(crossover+1,4):
            child1.append(choromosome2[i])    
    #print('sum child1:',sum(child1))       
    if sum(child1)<20:
        kambod=20-sum(child1)
        a1=min(child1)+kambod
        b1=child1.index(min(child1))
        child1.pop(b1)
        child1.insert(b1,a1)
         
    elif sum(child1)>20:
        ezafi=sum(child1)-20
        a2=max(child1)-ezafi
        b2=child1.index(max(child1))
        child1.pop(b2)
        child1.insert(b2,a2)
                                  
    while len(child2)!=4:              
        for i in range(crossover+1,4):
            child2.append(choromosome1[i])
    #print('sum child2:',sum(child2))        
    if sum(child2)<20:
        kambod=20-sum(child2)
        a3=min(child2)+kambod
        b3=child2.index(min(child2))
        child2.pop(b3)
        child2.insert(b3,a3)       
    elif sum(child2)>20:
        ezafi=sum(child2)-20
        a4=max(child2)-ezafi
        b4=child2.index(max(child2))
        child2.pop(b4)
        child2.insert(b4,a4)      

    return(child1,child2)
def inverse_mutatation(chorom):
    c=[]
    x=0
    y=0
    while ((y!=x+1) and (x!=y+1)):
        x=np.random.randint(0,4)
        #print('x=',x)   
        y=np.random.randint(0,4)
        #print('y=',y)
    if (x<y):   
        c.extend(chorom[x:y+1])
    else:    
        c.extend(chorom[y:x+1])
    #print('c',c)
    c.reverse()
    #print('c',c)
    if (x<y): 
        chorom[x:y+1]=c
    else:
        chorom[y:x+1]=c
        
    return chorom
    
def elitism_select(population):
    fitness_list=[]
    new_population=[]
    solution=[]
    pop=[]
    Z=[]
    X=[]
  
    for i in population:
        fitness_list.append(fitness(i,population))
    X = sorted(zip(fitness_list,population))
    for i in X:
        Z.append(i[1])
    population.remove(Z[0])
    population.remove(Z[1])
    fitness_list.clear()
    X.clear()
    Z.clear()
    d1=inverse_mutatation(chorom_after_crossover[0])
    d2=inverse_mutatation(chorom_after_crossover[1])
    population.append(d1)
    population.append(d2)
    for i in population:
        fitness_list.append(fitness(i,population))
    X = sorted(zip(fitness_list,population))
    for i in X:
        Z.append(i[1])
    
    #print('fitness list=',fitness_list)
    #print('list bar asase fitness=',X)
    #print('list bar asase fitness=',len(Z))
    new_population.extend(Z[45:50])
    p = random_chorom()
    pop.extend(p[1])
    pop.append(p[0])
    k=list(np.random.randint(0,49,25))
    k1=list(np.random.randint(0,49,20))
    solution=new_population[4]
    #print('solution',solution)
    for i in k:
        new_population.append(pop[i])
    for i in k1:
        new_population.append(population[i])
    x=X[49]
    max_fitness=x[0]
    avg_fitness=(sum(fitness_list))/len(fitness_list)
    #print('avg_fitness=',avg_fitness)
    return new_population,solution,max_fitness,avg_fitness



t=random_chorom()
population=t[1]
chorom=t[0]
population.append(chorom)

for i in range(1000):
    print('iteration=',i)
    best_choromosome=tselect(population)
    chorom_after_crossover = recombination(best_choromosome[0],best_choromosome[1])
    s=elitism_select(population)
    chorom=s[1]
    print('the max value of fitness in iteration',i,'=',s[2])
    max_fitness.append(s[2])
    print('the avarage value of fitness in iteration',i,'=',s[3])
    avaragef.append(s[3])
    if fitness(chorom,population)==50:
            print('solution is',chorom)
            break
       
    population=s[0]
    #print('len population (50)=',len(population))

#print(max_fitness)
#print(avaragef)
plt.style.use('seaborn')
plt.plot(max_fitness, color='blue',label='max fitness')
plt.plot(avaragef, color='red',label='avg fitness')
plt.legend()
plt.show()

