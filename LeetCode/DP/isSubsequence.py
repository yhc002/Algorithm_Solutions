def isSubsequence(self, s: str, t: str) -> bool:
        while len(s)>0:
            idx=t.find(s[0])
            if idx==-1:
                return False
            t=t[idx+1:]
            s=s[1:]
        return True
