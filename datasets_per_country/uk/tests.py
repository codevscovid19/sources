
import os
import os . path
import subprocess

import ukdl

assert (os . path . exists ("covid-19-indicators-uk.csv"))
os . remove ("covid-19-indicators-uk.csv")
  

assert (os . path . exists ("covid-19-cases-uk.csv"))
os . remove ("covid-19-cases-uk.csv")

try :
  ukdl . download_the_data ("nothin")
except (subprocess . CalledProcessError) :
  print ("all good")
else :
  assert (False)

