from collections import defaultdict
from collections import OrderedDict

def buses(ready_dict_final, src_dict_final):
        final_dict = {}
        final_dict = defaultdict(lambda: 0, final_dict)
        final_dict = ready_dict_final.copy()

        # print(final_dict)

        for key,value in src_dict_final.items():
            if key in final_dict.keys():
                final_dict[key] -= value
            else:
                final_dict[key] = -1*value
        final_dict_new = OrderedDict(sorted(final_dict.items()))

        sum=0
        for key, value in final_dict_new.items():
            sum += value
            final_dict_new[key]=sum
        min_val = 0
        for key, value in final_dict_new.items():
            min_val = min(min_val,value)


        end_val = final_dict_new[list(final_dict_new.keys())[-1]]
        kk = final_dict_new.keys()


        # plt.figure(figsize=(20, 15))
        # plt.plot( kk, final_dict_new.values())
        # print(final_dict_new)




        buses = (-1*min_val)
        return buses