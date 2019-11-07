import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier




def do_calculation(wt, block_info, KetVol):
  if (wt >100):
    MaxWt=100
  else:
    MaxWt=wt


  if (block_info == 1):
    vol,conc=30,0.25

  elif (block_info == 2):
    vol,conc=40,0.125

  else:
    vol,conc=0,0

  print(vol)




  maxBupiDose = MaxWt*2
  print(maxBupiDose)
  maxRopiDose = MaxWt*3
  print(maxRopiDose)






  fraction_LA_Used = round_half_up((vol*conc*10/maxBupiDose),2)
  print(fraction_LA_Used)
  fraction_LA_Remaining = round_half_up((1-fraction_LA_Used),2)
  print(fraction_LA_Remaining)
  RopiDoseHvlia = round_half_up((fraction_LA_Remaining*maxRopiDose),2)
  RopiVolHvlia = round_half_up((RopiDoseHvlia/2),0)
  if (block_info==2) and RopiVolHvlia>100:
    return 100 - KetVol - 1
  else:
    return RopiVolHvlia




def saline_vol(maxBlockVol, ropiVol, adVol, clonVol, KetVol, block_info):
  if (block_info == 3):
    maxBlockVol=150
  else:
    maxBlockVol=100

  salvol = maxBlockVol-ropiVol-adVol-clonVol-KetVol
  if salvol > 1:
    return salvol
  else:
    return 0
