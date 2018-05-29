def composite_count(limit):
    answer = []
    most_divisors = 0
    for i in range(limit):
        tally = 0
        for j in range(i):
            if not (i + 1) % (j + 1):
                tally += 1
        if tally > most_divisors:
            most_divisors = tally
            answer.append((i + 1))
    for j in answer:
	g=j+(j+1)
	if g==limit:
		return j,j+1
print composite_count (int(raw_input()))
