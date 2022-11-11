
# 1st line: Total shirt available
n_stock = input()

# 2nd Line input: Shirt size available
sizes_str = input().lower().split(' ')
sizes = [str(x) for x in sizes_str]

# 3rd line input: Number of requests
n_request  = input()

# 4th line: Requested sizes
requests_str = input().lower().split(' ')
requests = [str(x) for x in requests_str]

# Validating that n_stock >= n_request
if n_request > n_stock:
    print("No")
    quit()

# Encode size availables
size_conv = []
for i in sizes:
    x_count = 0;
    for xs in i:
        if xs == "x":
            x_count += 1
        else:
            last_char = xs
            
    if x_count == 0:
        size_parsed = last_char
    else:
        size_parsed = str(x_count) + "x" + last_char
    
    size_conv.append(size_parsed)

# Encode requests
requests_conv = []
for i in requests:
    x_count = 0;
    for xs in i:
        if xs == "x":
            x_count += 1
        else:
            last_char = xs
    
    if x_count == 0:
        size_parsed = last_char
    else:
        size_parsed = str(x_count) + "x" + last_char
    
    requests_conv.append(size_parsed)


# Evaluate requests
for i in requests_conv:
    digits = ''.join(x for x in i if x.isdigit())
    alpha = ''.join(x for x in i if x.isalpha())
    
    # Stub
    print ("Yes") # Remove later -- testing only
   