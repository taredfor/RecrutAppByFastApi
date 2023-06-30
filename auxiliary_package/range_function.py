from random import randrange

class Range():
    def range_id(self, diapason: int):
        l_st = []
        while len(l_st) < 3:
            for i in range(1, diapason):
                l = randrange(1, diapason, 2)
                if l not in l_st:
                    l_st.append(l)
                if len(l_st) > 3:
                    break
        return l_st

if __name__ == "__main__":
    print(Range().range_id(12))

