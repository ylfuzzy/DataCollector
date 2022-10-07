class DataCollector:
    
    @classmethod
    def collect(cls, starts, ends, data):
        collectedData = []
        numsToMerge = []
        for num in data:
            if num not in starts and num not in ends:
                numsToMerge.append(num)
                continue
            if num in starts:
                collectedData += numsToMerge
            elif num in ends:
                collectedData += cls.__merge(numsToMerge)
            numsToMerge = []
            collectedData.append(num)
        collectedData += numsToMerge
        return collectedData

    @staticmethod
    def __merge(numsToMerge):
        if numsToMerge == []:
            return []
        mergedNum = 0
        for num in numsToMerge:
            mergedNum = mergedNum * 10 + num
        return [mergedNum]

if __name__ == "__main__":
    output = DataCollector.collect([1,2], [8,9], [1,5,4,8,2,8,9,5,6])
    print(output)
    