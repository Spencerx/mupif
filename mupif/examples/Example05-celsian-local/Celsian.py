
import sys
sys.path.append('../../..')
from mupif import *

class Celsian(Application.Application):

    def __init__ (self, file):
        super(Celsian, self).__init__(file)
        self.mesh = None

    def getField(self, fieldID, time):
        parts=[1, 2]
        partRec=[]
        if (self.mesh == None):
            self.mesh = EnsightReader2.readEnsightGeo('paraview/MMPTestCase_v1.geo', parts, partRec)

        f = EnsightReader2.readEnsightField('paraview/fld_TEMPERATURE.escl', parts, partRec, 1, FieldID.FID_Temperature, self.mesh)
        return f

    def solveStep(self, tstep, stageID=0, runInBackground=False):
        time = tstep.getTime()
        self.value=1.0*time
    def getCriticalTimeStep(self):
        return 0.1


