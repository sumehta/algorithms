from collections import defaultdict

def anagram(st1, st2, k):
	if len(st1) != len(st2):
		return False

	hash = defaultdict(int)
	for i in range(len(st1)):
		hash[st1[i]]+=1
        hash[st2[i]]+=1

	if hash.values().count(1) <= k:
		return True

	return False


if __name__ == '__main__':
    print anagram('geeks', 'eggkf', 3)
