results = {
    "prince": 98,
    "sydwell": 78,
    "paul": 65,
    "matome": 26,
    "moses": 82,}

new_results = {}

for key in results:
    if results[key] >= 91:
        new_results[key] = "Outstanding"
    elif results[key] >= 81:
        new_results[key] = "Exceeds Expectation"
    elif results[key] >= 71:
        new_results[key] = "Acceptable"
    elif results[key] <= 70:
        new_results[key] = "fail"

print(f'new dictionary {new_results}')
