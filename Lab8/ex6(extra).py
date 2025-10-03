import time
import numpy as np

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.duration = self.end - self.start
        print(f"Время выполнения: {self.duration:.6f} секунд")
        return False



if __name__ == "__main__":
    with Timer():

        a = np.random.randint(0, 10, (5, 5))
        b = np.random.randint(0, 10, (5, 5))

        print('Поэлементное произведение матриц.')
        print(a * b)

        print('Матричное произведение.')
        print(a @ b)

        oprA = np.linalg.det(a)
        print('Определитель матрицы A.')
        print(oprA)

        trans = np.transpose(b)
        print('Транспонированную матрицу B.')
        print(trans)

        opr = np.linalg.det(a)
        if opr != 0:
            inv = np.linalg.inv(a)
            print(inv)
        else:
            print("ооэпрэр ты айпадкид, определитель равен нулю")

        C = a.sum(axis=1)
        x = np.linalg.solve(a, C)
        print(a)
        print(C)
        print(x)



