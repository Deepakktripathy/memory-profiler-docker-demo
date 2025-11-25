from memory_profiler import profile

@profile(stream=open('memory_profile.log', 'w'))
def something():
    large_list = []
    
    # Appending elements
    for i in range(10_000):
        large_list.append(f"element_{i}_" + "x" * 10)  
    
    #  Reading elements  
    read_count = 0
    for i in range(5000):
        value = large_list[i]  
        read_count += 1

     # NEW operation: Modify some elements
   
    for i in range(500):
        large_list[i] = f"modified_{i}_" + "z" * 5
    
    total_memory_estimate = len(large_list) * 8  # bytes per integer
    print(f"List statistics: {len(large_list)} elements, ~{total_memory_estimate} bytes estimated")

    return len(large_list)

if __name__ == "__main__":
    final_size = something()
    
    print(f" Final list size: {final_size} elements")
    print(f"Check logs in {memory_profile.log}")

