import sys
import os.path
import matplotlib.pyplot as plt



def process_file(filename):
    hash_set = set()
    success_count = 0
    failure_count = 0
    unique_failures = set()
    total_count = 0
    
    unique_hashes_over_time = []
    unique_bugs_over_time = []
    bugs_over_time = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith('HASH'):
                hash_val = line.split()[1]
                hash_set.add(hash_val)
                unique_hashes_over_time.append(len(hash_set))
                if i < len(lines) - 1 and lines[i + 1].strip() == 'Aborted. Execution: 1':
                    failure_count += 1
                    if hash_val not in unique_failures:
                        # print("{}".format(total_count))
                        pass
                    unique_failures.add(hash_val)
                    
                else:
                    success_count += 1
                # print(f"{total_count} {len(hash_set)} {len(unique_failures)}")
                total_count += 1
                bugs_over_time.append(failure_count)
                unique_bugs_over_time.append(len(unique_failures))
            
            
            
    
    return unique_hashes_over_time, unique_bugs_over_time, bugs_over_time



def plot_data(unique_hashes_over_time, unique_bugs_over_time, bugs_over_time, test_name):
    
    plt.title(test_name)
    plt.plot(range(1, len(unique_hashes_over_time) + 1), unique_hashes_over_time, label="unique hashes over time")
    plt.plot(range(1, len(unique_hashes_over_time) + 1), range(1, len(unique_hashes_over_time) + 1), label="number of executions")
    plt.plot(range(1, len(unique_bugs_over_time) + 1), unique_bugs_over_time, label="unique bugs over time")
    plt.plot(range(1, len(bugs_over_time) + 1), bugs_over_time, label="bugs over time")
    plt.xlabel("Time")
    plt.ylabel("Counts")
    plt.legend()
    plt.savefig(test_name + ".png")
    plt.close()

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python script.py <input_filename>")
    #     sys.exit(1)
    
    # input_filename = sys.argv[1]
    for input_filename in ["barrier.txt",  "chase-lev-deque.txt",  "dekker-change.txt",  "linuxrwlocks.txt",  "mcs-lock.txt",  "mpmc-queue.txt",  "rwlock-test.txt",  "seqlock-test.txt"]:
        test_name = os.path.splitext(input_filename)[0]
        
        unique_hashes_over_time, unique_bugs_over_time, bugs_over_time = process_file(input_filename)
        plot_data(unique_hashes_over_time, unique_bugs_over_time, bugs_over_time, test_name)
