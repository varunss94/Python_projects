# graph.py

from vertex import Vertex

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    self.graph_dict[to_node.value].add_edge(from_node.value, weight)

  def explore(self):
    print("Exploring the graph....\n")
    #FILL IN EXPLORE METHOD BELOW
    current_room = 'entrance'
    path_total = 0 
    print("\nStarting off at the {0}\n".format(current_room))
    
    while current_room != "treasure room":
      node = self.graph_dict[current_room]
      for connected_room, weight in node.edges.items():
        key = connected_room[0]
        print ("enter {0} for {1}: {2} cost".format(key, connected_room, weight))
        valid_choices = [room[0] for room in node.edges.keys()]
        print("\n You have accumilated: {0} cost ".format(path_total)
              choice = input("\n which room do you move to?")
              
        			if choice not in valid_choices:
              
        				print("please select form these letters: {0}")
              else:
              	for room in node.edges.keys():
              		if choice == room[0]:
              
              			current_room = room
              			path_total += node.edges[room]
      					print("\n ***you have chosen: {0} ***\n ".format(current_room))
              
              
              		
              		
              
              
            
              
      
    
      
      
  def print_map(self):
    print("\nMAZE LAYOUT\n")
    for node_key in self.graph_dict:
      print("{0} connected to...".format(node_key))
      node = self.graph_dict[node_key]
      for adjacent_node, weight in node.edges.items():
        print("=> {0}: cost is {1}".format(adjacent_node, weight))
      print("")
    print("")

def build_graph():
  graph = Graph()
  
  # MAKE ROOMS INTO VERTICES BELOW...tex()
  entrance = Vertex("entrance")
  


  # ADD ROOMS TO GRAPH BELOW...
  graph.add_vertex(entrance)

  # ADD EDGES BETWEEN ROOMS BELOW...
  ante_chamber = Vertex("ante-chamber")
  graph.add_vertex(ante_chamber)
  kings_room = Vertex("king's room")
  graph.add_vertex(kings_room)
  
  graph.add_edge(entrance, ante_chamber, 7)
  graph.add_edge(ante_chamber, kings_room, 3)
  
  graph.add_edge(kings_room, ante_chamber ,1)
  
  grand_gallery = Vertex("grand_gallery")
  graph.add_vertex(grand_gallery)
  graph.add_edge(grand_gallery, ante_chamber, 2)
  graph.add_edge(grand_gallery, kings_room, 2)
  treasure_room = Vertex("treasure room")
  graph.add_vertex(treasure_room)
  graph.add_edge(treasure_room, ante_chamber, 6)
  graph.add_edge(treasure_room, grand_gallery, 4)


    
    
  # DON'T CHANGE THIS CODE
  graph.print_map()
  return graph
