import pandas as pd                        
import json

# cate = pd.read_json (r'cat.json')

# cate_id = cate['id']

# cate_children = cate["children"]

# cate_children_df = pd.DataFrame(cate_children)


# cat_lv1 = []

# for row in cate_children.index :

#     row = cate_children.iloc[row]
#     row_id = row['id']
#     cat_lv1.append(row_id)
# # firstrow_children = firstrow["children"]

# # # firstrow_df = pd.DataFrame.from_dict(firstrow)
# # firstrow_children_df = pd.DataFrame(firstrow_children)

# # print(type(firstrow_children))

# print(type(cat_lv1))

# print(cat_lv1)

all_cat = pd.read_excel('cat1.xlsx')
all_cat_id = all_cat['category'].values.tolist()
print(type(all_cat_id))
print(all_cat_id)