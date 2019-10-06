import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def do_calculation(wt, block_type):
  if (wt >100):
    MaxWt=100
  else:
    MaxWt=wt

  maxBupiDose = MaxWt*2
  print(maxBupiDose)
  maxRopiDose = MaxWt*3
  print(maxRopiDose)
  block_type = 2
  if block_type == 1:
    vol = 30
    conc = 0.25

  elif block_type == 2:
    vol = 40
    conc = 0.125


  fraction_LA_Used = round_half_up((vol*conc*10/maxBupiDose),2)
  print(fraction_LA_Used)
  fraction_LA_Remaining = round_half_up((1-fraction_LA_Used),2)
  print(fraction_LA_Remaining)
  RopiDoseHvlia = round_half_up((fraction_LA_Remaining*maxRopiDose),2)
  print(RopiDoseHvlia)


  return round_half_up((RopiDoseHvlia/2),0)

def saline_vol(maxSalVol, ropiVol, adVol, clonVol, KetVol):
  if (ropiVol>maxSalVol):
    maxSalVol=ropiVol+KetVol+clonVol+adVol
  else:
    maxSalVol=maxSalVol
  return maxSalVol-ropiVol-adVol-clonVol-KetVol



saline = saline_vol(100,do_calculation(110,1),0.5,0.5,1)
print ("saline vol =" + str(saline) + " " + "mls")




final_vol = round_half_up(do_calculation(110,1),0)
print(final_vol)
