class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
        
        def my_key(pp):
            return -pp[0],pp[1]#表示按第一个键降序 第二个键升序
        people.sort(key=my_key)
        for i in range(len(people)):
            if i>=len(people):
                break
            if(people[i][1]==i):
                continue
            tmp=people[i]
            people.pop(i)
            people.insert(tmp[1],tmp)
        return people
