def anagram(s1, s2):
    if(sorted(s1) == sorted(s2)):
        print("Anagrams")
    else:
        print("Aren't anagram")

s1 = "listen"
s2 = "silent"

anagram(s1,s2)