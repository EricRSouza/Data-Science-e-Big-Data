# Exercicio 1

# from multiprocessing import Process

# def f(name):
#     print('hello, sou', name)

# if __name__ == '__main__':
#     p = Process(target=f, args=('bob filho', ))
#     p.start()
#     print('hello, sou', 'bob pai') ## Temos 2 processos!
#     p.join()



# ---------------------------------------------------------------------------------
# Exercicio 2
# Imprime tudo ao mesmo tempo
# from multiprocessing import Process

# def f(name, id):
#     print('hello, sou', name, id)

# if __name__ == '__main__':
#     procs = []
    
#     for i in range(16):
#         p = Process(target=f, args=('bob filho', i, ))
#         procs.append(p)

#     print('hello, sou', 'bob pai')
    
#     for i in range(16):
#         procs[i].start()

#     for i in range(16):
#         procs[i].join()



# ---------------------------------------------------------------------------------
# Exercicio 3
# Executa sequencialmente. NÃO PROCESSA EM PARELELLO

# from multiprocessing import Process

# def f(name, id):
#     print('hello, sou', name, id)

# if __name__ == '__main__':
#     procs = []
    
#     for i in range(16):
#         p = Process(target=f, args=('bob filho', i, ))
#         procs.append(p)

#     print('hello, sou', 'bob pai')
    
#     for i in range(16):
#         procs[i].start()
#         procs[i].join()



# ---------------------------------------------------------------------------------
# Exercicio 4

import time
from multiprocessing import Process

def pi_naive(start, end, step):
    # print ("Start: ", str(start))
    # print ("End: ", str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    print(f'Somar: {sum * step}')

if __name__ == "__main__":
    num_steps = 10000000 #10.000.000 (10+e7)
    sums = 0.0
    step = 1.0/num_steps
    tic = time.time() # Tempo Inicial
    
    proc_qt = 4
    procs = []

    for i in range(proc_qt):
        p = Process(target=pi_naive, args=(i*(num_steps//proc_qt), (i+1)*(num_steps//proc_qt)-1, step, ))
        procs.append(p)

    for i in range(proc_qt):
        procs[i].start()

    for i in range(proc_qt):
        procs[i].join()

    toc = time.time() # Tempo Final 
    # pi = step * sums
    # print ("Valor Pi: %.10f" %pi)
    # print ("Tempo Pi: %.8f s" %(toc-tic))