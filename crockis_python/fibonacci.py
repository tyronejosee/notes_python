def fibonacci():
    anterior = 0
    siguiente = 1
    for index in range(0,51):
        #print(index)
        temporal = anterior+siguiente
        anterior = siguiente
        siguiente = temporal
        print(anterior)

fibonacci()
