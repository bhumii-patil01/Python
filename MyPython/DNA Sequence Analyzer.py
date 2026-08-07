# DNA SEQUENCE ANALYZER

print("-" * 50)
print(" Welcome to DNA Sequence Analyzer ")

# Step 1: Input DNA sequence
dna = input("Enter DNA sequence (A, T, G, C only): ").upper()

# Step 2: Validate DNA sequence
valid = True
for base in dna:
    if base not in "ATGC":
        valid = False
        break

if valid:
    print("\nValid DNA Sequence Detected!")

    # Step 3: Length of DNA
    length = len(dna)

    # Step 4: Count nucleotides
    A = dna.count("A")
    T = dna.count("T")
    G = dna.count("G")
    C = dna.count("C")

    # Step 5: GC Content
    gc_content = ((G + C) / length) * 100

    # Step 6: Complementary DNA
    # DNA base pairing dictionary
    base_pair = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    complement = ""

    for base in dna:
        complement += base_pair[base]

    # Step 7: Reverse Complement
    reverse_complement = complement[::-1]

    # Step 8: DNA → RNA Transcription
        #rule
            # T → U
    rna = dna.replace("T","U")

    print("-" * 50)
    print("\nDNA ANALYSIS REPORT")
    print(f"Entered DNA sequence :{dna}")
    print(" 1.Sequence Length :", length)
    print(" 2.A Count :", A)
    print("   T Count :", T)
    print("   G Count :", G)
    print("   C Count :", C)
    print(" 3.GC Content : {:.2f}%".format(gc_content))
    print(" 4.Complementary Strand :", complement)
    print(" 5.Reverse Complement :", reverse_complement)
    print(" 6.RNA Sequence :", rna)
    print("-" * 50)

    print("MUTATION DETECTION")

    # Step 9: Input DNA2 for mutation detection
    dna2 = input("Enter another DNA sequence (A, T, G, C only):").upper()

    # Step 10: Validate DNA sequence
    valid = True
    for base in dna2:
        if base not in "ATGC":
            valid = False
            break

    if valid:
        #Step 11: Count total number of mutations
        if len(dna) != len(dna2):
            print("Sequences must be of equal length to compare mutations.")
        else:
            mutations = 0

            for i in range(len(dna)):
                if dna[i] != dna2[i]:
                    mutations += 1
                    print("Mutation at position", i+1, ":", dna[i], "→", dna2[i])

            print("Total Mutations Detected :", mutations)

    else:
        print("\n Invalid DNA Sequence! Please enter only A, T, G, C")
    
    print("-" * 50)


else:
    print("\n Invalid DNA Sequence! Please enter only A, T, G, C")
    print("-" * 50)