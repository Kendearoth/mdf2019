#!/usr/bin/python
class Executor:

    @staticmethod
    def run(inputs):
        print(inputs)
        result = 'false'
        i = 0
        while i < len(inputs)-1:
            segment = inputs[i:i+2]
            print(segment)
            #on cherche si ce segment existe dans le reste du trajet
            j = i+2
            while j < len(inputs)-1:
                print('test:'+str(inputs[j:j+2]))
                if segment == inputs[j:j+2]:
                    result = 'true'
                    break
                j+=1
            i+=1
        print(result)
        return [result]


Executor.run(['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Marseille', 'Lyon', 'Toulouse', 'Poitiers'])