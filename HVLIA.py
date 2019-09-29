





wt = float(input("Enter the patient's weight in Kg: "))
vol = float(input("Enter the volume of LA used in the block (mls): "))
conc = float(input("Enter the concentration of LA used in the block (%): "))

maxBupi = 2
maxRopi = 3

def maxLocalDose(wt,maxDose):
  if (wt >100):
    wt=100
  else:
    wt=wt
  return wt*maxDose

maxBupiDose = maxLocalDose(wt,maxBupi)
maxRopiDose = maxLocalDose(wt,maxRopi)

print(maxBupiDose)
print(maxRopiDose)

def blockDose(vol,conc,maxLocalDose):
  return vol*conc*10/maxBupiDose

fraction_LA_Used = blockDose(vol,conc,maxLocalDose)
fraction_LA_Remaining = 1-fraction_LA_Used
RopiDoseHvlia = fraction_LA_Remaining*maxRopiDose


# RopiVolHvlia = RopiDoseHvlia/2

def finalVol(LaDose,RopiConc):
  return LaDose/RopiConc

final_vol = finalVol(RopiDoseHvlia,2)

print(final_vol)
