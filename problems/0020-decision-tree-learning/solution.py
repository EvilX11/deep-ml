import math
from collections import Counter

def calculate_entropy(labels: list) -> float:
    """Calculate the entropy of a list of labels."""
    freq={}
    for i in labels:
        freq[i]=freq.get(i,0)+1
    total=0.0
    for i in freq:
        total+=freq[i]
    val=0.0
    for i in freq:
        probab=freq[i]/total
        val+=-math.log2(probab)*probab

    return val

def calculate_information_gain(examples: list[dict], attr: str, target_attr: str) -> float:
    """Calculate the information gain of splitting on attr."""
    s=set()
    freq={}
    for e in examples:
        s.add(e.get(attr))
        freq[e[attr]]=freq.get(e[attr],0)+1
    
    total=0
    ig=0.0
    h_s_a=0.0
    for key,value in freq.items():
        total+=value
    for ele in s:
        l=[]
        for e in examples:
            if e[attr]==ele:
                l.append(e.get(target_attr))
        entropy_s_a=calculate_entropy(l)
        h_s_a+=(freq[ele]/total)*entropy_s_a
    list_target=[]
    for e in examples:
        list_target.append(e.get(target_attr))
    h_s=calculate_entropy(list_target)
    ig=h_s-h_s_a
    return ig


def majority_class(examples: list[dict], target_attr: str) -> str:
    labels=[]
    for e in examples:
        labels.append(e.get(target_attr))

    count=Counter(labels)
    return count.most_common(1)[0][0] 


def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict:
    labels=[e[target_attr] for e in examples]

    if not examples:
        return None
    if len(set(labels))==1:
        return labels[0]
    
    if not attributes:
        return majority_class(examples,target_attr)

    best_attr=None
    max_gain=-float('inf')

    for attr in attributes:
        gain=calculate_information_gain(examples,attr,target_attr)
        if gain>max_gain:
            max_gain=gain
            best_attr=attr
    
    tree={best_attr:{}}
    values=sorted(set(e[best_attr]for e in examples))

    for value in values:
        subset=[
            e for e in examples
            if e[best_attr]==value
        ]

        remaining_attributes=[
            a for a in attributes
            if a!=best_attr
        ]

        subtree=learn_decision_tree(
            subset,
            remaining_attributes,target_attr
        )

        tree[best_attr][value]=subtree

    return tree

