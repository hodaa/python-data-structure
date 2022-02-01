# class Solution(object):
#     my_dict ={}
#     def minDeletions(self, s):
#         for i in range(len(s)):
#             # print(s[i])
#             if s[i] in self.my_dict.keys():
#                 self.my_dict[s[i]] =  self.my_dict[s[i]]+1
#                 # print("yes")
#             else:
#                 self.my_dict[s[i]] = 1
#                 # print( "no")
                
#         key_list = list(self.my_dict.keys())
#         val_list = list(self.my_dict.values())
        
#         i=1;
#         for char in self.my_dict:
#             # print(i)
#             print(val_list[1])
#             if i < len(val_list):
#                 # position = val_list[i:].index(self.my_dict[char])
#                 # print(position)
#                 # i+=1
                
#             # if self.r[char] in  self.r.values():
#                 # print("ye")
#             # print(char)
#             # print(self.r.values())
#             # print(list(self.r))
            
#         # print(self.r)
#         """
#         :type s: str
#         :rtype: int
#         """
        

from collections import Counter
s= Counter('aab')
print(sorted(s.values(),True))