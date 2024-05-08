from collections import defaultdict
from collections import OrderedDict
from utils import charging_time_factor, charge_full_time, max_km
import math
def merged_list(src, dest):
    def precompute_and_queueing(s,distance,max_km,charge_full_time,time_taken):
        initial=s
        clean_time = s.replace(":",".")
        itime = float(clean_time);
        itime = math.trunc(itime) + (itime%1)*5/3
        itime += float(time_taken)/60

        charge_consumed = distance*100/max_km
        time_to_charge=(charge_consumed) * charging_time_factor/3.25

                                                    
                                                    
        merged_list.append([itime, time_to_charge])

        # addToQueue(itime, time_to_charge)

    src_num = src['Bus Number'].count()
    dest_num = dest['Bus Number'].count()
    ready_dict = {}
    ready_dict = defaultdict(lambda: 0, ready_dict)
    src_dict = {}
    src_dict = defaultdict(lambda: 0, src_dict)

    # temp_dict = {}
    # temp_dict = defaultdict(lambda: 0, temp_dict)

    for i in range(0,src_num):
        temp2 = [x.strip() for x in src['Departure From Destination'][i].split(',')]
        dist = [x.strip() for x in src['Distance'][i].split(' ')]
        temp2.pop()
        dist.pop()
        distance = dist[0]

        time_taken = src['Journey Time'][i]
        if time_taken == "Not available":
            time_taken = int(round(float(distance)/18 * 60,0))

        for j in temp2:
            precompute_and_queueing(j[:5],float(distance),max_km,charge_full_time,int(time_taken))

    for i in range(0,dest_num):
        temp2 = [x.strip() for x in dest['Departure From Source'][i].split(',')]
        dist = [x.strip() for x in dest['Distance'][i].split(' ')]
        temp2.pop()
        dist.pop()
        distance = dist[0]
        time_taken = dest['Journey Time'][i]
        if time_taken == "Not available":
            time_taken = int(round(float(distance)/18 * 60,0))
        for j in temp2:
            precompute_and_queueing(j[:5],float(distance),max_km,charge_full_time,int(time_taken))
    # print(merged_list)
    merged_list = sorted(merged_list, key=lambda x: x[0])  ##############################################

    ss = merged_list.copy()

    ss = sorted(ss, key=lambda x: x[0])
    art = []
    for x in ss:
        if x[0] not in art:
            art.append(x[0])
    final_merged_list = []
    for j in art:
        same_time_bus = []
        for x in ss:
            if x[0] == j:
                same_time_bus.append([x[0],x[1]])
        same_time_bus = sorted(same_time_bus, key =lambda y:y[1])
        for y in same_time_bus:
            final_merged_list.append(y)

    merged_list = final_merged_list.copy()
    ss = merged_list.copy()

    return merged_list