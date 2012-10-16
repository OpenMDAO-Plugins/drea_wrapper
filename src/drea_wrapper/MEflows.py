from openmdao.main.api import VariableTree
from openmdao.lib.datatypes.api import Float, Slot
from stream import Stream

class MEflows(VariableTree):
    """Container of variables defining the flow properties of the mixer-ejector nozzle"""

    # Primary and Secondary Streams
    pri = Slot(Stream, iotype='in')
    sec = Slot(Stream, iotype='in')   
    
    gamma = Float(1.4, desc='Ratio of specific heats')
    Pstatic = Float(2116.8, units='lbf/ft**2', desc='Freestream static pressure')
    #alt = Float(0.0, units='ft', desc='Altitude')
    #Mach = Float(0.0, desc='Freestream Mach number')

    def __init__(self):
        super(MEflows, self).__init__()
        self.add('pri', Stream())
        self.add('sec', Stream())
    