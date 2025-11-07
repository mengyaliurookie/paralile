from multiprocessing import Process,Lock

def f(l,i):
    # l.acquire()
    # try:
        print(f"Process {i}: {'hello ' * 2000}")
    # finally:
    #     l.release()

if __name__=='__main__':
    lock=Lock()

    for num in range(30):
        Process(target=f,args=(lock,num)).start()