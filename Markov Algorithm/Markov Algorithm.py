def markov_algorithm(input_string):
    rules = [
        ("A", "B"),
    ]

    while True:
        applied = False  # Flag to track whether a rule was applied in this iteration

        for pattern, replacement in rules:
            if pattern in input_string:
                input_string = input_string.replace(pattern, replacement)
                applied = True

        if not applied:
            break  # No rules were applied, so we're done

    return input_string

# Test the Markov algorithm
initial_string = "AAAAABAAA"
result = markov_algorithm(initial_string)
print("Initial String:", initial_string)
print("Final Result:", result)
