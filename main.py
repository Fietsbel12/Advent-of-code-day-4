def parse_section(section):
    start, end = map(int, section.split('-'))
    return start, end

# Lees de sectieparen uit het bestand 'data.txt'
with open("data.txt", "r", encoding="UTF-8") as dataFile:
    section_pairs = dataFile.readlines()

total = 0
for line in section_pairs:
    line = line.strip()
    if line:  # Controleer of de regel niet leeg is
        pair = line.split(',')
        a, b = parse_section(pair[0])
        c, d = parse_section(pair[1])

        # Wissel ze zodat de eerste begint voordat de tweede begint.
        if (a > c) or (a == c and d > b):
            a, b, c, d = c, d, a, b

        # Controleer of het tweede paar volledig binnen het eerste paar valt.
        if a <= c and b >= d:
            total += 1

print(total)
