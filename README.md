# Frequency-checker
## Find fequency of your list.

###Code
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
print(new)```
