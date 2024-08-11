from itertools import combinations

l, c = map(int, input().split())
letters = input().split()

vowel = []
consonant = []

for letter in letters:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        vowel.append( letter )
    else:
        consonant.append( letter )

ans = []

for vowel_size in range(1, l-1):
    vowel_combination = list(combinations(vowel, vowel_size))
    consonant_combination = list(combinations(consonant, l-vowel_size))
    for vowel_comb in vowel_combination:
        for consonant_comb in consonant_combination:
            curr_combination = list(vowel_comb) + list(consonant_comb)
            curr_combination.sort()
            curr_key = ''.join( curr_combination )
            ans.append( curr_key )

ans.sort()

for key in ans:
    print(key)    
