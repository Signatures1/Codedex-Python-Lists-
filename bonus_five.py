dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']
item_to_find = input("Enter the DNA sequence to find: ")
item_found = False
for dna in dna_sequence:
    if dna == item_to_find:
        item_found = True
        print("DNA sequence found:", dna)
        break
if item_found == False:
    print("DNA sequence not found.")
else:
    print("Search Completed.")