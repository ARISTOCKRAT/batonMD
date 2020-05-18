# import json
#
# with open("out_data/fuzzy_logic.json") as f:
#     data = json.load(f)
#
# print(data.keys())
# for item in data['68'].items():
#     print(item)
#
# for i in range(69):
#     print(data[str(i)]['feature_name'], end='\t')
#     print(data[str(i)]['intervals_count'], end='\t')
#
#     for interval in data[str(i)]['intervals']:
#         print(f"[{interval[0]:.2f}..{interval[1]:.2f}]({interval[3]:.2f})K{interval[2]}, ", end="")
#     print(f"\t{data[str(i)]['stability']:.2f}")

a = {1,2,3,4,5,}

b = ', '.join(str(e) for e in a)
print(b)


