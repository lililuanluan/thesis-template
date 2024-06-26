import matplotlib.pyplot as plt

# 从文件读取数据

def process_file(file_path):   

    with open(file_path, 'r') as file:
        lines = file.readlines()
        y = []

        for line in lines:
            parts = line.strip().split()
            y.append(int(parts[1]))
        return y
    
    
def plot_data(rnd, fz, test_name):
    
    plt.title(test_name)
    plt.plot(range(1, len(rnd) + 1), rnd, label="rand")
    plt.plot(range(1, len(fz) + 1), fz, label="fuzz")
    # plt.plot(range(1, len(unique_bugs_rnd) + 1), unique_bugs_rnd, label="unique bugs rand")
    # plt.plot(range(1, len(unique_bugs_mut) + 1), unique_bugs_mut, label="unique bugs mutate")
    plt.xlabel("Time")
    plt.ylabel("Counts")
    plt.legend()
    plt.savefig(test_name + ".png")
    plt.close()

if __name__ == "__main__":
    for test in ["big00", "mpmc-queue"]:
        rd = process_file(test + "-rnd.txt")
        fz = process_file(test + "-fz.txt")
        plot_data(rd, fz, test)