# 1. scope

x = 5

def carp():
  # 2. scope
  global t 
  t = 50

carp()

print(t) 
