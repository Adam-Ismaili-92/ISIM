import timeit, cProfile

def benchmark_time(pipeline):
    num_runs = 5
    elapsed_time = timeit.timeit(pipeline, number=num_runs)
    average_time = elapsed_time / num_runs
    print(f"Average execution time: {average_time:.2f} seconds")


def benchmark_profile():
    cProfile.run("pipeline()")
