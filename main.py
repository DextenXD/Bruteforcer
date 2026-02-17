password = "password"

with open('rockyou.txt', 'rt', encoding='latin-1') as f:
  attempt = 0
  for line in f:
    if password == line.strip():
      attempt =+ 1
      print(f"Password is {line.strip()}. It took {attempt} try")
      break
  else:
    print("Password not found. Try a different wordlist")
