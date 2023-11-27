# Consigne : Trouver le plus grand élément d'une liste d'entiers

lst = [18,4,5,4,9,20,46,45,2,94,7]

def max_dans_liste(arr):
    max = 0
    for element in arr:
        if element > max:
            max = element
    return max

print(f"Le plus grand élément de la liste est : {max_dans_liste(lst)}")