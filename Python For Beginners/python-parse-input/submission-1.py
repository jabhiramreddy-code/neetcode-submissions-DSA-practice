from typing import List

def read_integers() -> List[int]:
    ans = input().split(",")
    for i in range(len(ans)):
        ans[i]=int(ans[i])
    return ans


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
