dictionar = {"cheie":"valoare","cheie1":"3"}

dictionar['cheie2'] =5
dictionar.update({'cheie2':8})
print(dictionar)
print(dictionar.keys())
print(dictionar.values())
print(dictionar.get('cheie2',5))