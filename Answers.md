**Решение:**
```python
text = input("Введите строку: ").lower().replace(" ", "")
freq_dict = {}

for char in text:
    if char.isalpha():
        freq_dict[char] = freq_dict.get(char, 0) + 1

print(freq_dict)
```
==================================
**Решение:**
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
new_dict = {**dict1, **dict2}

print(new_dict)
```
