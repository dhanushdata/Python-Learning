languages = ["python", "java", "python", "c", "java", "python"]

counts = {}

for language in languages:

    if language in counts:
        counts[language] = counts[language] + 1

    else:
        counts[language] = 1

print(counts)