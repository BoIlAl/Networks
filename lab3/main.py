from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from generals import LoyalGeneral, TraitorGeneral

class GeneralProblemTask:
    def __init__(self, loyal: int, traitor: int) -> None:
        self.loyal_num = loyal
        self.traitor_num  = traitor
        self.generals = \
            [LoyalGeneral(i, self.traitor_num) for i in range(self.loyal_num)] + \
            [TraitorGeneral(self.loyal_num + i, self.traitor_num) for i in range(self.traitor_num)]
        
    def start(self) -> bool:
        
        with ThreadPoolExecutor() as executor:
            
            futures = []

            for general in self.generals:
                futures.append(executor.submit(general.start, self.generals))

            res = []
            for f in futures:
                
                if len(res) == 0:
                    res = f.result()
                    continue
                
                if res != f.result():
                    return False
            return True


def main():
    for k_l in range(2, 8):
        for k_t in range(0, k_l):
            general_task = GeneralProblemTask(k_l - k_t, k_t)
            print(k_l, k_t, general_task.start())
    


if __name__ == '__main__':
    main()