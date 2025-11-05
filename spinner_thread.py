import itertools
import time
from threading import Thread,Event
from primes import is_prime

def spin(msg:str,done:Event)->None:
    for char in itertools.cycle(r'\|/-'):
        status=f'\r{char} {msg}'
        print(status,end='',flush=True)
        # 这里的wait()方法会阻塞此线程0.1秒，直到done.set()被调用
        # 如果没有被调用，则wait()方法会在0.1秒后返回False
        # 如果其他线程调用done.set()方法，则wait()方法会返回True
        if done.wait(.07):
            break
    blanks=' '*len(status)
    print(f'\r{blanks}\r',end='')

def slow()->int:
    # time.sleep(3)
    is_prime(5000111000222021)
    return 42


def supervisor()->int:
    # 创建一个事件用来两个线程通信
    done=Event()
    # 创建一个线程
    spinner=Thread(target=spin,args=('thinking!',done))
    # 打印此时线程的状态，显示initial
    print(f"spinner object: {spinner}")
    # 开始执行这个线程
    spinner.start()
    # 主线程调用函数阻塞主线程，此时会释放GIL，并允许其他线程执行
    result=slow()
    # 主线程阻塞完毕之后，会继续执行，调用done.set()方法，通知线程结束
    done.set()
    # 主线程等待线程结束
    spinner.join()
    return result

def main()->None:
    answer=supervisor()
    print(f'Answer: {answer}')

if __name__=='__main__':
    main()