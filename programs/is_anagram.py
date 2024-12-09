s = 'jam'
t = 'jar'

def is_anagram(s,t):
    counts, countt={}, {}
    if len(s)!=len(t):
        return False
    for i in range(len(s)):
        counts[s[i]] = 1 + counts.get(s[i], 0)
        print(counts[s[i]])
        print(counts)

print(is_anagram(s,t))

my_dict = {}

for i in range(len(s)):
    print(my_dict.get(i), 0)
