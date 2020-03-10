from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph.output import GraphvizOutput
from Augmentation import Augmentation

graphviz = GraphvizOutput(output_file='map.png')
with PyCallGraph(output=graphviz):
    Augmentation.Augmentation()