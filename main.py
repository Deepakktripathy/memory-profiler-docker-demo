from memory_profiler import profile

@profile(stream=open('memory_profile.log', 'w'))
def something():
    large_list = []
    
    # Operation 1: Appending elements
    for i in range(10_000):
        large_list.append(f"element_{i}_" + "x" * 10)  
    
    # Operation 2: Reading elements  
    read_count = 0
    for i in range(5000):
        value = large_list[i]  # Read operation
        read_count += 1
    
    return len(large_list)

if __name__ == "__main__":
    final_size = something()
    
    print(f" Final list size: {final_size} elements")
    print("Check the following log files:")
    print("- memory_profile.log")