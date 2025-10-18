import csv
import sys


def main():

    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]


    with open(database_file) as file:
        reader = csv.DictReader(file)
        str_names = reader.fieldnames[1:]
        database = list(reader)


    with open(sequence_file) as file:
        dna_sequence = file.read().strip()


    dna_profile = {}
    for str_name in str_names:
        dna_profile[str_name] = longest_match(dna_sequence, str_name)


    for person in database:
        match = all(int(person[str_name]) == dna_profile[str_name] for str_name in str_names)
        if match:
            print(person["name"])
            return

    
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subseq_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while True:
            start = i + count * subseq_len
            end = start + subseq_len
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
