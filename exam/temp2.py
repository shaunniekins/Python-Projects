def compute_hash(subset):
    subset_str = ''.join(str(num) for num in subset)

    hash_value = hash_function(subset_str)

    return hash_value

def verify_subset(subset, provided_hash_value):
    computed_hash_value = compute_hash(subset)

    if computed_hash_value == provided_hash_value:
        return True
    else:
        return False

def hash_function(string):

    return hash_value

