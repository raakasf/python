# This imports the ThreadPoolExecutor class from the concurrent.futures module.
# ThreadPoolExecutor allows you to run functions in separate threads without managing threads manually.
from concurrent.futures import ThreadPoolExecutor
def task(x): return x * 2
# This line creates a thread pool executor using a context manager (with block).
# The context manager ensures that the thread pool is properly shut down when the block ends (no need to manually call shutdown()).
with ThreadPoolExecutor() as ex:
	# This submits the function task with argument 3 to the executor.
	# ex.submit() returns a Future object (f in this case), which acts like a placeholder for the result of the task.
	# The task runs in a separate thread from the main program.
	f = ex.submit(task, 3)
	# f.result() waits for the thread to complete (if it hasn’t already), and then returns the result.
	print(f.result())
