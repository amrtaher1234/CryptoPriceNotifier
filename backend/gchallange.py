
# from typing import data


def solution(data, n):
    result = []
    for x in range(0, len(data)):
      myn = data[x]
      rep_data = [i for i in data if i== myn]
      if len(rep_data) < n:
        result.append(myn)
    
    return result



if __name__ == '__main__':
    print (solution([1,1,3,3,3,5,6,4], 2))
    print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
    solution([1, 2, 3], 0)
    solution([1, 2, 3], 0)