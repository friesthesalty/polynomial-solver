# functions also used previously in cubic
def quad(a, b, c):
  """
  modified to return list instead of tuple for cubic
  """
  dis = b**2 - 4*a*c
  if dis > 0:
    x1 = (-b+(dis)**0.5)/(2*a)
    x2 = (-b-(dis)**0.5)/(2*a)
    return [x1, x2]
  elif not dis:
    return (-b+(dis)**(1/2))/(2*a)
  else:
    x = -b/(2*a)
    imagine = ((-dis)**0.5)/(2*a)
    return [complex(x, imagine), complex(x, -imagine)]
  
def fact(n):
  """
  returns positive factors of a number including 1 and itself.
  """
  return [x for x in range(1, abs(n)+1) if not n % x]

def zero_check(test_case, power, coefficients:list): # RETURNS TRUE IF ZERO
  """
  Can confirm this works.
  """
  res = 0
  for coefficient in coefficients:
    res += coefficient*test_case**power
    power -= 1
  if abs(res) < 1e-10:
    return 1
  return 0

def finding_zero(p, q, power, coefficients:list):
  """
  Probably working.
  """
  for i in p:
    for j in q:
      check = i/j
      if zero_check(check, power, coefficients):
        return check
  # negatives
  for i in p:
    for j in q:
      check = -i/j
      if zero_check(check, power, coefficients):
        return check
  return None 

# main
def poly(*args):
  """
  Find roots of any polynomial if there are less than 3 irrational roots.

  Does not have type check.
  """
  roots = []
  
  coefficients = list(args) # needs a mutable ver

  # strip trailing zeros from the left
  i = 0
  while i < len(coefficients) and not coefficients[i]:
    i += 1
  coefficients = coefficients[i:]

   
  # trailing zero on the right
  if not coefficients[-1]: # factor out x since there is no constant
    roots.append(0)
    coefficients = coefficients[:-1] # delete unnecessary zero
  # print(coefficients)
  
  power = len(coefficients)-1 


  # other cases
  if power == 0:
    return "Please enter at least two arguments."
  if power == 1:
    return -coefficients[1]/coefficients[0]
  if power == 2: # pretty sure this is unecessary actually
    return quad(coefficients[0], coefficients[1], coefficients[2])
  
  
  # the main action now...
  p = fact(coefficients[-1])
  q = fact(coefficients[0])

   
  while len(coefficients) > 3:
    # time for the synthetic division
    new = []
    quo = finding_zero(p, q, power, coefficients)
    if quo == None:
      return "No rational roots."
    roots.append(quo)
    

    for inx, val in enumerate(coefficients):
      if not inx:
        new.append(val)
      else:
        new.append(val + quo*new[inx-1])

    if new[-1]:
      return "Division error?"
    
    # print(new)
    # print(coefficients)
  
    coefficients = new[:-1]


  # find last two roots using quadratic
  # print(coefficients)
  last = quad(coefficients[0], coefficients[1], coefficients[2])
  roots.append(last[0])
  roots.append(last[1])
  return roots
  
  
print(poly(6,2))
print(poly(1, 9, -35, -405, -866, -504))
print(poly(1, -1, -42, -104, -64, 0))
print(poly(6, 0, 0))



# TEST CASE 1, 9, -35, -405, -866, -504
# EXPECTED ROOTS ARE -2, -4, -9, 7, -1

