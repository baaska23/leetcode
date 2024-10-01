from collections import deque

graph = {
    "you": ["sanchir", "oyu", "bayraa"],
    "sanchir": ["ayna", "murun", "dulguun"],
    "oyu": ["zul", "manduul"],
    "bayraa" : ["baljka"],
    "ayna": [],
    "murun": [],
    "dulguun": [],
    "zul": [],
    "manduul": [],
    "baljka": []

}

def personIsSeller(name):
    return name[-1] == 'u'

def breadthFirstSearch(start):
    search_queue = deque()
    search_queue.append(start)
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if personIsSeller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue.extend(graph.get(person, []))
                searched.append(person)
    return False

result = breadthFirstSearch("oyu")
print(result)