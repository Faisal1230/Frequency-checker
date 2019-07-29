# Frequency-checker
<ul>
Find fequency of your list.
    </ul>

<h3>Source Code</h3>

```lst = ['apple','graphes','nemo','apple','graphes','nemo','apple','graphes','nemo']

def freq():
    frequency = {}
    for x in lst:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1
    return frequency

new = freq()
print(new)
```
<h3>Output</h3>

{'apple': 3, 'graphes': 3, 'nemo': 3}
