

if __name__ == '__main__':
    print(f"number of seeds {len(Seeds)}")
    counts = {}
    for item in Seeds:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    
    print("repeated seeds:")
    for item, count in counts.items():
        if count > 1:
            print(f"{item}: {count}")
    
    print(f"unique number of seeds {len(counts)}")