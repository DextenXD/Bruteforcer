import time

password = "123456"
start_time = time.perf_counter()

with open('rockyou.txt', 'rt', encoding='latin-1') as f:
  attempt = 0
  for line in f:
    attempt += 1
    if password == line.strip():
      end_time = time.perf_counter()
      elapsed = end_time - start_time
      print(f"Password is {line.strip()}. It took {attempt} try, Time eslapsed: {elapsed:.6f} seconds.")
    
      break
  else:
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"Password not found. Try a different wordlist Time eslapsed: {elapsed:.6f} seconds.")
