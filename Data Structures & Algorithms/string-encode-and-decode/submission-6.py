class Solution:
    encoder = ";asldkjf439i5"
    def encode(self, strs: List[str]) -> str:
        encoder = ";asldkjf439i5"
        # ans=""
        # for i in strs:
        #     ans += i + encoder
        # return ans
        return (encoder).join(strs)+"..."+str(len(strs))

    def decode(self, s: str) -> List[str]:
        encoder = ";asldkjf439i5"
        res = s.split("...")
        print(res)
        if res[1] != '0':
            return res[0].split(encoder)
        return []
