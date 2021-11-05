def twoSum(nums, target: int):
    mmap = {}
    
    for i, v in enumerate(nums):
        print(i, v)
        mtarget = target -v
        if mtarget in mmap:
            return [i, mmap[mtarget]]
                    
        mmap[v] = i

if __name__ == '__main__':
    print(twoSum([1,3,5,7,9], 8))
    