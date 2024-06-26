import sys
import os

def process_file(filename):
    hash_set = set()
    success_count = 0
    failure_count = 0
    unique_failures = set()
    total_count = 0

    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith('HASH'):
                hash_val = line.split()[1]
                hash_set.add(hash_val)
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
    return hash_set, success_count, failure_count, unique_failures, total_count

def print_statistics(HASH_FILE):
    filename = HASH_FILE
    hash_set, success_count, failure_count, unique_failures, total_count = process_file(filename)

    parts = filename.split("_", 1)
    extracted_part = parts[0]
    # print(f"TEST: {extracted_part}")
    print("Total different hashes: {} {:.1f}%".format(len(hash_set), 100 * len(hash_set) / total_count))
    # print("Total successful executions: {} {:.2f}%".format(success_count, 100 * success_count / total_count))
    # for hash_val in hash_set:
    #     print(hash_val)
    print("Total failed executions: {} {:.1f}%".format(failure_count, 100 * failure_count / total_count))
    print("Total different failures: {} {:.1f}%".format(len(unique_failures), 100 * len(unique_failures) / total_count))
    print("Total:", total_count)
    
def print_table_with_data(tests, metrics, data):
    table_width = max(len(header) for header in metrics) + 1
    # input(f"table width = {table_width}")   # 16
    
    # 打印左上角空白
    print(" " * table_width, end=" | ")

    # 打印第一行表头
    for header in tests:
        print(f"{header:^{table_width}}", end=" | ")
    print()

    # 打印分隔线
    print("-" * table_width, end="-|-")
    print("-" * ((table_width + 2) * len(tests) + 5 ), end = "-|\n")

    # 打印表格数据
    for i, header in enumerate(metrics):
        # input()
        print(f"{header:<{table_width}}", end=" | ")
        for j, col in enumerate(data):
            
            d = f"{col[i]:.1f}" + " %"
            print(f"{d:^{table_width}}", end=" | ")
        print()

def print_table(file_postfix, is_c11tester = False):
    tests = ["barrier", "chase-lev-deque", "mpmc-queue", "linuxrwlocks", "mcs-lock", "dekker-change", "rwlock-test", "seqlock-test"]
    metrics = ["uniq executions", "bug rate", "uniq bug rate"]
    
    data = []
    
    print(">>>>>>  " + ["fuzzer:", "c11tester:"][is_c11tester])
    
    # print("tests: ", end='\t')
    for test in tests:
        hash_set, success_count, failure_count, unique_failures, total_count = process_file(test + file_postfix)
        data.append([100 * len(hash_set) / total_count, 100 * failure_count / total_count, 100 * len(unique_failures) / total_count])
        
    print_table_with_data(tests, metrics, data)



if __name__ == "__main__":
    print_table(".txt", is_c11tester=True)
    print()
    print()
    print_table("_hashes2.txt", is_c11tester=False)
    # tests = ["barrier", "chase-lev-deque", "mpmc-queue", "linuxrwlocks", "mcs-lock", "dekker-change", "rwlock-test", "seqlock-test"]
    # for t in tests:
    #     # os.system("ls")
    #     os.system(f"touch {t}.txt")
    #     os.system(f"touch {t}_hashes2.txt")

