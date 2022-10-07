class DataCollector:
    
    @classmethod
    def collect(cls, starts, ends, data):
        collected_data = []
        nums_to_merge = []
        for num in data:
            if num not in starts and num not in ends:
                nums_to_merge.append(num)
                continue
            if num in starts:
                collected_data += nums_to_merge
            elif num in ends:
                collected_data += cls.__merge(nums_to_merge)
            nums_to_merge = []
            collected_data.append(num)

        should_merge_leftover_nums = len(nums_to_merge) != 0 and len(nums_to_merge) < len(data) and data[-(len(nums_to_merge) + 1)] in starts
        if should_merge_leftover_nums:
            collected_data += cls.__merge(nums_to_merge)
        else:
            collected_data += nums_to_merge

        return collected_data

    @staticmethod
    def __merge(nums_to_merge):
        if nums_to_merge == []:
            return []
        
        merged_num = 0
        for num in nums_to_merge:
            merged_num = merged_num * 10 + num

        return [merged_num]

if __name__ == "__main__":
    output = DataCollector.collect([1,2], [8,9], [1,5,4,8,2,8,9,5,6])
    output_merge_leftover_nums = DataCollector.collect([1,2], [8,9], [1,5,6,2,3,4,5,8,1,4,5,0])
    print(output)
    print(output_merge_leftover_nums)
    