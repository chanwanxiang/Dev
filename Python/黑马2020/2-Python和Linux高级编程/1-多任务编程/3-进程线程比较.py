## 进程线程对比

#     进程:是操作系统进行资源分配和调度的基本单位,进程是线程的容器
#     线程:是操作系统能够进行运算调度的最小单位.它被包含在进程之中,是进程中的实际运作单位.一条线程指的是进程中一个单一顺序的控制流,一个进程中可以并发多个线程,每条线程并行执行不同的任务

# 1. 进程线程对比的三个方向
#     关系对比
#     区别对比
#     优缺点对比

# 2. 关系对比
#     线程是依附在进程里面的,没有进程就没有线程
#     一个进程默认提供一条线程,进程可以创建多个线程

# 3. 区别对比
#     进程之间不共享全局变量
#     线程之间共享全局变量,但是要注意资源竞争的问题,解决办法互斥锁或者线程同步
#     创建进程的资源开销要比创建线程的资源开销要大
#     进程是操作系统资源分配的基本单位,线程是CPU调度的基本单位
#     线程不能够独立执行,必须依存在进程中
#     多进程开发比单进程多线程开发稳定性要强

# 4. 优缺点对比
#     进程优缺点
#         优点可以用多核
#         缺点资源开销大
#     线程优缺点
#         优点资源开销小
#         缺点不能使用多核

# 5. 小结
#     进程和线程都是完成多任务的一种方式
#     多进程要比多线程消耗的资源多,但是多进程开发比单进程多线程开发稳定性要强,某个进程挂掉不会影响其它进程
#     多进程可以使用cpu的多核运行,多线程可以共享全局变量
#     线程不能单独执行必须依附在进程里面