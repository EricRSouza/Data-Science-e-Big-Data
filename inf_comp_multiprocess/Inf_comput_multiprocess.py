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

# import time
# from multiprocessing import Process

# def pi_naive(start, end, step):
#     # print ("Start: ", str(start))
#     # print ("End: ", str(end))
#     sum = 0.0
#     for i in range(start, end):
#         x = (i+0.5) * step
#         sum = sum + 4.0/(1.0+x*x)
#     print(f'Somar: {sum * step}')

# if __name__ == "__main__":
#     num_steps = 10000000 #10.000.000 (10+e7)
#     sums = 0.0
#     step = 1.0/num_steps
#     tic = time.time() # Tempo Inicial
    
#     proc_qt = 4
#     procs = []

#     for i in range(proc_qt):
#         p = Process(target=pi_naive, args=(i*(num_steps//proc_qt), (i+1)*(num_steps//proc_qt)-1, step, ))
#         procs.append(p)

#     for i in range(proc_qt):
#         procs[i].start()

#     for i in range(proc_qt):
#         procs[i].join()

#     toc = time.time() # Tempo Final 
    # pi = step * sums
    # print ("Valor Pi: %.10f" %pi)
    # print ("Tempo Pi: %.8f s" %(toc-tic))


#----------------------------------------------------------------------------------
# Exercicio 5

# import time
# from multiprocessing import Process, Pipe, Lock

# def pi_naive(lk, start, end, step, connection):
#     # print ("Start: ", str(start))
#     # print ("End: ", str(end))
#     sum = 0.0
#     for i in range(start, end):
#         x = (i+0.5) * step
#         sum = sum + 4.0/(1.0+x*x)
#     with lk:
#         connection.send(sum * step)

# if __name__ == "__main__":
#     num_steps = 10000000 #10.000.000 (10+e7)
#     sums = 0.0
#     step = 1.0/num_steps
#     tic = time.time() # Tempo Inicial
    
#     proc_qt = 4
#     workers = []

#     connection_master, connection_worker = Pipe()
#     var_pi = []
#     #pi = 0.0

#     lock = Lock()


#     for i in range(proc_qt):
#         p = Process(target=pi_naive, args=(lock, i*(num_steps//proc_qt), (i+1)*(num_steps//proc_qt)-1, step, connection_worker, ))
#         workers.append(p)

#     for i in range(proc_qt):
#         workers[i].start()

#     for i in range(proc_qt):
#         workers[i].join()
#         var_pi.append(connection_master.recv())
#     print(var_pi)
#     print(sum(var_pi)) # Valor de Pi
#         #pi += connection_master.recv()
#    # print(pi)
      

#     toc = time.time() # Tempo Final 
#     # pi = step * sums
#     # print ("Valor Pi: %.10f" %pi)
#     # print ("Tempo Pi: %.8f s" %(toc-tic))


#----------------------------------------------------------------------------------
# Exercicio 5

# import time
# from multiprocessing import Process, current_process, Queue

# def pi_naive(start, end, step, queue):
#     # print ("Start: ", str(start))
#     # print ("End: ", str(end))
#     sum = 0.0

#     for i in range(start, end):
#         x = (i+0.5) * step
#         sum = sum + 4.0/(1.0+x*x)

#     queue.put(sum * step)

# if __name__ == "__main__":
#     num_steps = 10000000 #10.000.000 (10+e7)
#     sums = 0.0
#     step = 1.0/num_steps
#     tic = time.time() # Tempo Inicial

#     cpu = 4
#     loop_range = num_steps//cpu
#     workers = []

#     var_pi = []
#     # pi = 0.0

#     queue = Queue()

#     for i in range(cpu):
#         p = Process(target=pi_naive, args=(i*(loop_range), (i+1)*(loop_range)-1, step, queue))
#         workers.append(p)

#     for i in range(cpu):
#         workers[i].start()

#     for i in range(cpu):
#         workers[i].join()
#     #     pi += queue.get()
#     # print(pi)
#         var_pi.append(queue.get())
#     print(var_pi)
#     print(sum(var_pi))


#     toc = time.time() # Tempo Final 
    # pi = step * sums
    # print ("Valor Pi: %.10f" %pi)
    # print ("Tempo Pi: %.8f s" %(toc-tic))


#----------------------------------------------------------------------------------
# Exercicio 6

import time
from multiprocessing import Process, Value

def pi_naive(start, end, step, valor):
    # print ("Start: ", str(start))
    # print ("End: ", str(end))
    sum = 0.0

    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)

    with valor.get_lock():
        valor.value += sum * step

if __name__ == "__main__":
    num_steps = 10000000 #10.000.000 (10+e7)
    sums = 0.0
    step = 1.0/num_steps
    tic = time.time() # Tempo Inicial

    cpu = 4
    loop_range = num_steps//cpu
    workers = []

    pi = 0.0
    v = Value('d', 0, lock=True)


    for i in range(cpu):
        p = Process(target=pi_naive, args=(i*(loop_range), (i+1)*(loop_range)-1, step, v))
        workers.append(p)

    for i in range(cpu):
        workers[i].start()

    for i in range(cpu):
        workers[i].join()
    
    pi += step * v.value
    print(pi)

    toc = time.time() # Tempo Final 
    # pi = step * sums
    # print ("Valor Pi: %.10f" %pi)
    # print ("Tempo Pi: %.8f s" %(toc-tic))


