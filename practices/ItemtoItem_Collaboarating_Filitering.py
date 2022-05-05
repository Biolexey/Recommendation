import numpy as np
from scipy.spatial.distance import squareform, pdist, cosine #コサイン類似度計算用

x = np.array([      #購入データ
  [1,1,1,0,0,0],
  [1,1,0,1,0,0],
  [1,0,1,0,1,0],
  [0,0,1,1,1,0],
  [0,1,0,0,0,0],
  [1,0,0,0,1,0],
  [1,0,1,0,1,1],
  [0,0,0,0,1,1]
])

x = x.T             #アイテム毎にするために転置
d = pdist(x, "cosine")  
d = 1 - d

d = squareform(d)

d = d - np.eye(d.shape[0])  #自分自身の垂線度を低くするために単位行列を引く

print(d)
for i in range(x.shape[0]):
  print(f"item{i+1}")
  item1_sim = d[:, i]
  print(f"item1_sim = {item1_sim}")
  item1_rel = []
  for j in range(item1_sim.shape[0]):
    item1_rel.append((f"item{j+1}", item1_sim[j]))
  item1_rel = sorted(item1_rel, key=lambda d:d[1], reverse=True)
  #3件に絞る
  item1_rel = item1_rel[:3]
  print(item1_rel)  
