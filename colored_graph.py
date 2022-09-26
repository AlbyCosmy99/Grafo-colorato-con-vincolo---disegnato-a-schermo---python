#grafo con nodi colorati, con vincolo che due colori uguali non possono stare vicini. 
#I nodi assumono colori casuali dal dominio ["red", "green", "blue"]

from constraint import *
from networkx import *
import matplotlib.pyplot as plt
import random 

def grafo_vincoli(grafo):
    problem = Problem()
    
    for node in grafo.nodes():
        problem.addVariable(node,(["red", "green", "blue"]))
        for neighbor in grafo.neighbors(node):
            problem.addConstraint(lambda a,b : a!=b, (node,neighbor))
            
    solutions = problem.getSolutions()
    
    n_sol = random.randint(0,len(solutions)-1)
    
    if not len(solutions) == 0:
        return solutions[n_sol]  #restituisco solo la n_sol soluzione
    else:
        return "Non ci sono soluzioni valide."
    
#main utilizzato per testare il codice    
if __name__ == '__main__':
    
    #problema2
    grafo = Graph()
    grafo.add_nodes_from(["A","B","C","D","E","F","G","H","I","L","M","N","O","P","Q","R","S","T","U","V","Z"])
    nodes = grafo.nodes()
  
    grafo.add_edge("A","V")
    grafo.add_edge("A","H")
    grafo.add_edge("B","G")
    grafo.add_edge("B","L")
    grafo.add_edge("C","U")
    grafo.add_edge("C","D")
    grafo.add_edge("D","H")
    grafo.add_edge("E","R")
    grafo.add_edge("F","M")
    grafo.add_edge("F","I")
    grafo.add_edge("G","N")
    grafo.add_edge("I","T")
    grafo.add_edge("L","U")
    grafo.add_edge("M","O")
    grafo.add_edge("N","Z")
    grafo.add_edge("O","V")
    grafo.add_edge("P","Q")
    grafo.add_edge("Q","S")
    grafo.add_edge("R","Z")
    grafo.add_edge("S","T")
    grafo.edges()
  
    result = grafo_vincoli(grafo)
    print(result)
    
    color_list = []
    for node in nodes:
        color_list.append(result[node])
    
    draw(grafo,node_color=color_list)
    plt.show()

    
   
