import pickle
import random

def generateIds(leng):
  nodeIds = set()
  while len(nodeIds) < leng:
      nodeId = ''.join(random.choices(('a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), k=8))
      nodeIds.add(nodeId)
  return list(nodeIds)

with open('blr.bin', 'rb') as f:
    Gp = pickle.load(f)

c = len(Gp.nodes)
for u, v in Gp.edges.items():
    if 'geometry' in v.keys():
        c += len(v['geometry'].wkt[12:-1].split(','))

nodeIds = generateIds(c)

with open('data.bin','wb') as f:
    pickle.dump(nodeIds, f)