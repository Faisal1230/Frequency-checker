lst = ['apple','graphes','nemo','apple','graphes','nemo','apple','graphes','nemo']

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

num_1 = [1,2,3,4,1,1,1,1,1,1,2,2,2,2,3,3,3,3]
id = freq(num_1)
print(id)