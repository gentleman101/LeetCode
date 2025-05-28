class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)

        def key_process(st):
            final_string = ""
            
            dis = ord(st[0])-ord('a')
            
            for char in st:
                new_char = chr((ord(char)-dis)%26)
                final_string += new_char
            return (final_string)      
                
        for s in strings:
            dict_key = key_process(s)
            res_dict[dict_key].append(s)      

        return ([x for x in res_dict.values()])