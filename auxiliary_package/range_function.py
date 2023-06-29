
class Range():
    def range_id(self, diapason: int):
        l_st = []
        for i in range(1, diapason, 2):
            l_st.append(i)
        return l_st

if __name__ == "__main__":
    print(Range.range_id(6))