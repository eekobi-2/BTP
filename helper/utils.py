import math
def hour_to_str(itime):
  tr =  str(math.trunc(itime)) + ':' + str(int(round((itime%1)*300/5)))
  itime = math.trunc(itime) + (itime%1)*3/5
  s=str(itime)
  clean_time = s.replace(".",":")

  if ( math.trunc(itime)<10) :
    clean_time = '0'+clean_time
    tr = '0' + tr
  clean_time  = clean_time[:5]
  if (len(clean_time)<5):
    clean_time+='0'

  return clean_time
charging_time_factor = 0.0
max_km=200
charge_full_time=6

def Factor_charging_time(charge_full_time):
  sum=0;
  for i in range(0,25):
      sum+=1/((2*(i/25)) +1.25);
  sum+=55/3.25;
  for i in range (80,100):
      sum+=1/(11.25 - (0.1*i));
  return charge_full_time/sum;

charging_time_factor = Factor_charging_time(charge_full_time)
