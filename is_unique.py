def is_unique(s):

	storage = set()
	for c in s:
		if c in storage:
			return False
		storage.add(c)
	return True

def is_unique_use_existing_string(s):

	for idx, val in enumerate(s):
		if val in s[:idx]:
			return False
	return True

def is_unique_ascii(s):

	mapped = [False] * 127
	for c in s:
		if mapped[ord(c)]:
			return False
		mapped[ord(c)] = True
	return True

def test():
    is_unique()
