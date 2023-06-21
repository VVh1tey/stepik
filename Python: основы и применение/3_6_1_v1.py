from xml.etree import ElementTree

root = ElementTree.fromstring(input())
colors = {"red": 0, "green": 0, "blue": 0}

def CalcWeights(root, value):
    colors[root.attrib['color']] += value
    for child in root:
        CalcWeights(child, value+1)

CalcWeights(root,1)
print(colors["red"], colors["green"], colors["blue"])