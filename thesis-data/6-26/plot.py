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



def plot_data(unique_hashes_rnd, unique_hashes_mut, unique_hashes_pct, unique_bugs_rnd, unique_bugs_mut, unique_bugs_pct, test_name):
    
    plt.title(test_name)
    plt.plot(range(1, len(unique_hashes_rnd) + 1), unique_hashes_rnd, label="C11Tester")
    plt.plot(range(1, len(unique_hashes_mut) + 1), unique_hashes_mut, label="C11Fuzzer")
    plt.plot(range(1, len(unique_hashes_pct) + 1), unique_hashes_pct, label="PCTWM")
    # plt.plot(range(1, len(unique_bugs_rnd) + 1), unique_bugs_rnd, label="unique bugs rand")
    # plt.plot(range(1, len(unique_bugs_mut) + 1), unique_bugs_mut, label="unique bugs mutate")
    plt.xlabel("Number of iterations")
    plt.ylabel("Number of unique execution graphs")
    plt.legend()
    plt.savefig(test_name + ".pdf")
    plt.close()

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python script.py <input_filename>")
    #     sys.exit(1)
    
    # input_filename = sys.argv[1]
    # tests = ["barrier",  "chase-lev-deque",  "dekker-change",  "mcs-lock",  "rwlock-test", "left_right", "ring_buf", "bipartite_buf"]
    tests = ["barrier",  "chase-lev-deque",  "mpmc-queue", "mcs-lock",  "seqlock-test",  "rwlock-test",  "linuxrwlocks"]
    for input_filename in tests:
        test_name = os.path.splitext(input_filename)[0]
        
        unique_hashes_rnd, unique_bugs_rnd, _ = process_file("../5-21/" + input_filename + ".txt")
        unique_hashes_mut, unique_bugs_mut, _ = process_file("../5-21/" + input_filename + "_hashes2.txt")
        unique_hashes_pct, unique_bugs_pct, _ = process_file(input_filename + "_pct.txt")
        plot_data(unique_hashes_rnd, unique_hashes_mut, unique_hashes_pct, unique_bugs_rnd, unique_bugs_mut, unique_bugs_pct, test_name)