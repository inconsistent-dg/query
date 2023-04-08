
# sequence = input("Enter a sequence: ")   # when this was just cli, prompt user for the sequence. uncomment (and get red of def) if you want a cli again

def calculate(sequence):
# Check if sequence is empty
    if len(sequence) == 0:
        print("ERROR: No sequence given.")
    else:
    # check if sequence contains any q's, as if so the output is always q
        if 'Q' in sequence:
            print("The output is: Q")
        elif 'q' in sequence:
            print("The output is: q")
    
        # if it doesn't, do this
        else:
            # count each input in sequence
            counts = {}
            for c in sequence:
                if c in counts:
                    counts[c] += 1
                else:
                    counts[c] = 1

            # check for modifiers
            if 'O' in counts and 'A' not in counts:
                output = max(counts, key=counts.get)
            elif 'A' in counts and 'O' not in counts:
                output = min(counts, key=counts.get)
            elif 'O' in counts and 'A' in counts:
                if counts['O'] >= counts['A']:
                    output = max(counts, key=counts.get)
                else:
                    output = min(counts, key=counts.get)
            else:
                output = max(counts, key=counts.get)

            print("The output is:", output)