import pyfpgrowth

# Example dataset
dataset = [['bread', 'milk'],
           ['bread', 'diaper', 'beer', 'eggs'],
           ['milk', 'diaper', 'beer', 'cola'],
           ['bread', 'milk', 'diaper', 'beer'],
           ['bread', 'milk', 'diaper', 'cola']]

# Use the pyfpgrowth library to find frequent itemsets
patterns = pyfpgrowth.find_frequent_patterns(dataset, 2)
rules = pyfpgrowth.generate_association_rules(patterns, 0.6)

# Print the frequent itemsets and association rules
print("Frequent Itemsets:")
print(patterns)

