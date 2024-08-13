from graphviz import Digraph

dot = Digraph(comment='Firewall GUI Project')

# Nodes
dot.node('A', 'Firewall GUI Application')
dot.node('B', 'Tkinter (GUI)')
dot.node('C', 'IPTables Commands')
dot.node('D', 'Rule Management')
dot.node('E', 'Whitelist Management')
dot.node('F', 'Blacklist Management')
dot.node('G', 'Logging')
dot.node('H', 'Show Rules')
dot.node('I', 'Flush Rules')
dot.node('J', 'Help')

# Edges
dot.edges(['AB', 'AC'])
dot.edge('A', 'D', label='Add/Delete Rules')
dot.edge('A', 'E', label='Add/Delete Whitelist')
dot.edge('A', 'F', label='Add/Delete Blacklist')
dot.edge('A', 'G', label='Log Actions')
dot.edge('A', 'H', label='Display Current Rules')
dot.edge('A', 'I', label='Flush All Rules')
dot.edge('A', 'J', label='Show Help')

# Subgraph for Rule Management
with dot.subgraph(name='cluster_0') as c:
    c.attr(style='filled', color='lightgrey')
    c.node_attr.update(style='filled', color='white')
    c.edges(['CD', 'CE', 'CF'])
    c.label = 'Rule Management'

# Save the diagram
dot.render('firewall_gui_project', view=True, format='png')

print(dot.source)
