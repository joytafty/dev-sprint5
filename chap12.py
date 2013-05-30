# This is where the answers to Chapter 12 questions
# Name: Tharathorn (Joy) Rimchala

# Exercise 12.4 (more anagram)

def madewlist(fin):
	wl = []
	for line in fin:
		ww = line.strip()
		wl.append(ww)
	return wl

def all_anagram(wl):
	c = {}
	i = 0
	for w in wl:
		f = ''.join(sorted(w))
		if f not in c:
			c[f] = [w]
			i =+ 1
		else:
			c[f].append(w)
	return c

def print_anaset(dl):
	for an in dl:
		print an[1]

def print_all_anagram(c):
	d = {}
	for an in c.values():
		if len(an) > 1:
			wkey = ''.join(sorted(an[0]))
			d[wkey] = an
	# Print anagram	
	print_anaset(d)
	return d

def print_ordered_anaset(d):
	# Find key length
	dl = []
	for ank in d.values(): 
		dl.append((len(ank), ank))
	
	# Sort anagram list by length
	dl.sort()
	dl.reverse()
	# Print anagram	
	print_anaset(dl)
	return dl

def filter_wordlength(d, nb):
	db = {}
	for ank in d.keys():
		if (len(ank) == nb):
			db[ank] = d[ank]

	return db

def calc_frequency(db):
	df = []
	for ank in db.keys():
		df.append((len(db[ank]), db[ank]))

	return df

def find_most_frequent(df):
	df.sort()
	df.reverse()
	return df[0]

# Load word file
fin = open('words.txt')
# Make word list
wl = madewlist(fin)
# Find anagrams in word list
c = all_anagram(wl)
# Exercise 12.4 part 1: Print all anagram sets
d1 = print_all_anagram(c)
# Exercise 12.4 part 2: Print anagram ordered by number of elements
d2 = print_ordered_anaset(d1)
# Exercise 12.4 part 3: Find most frequent BINGO words
nb = 8
d3 = filter_wordlength(d1, nb)
df = calc_frequency(d3)
dftop = find_most_frequent(df)
print dftop
