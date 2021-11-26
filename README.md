# Fun & Games

Repository for random scripts I write to solve games easily, make processes more efficient, etc.

## Spelling bee

I have been playing the NYT Spelling Bee game for a bit now. You’re asked to build as many words as possible using the letters provided; words must be 4+ letters and contain the center letter. I got tired of waiting for the solutions so I wrote a quick Python script to solve the game.

Curious about how other devs would have written it, taking into account efficiency. My first instinct was a bottom up approach: starting with all possible combinations of letters provided and checking the dictionary for them but I quickly realized that wasn’t feasible b/c: 

(1) Words don’t have to be exactly 7 letters, (2) there is no limit to the length of the words, and (3) you can use a letter as many times as you want in the word. You can definitely hack your way around these issues but couldn’t find an efficient way to do it

So I switched to a top-down approach. I used the PyEnchant lib (NLTK works too), started with the whole English dictionary and narrowed it down to words that contained the center letter & didn’t contain any letter from the complement of the authorized letter set.

I didn’t pay much attention to efficiency while writing the script, but curious to know how you’d solve this game efficiently.
