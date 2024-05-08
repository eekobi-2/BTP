from collections import defaultdict
from collections import OrderedDict

def src_dict(data, depot):
  src = data[(data['Source Depot'] == depot)]
  dest = data[(data['Destination Depot'] == depot)]

  src.index = [i for i in range(len(src))]
  dest.index = [i for i in range(len(dest))]

  src_num = src['Bus Number'].count()
  dest_num = dest['Bus Number'].count()

  src_dict = {}
  src_dict = defaultdict(lambda: 0, src_dict)

  for i in range(0,src_num):
    temp2 = [x.strip() for x in src['Departure From Source'][i].split(',')]
    temp2.pop()
    for i in temp2:
      src_dict["{}".format(i)] += 1

  for i in range(0,dest_num):
    temp2 = [x.strip() for x in dest['Departure From Destination'][i].split(',')]
    temp2.pop()
    for i in temp2:
      src_dict["{}".format(i)] += 1

  src_dict_final = OrderedDict(sorted(src_dict.items()))

  return src_dict_final, src, dest