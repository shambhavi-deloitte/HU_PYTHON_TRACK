from itertools import combinations
#####################################
class StringClass:
    def __init__(self,s):
        self.s=s
        def StringLength(self):
            return len(self.s)
        def StringToListOfCharacters(self):
               return list(map(str,self.s))
        def GetString(self):
                return self.s

class PairsPossible(StringClass):
        def __init__(self,arr):
            self.arr=arr
            StringClass.__init__(self,arr)
            def StoreAllPossiblePairs(self):
                self.arr=list(combinations(self.s,2))

                def PrintAllPossiblePairs(self):
                        for i in self.arr:
                            print(list(i),end=' ')
                        print()
                        def GetAllPossiblePairs(self):
                            return self.arr
                            def GetString(self):
                                return self.s
class SearchCommonElements:
            def __init__(self,s,s1,s2):
                    self.s=s
                    self.s1=s1
                    self.s2=s2
            def SearchElements(self):
                res=[];dict1={};dict2={}
                for c in list(map(str,self.s)):
                    if c in list(map(str,self.s1)):
                        if dict1.get(c)==None:
                            dict1[c]=1
                        else:
                            dict1[c]+=1
                            if c in self.s2:
                                if dict2.get(c)==None:
                                    dict2[c]=1
                                else:
                                    dict2[c]+=1
                                    res=[len(dict1),len(dict2)]

class EqualSumPairs:
        def __init__(self,arr):
            self.arr=arr
            def CountPairs(self):
                temp_counts=[];res=0
                for pair in self.arr:
                        s=0
                        s = int(list(pair)[0]) + int(list(pair)[1])
                        if s not in temp_counts:
                            res+=1;temp_counts.append(s)
                        print(res)
                        SObj = StringClass("12314532")
                        print(SObj.StringLength())
                        print(SObj.StringToListOfCharacters())
                        PObj=PairsPossible(SObj.StringToListOfCharacters())
                        PObj.StoreAllPossiblePairs()
                        PObj.PrintAllPossiblePairs()
                        S2Obj=SearchCommonElements("testString",SObj.GetString(),PObj.GetString())
                        S2Obj.SearchElements()
                        EObj=EqualSumPairs(PObj.GetAllPossiblePairs())
                        EObj.CountPairs()