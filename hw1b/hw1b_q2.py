
class Fibonacci:
    def __init__(self,limit):
        self.limit = limit
    def __iter__(self):
        self.prev = [0]
        return self
    def __next__(self):
        if len(self.prev) == 1:
            self.prev.append(1)
            return 1
        n = sum(self.prev)
        if n > self.limit:
            raise StopIteration
        self.prev[0],self.prev[1] = self.prev[1],n
        return n
        
if __name__ == "__main__":
    print(*Fibonacci(50))

