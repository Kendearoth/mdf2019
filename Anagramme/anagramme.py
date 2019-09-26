#!/usr/bin/python
class Executor:

    @staticmethod
    def run(inputs):
        print(inputs)
        results = []
        base = inputs[0]

        isAnagram = True
        for word in inputs[1:]:
            cp = list(word)
            for charB in base:
                if charB in cp:
                    cp.remove(charB)
                else:
                    isAnagram = False
                    break
            if cp == [] and base != word and len(base) == len(word):
                results.append(word)
        print(results)
        return results

Executor.run(["test", "estt"])