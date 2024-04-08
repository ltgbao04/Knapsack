def load_data(filename):
    n, c = False, False
    try:
        with open(filename, 'r') as file:
            values, weights = [], []
            for line in file:
                parts = line.strip().split()
                if (len(parts) == 2):
                    values.append(int(parts[0]))
                    weights.append(int(parts[1]))
                
                elif(len(parts)==1):
                    if(not n):
                        number = int(parts[0])
                        n = True
                    elif(not c):
                        capacity = int(parts[0])
                        c = True
                    
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except Exception as e:
        print(e)
    
    return number, capacity, values, weights