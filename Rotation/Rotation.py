#!/usr/bin/python
class Executor:

    @staticmethod
    def run(inputs):
        result = []
        ## init
        for char in list(inputs[0]):
            result.append(char)
        for ligne in inputs[1:]:
            tmp = list(ligne)
            for i in range(0, len(tmp)):
               result[i] = tmp[i] + result[i]
        print(result)
        return result

#["AAA","BBB","CCC] [['A','A','A]
#                    ['B','B','B']
#                    ['C','C','C']]
#['CBA','CBA','CBA']
Executor.run(['AAAA', 'BBBB', 'CCCC', 'DDDD'])