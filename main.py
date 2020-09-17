# Author: Joshua McIntyre jjm7410@psu.edu
# Collaborator: Finn Thompson fet5024@psu.edu  
# Collaborator: Caleb Frantz cmf6208@psu.edu  
# Collaborator: Abishek apv5314@psu.edu 
# Section: 4
# Breakout: 18

def sum_n(n): 
  if (n==0):
    return
  else:
    return n + sum_n(n-1)

def print_n(s,n):
  if (n > 0):
    print(f"{s}")
    print_n(s,n-1)


def run()
  n = int(input("Enter an int: "))
  print(f"sum is {sum_n(n)}.")
  s = input("Enter a string: ")
  print(f"{print_n(s,n)}")

  if__name__ == "__main__":
    run()