```python
inventario= [
    [10, 4, 8],
    [5, 12, 3],
    [7, 20, 6],
]

total=0 

for fila in inventario:
    for cantidad in fila:

        if cantidad > 5 and cantidad %2 ==0:
            total += cantidad

print(f"la cantidad de frutas son: {total}")
```