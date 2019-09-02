# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-5 replay file
# Internal Version: 2015_08_18-07.37.49 135153
# Run by Emily on Fri Apr 13 04:38:36 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=166.75, 
    height=140.829620361328)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('tensile_simulation.cae')
#: The model database "D:\abaqus_\Temp\tensile_simulation.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(name='D:/abaqus_/Temp/tensile_test_dispcontrol_1.odb')
#: Model: D:/abaqus_/Temp/tensile_test_dispcontrol_1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       7
#: Number of Node Sets:          10
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
session.viewports['Viewport: 1'].view.setValues(nearPlane=461.346, 
    farPlane=733.413, width=117.831, height=98.567, viewOffsetX=-5.47169, 
    viewOffsetY=7.19052)
odb = session.odbs['D:/abaqus_/Temp/tensile_test_dispcontrol_1.odb']
session.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('E', INTEGRATION_POINT, ((INVARIANT, 'Max. In-Plane Principal'), 
    )), ('S', INTEGRATION_POINT, ((INVARIANT, 'Max. In-Plane Principal'), )), 
    ), elementPick=(('PART-1-1', 168, (
    '[#0:3 #fffc0000 #ffffffff:4 #3ffffff ]', )), ), )
#: Warning: Requested operation will result in the creation of a very large number of xyDataObjects. Performance can be affected. Please reduce the number of specified entities using Display Group operations before re-performing this operation.

#: The model database has been saved to "D:\abaqus_\Temp\tensile_simulation.cae".
for i in range(115,282):
    xy1 = session.xyDataObjects['E:Max In-Plane Principal PI: PART-1-1 E: ' + str(i)+ ' IP: 1']
    xy2 = session.xyDataObjects['E:Max In-Plane Principal PI: PART-1-1 E: ' + str(i)+ ' IP: 2']
    xy3 = session.xyDataObjects['E:Max In-Plane Principal PI: PART-1-1 E: ' + str(i)+ ' IP: 3']
    xy4 = session.xyDataObjects['E:Max In-Plane Principal PI: PART-1-1 E: ' + str(i)+ ' IP: 4']
    xy5 = avg((xy1, xy2, xy3, xy4))
    xy5.setValues(
        sourceDescription='avg ( ( "E:Max In-Plane Principal PI: PART-1-1 E: '+str(i)+ ' IP: 1","E:Max In-Plane Principal PI: PART-1-1 E: '+str(i)+' IP: 2", "E:Max In-Plane Principal PI: PART-1-1 E: '+str(i)+ ' IP: 3","E:Max In-Plane Principal PI: PART-1-1 E: '+str(i)+' IP: 4",) )')
    tmpName = xy5.name
    session.xyDataObjects.changeKey(tmpName, 'E element '+ str(i))
    xy1 = session.xyDataObjects['S:Max In-Plane Principal PI: PART-1-1 E: ' + str(i) + ' IP: 1']
    xy2 = session.xyDataObjects['S:Max In-Plane Principal PI: PART-1-1 E: ' + str(i) + ' IP: 2']
    xy3 = session.xyDataObjects['S:Max In-Plane Principal PI: PART-1-1 E: ' + str(i) + ' IP: 3']
    xy4 = session.xyDataObjects['S:Max In-Plane Principal PI: PART-1-1 E: ' + str(i) + ' IP: 4']
    xy5 = avg((xy1, xy2, xy3, xy4))
    xy5.setValues(
        sourceDescription='avg ( ( "S:Max In-Plane Principal PI: PART-1-1 E: ' + str(
            i) + ' IP: 1","S:Max In-Plane Principal PI: PART-1-1 E: ' + str(
            i) + ' IP: 2", "S:Max In-Plane Principal PI: PART-1-1 E: ' + str(
            i) + ' IP: 3","S:Max In-Plane Principal PI: PART-1-1 E: ' + str(i) + ' IP: 4",) )')
    tmpName = xy5.name
    session.xyDataObjects.changeKey(tmpName, 'S element ' + str(i))
xy1 = session.xyDataObjects['E element 115']
for i in range(116,282):
    xy2 = session.xyDataObjects['E element '+str(i)]
    xy3 = maxEnvelope((xy1, xy2))
xy3.setValues(
    sourceDescription='maxEnvelope ( ( "E element 115", "E element 116" ) )')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'E')
xy1 = session.xyDataObjects['S element 115']
for i in range(116,282):
    xy2 = session.xyDataObjects['S element '+str(i)]
    xy3 = maxEnvelope((xy1, xy2))
xy3.setValues(
    sourceDescription='maxEnvelope ( ( "S element 115", "S element 116" ) )')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'S')

xy1 = session.xyDataObjects['E']
xy2 = session.xyDataObjects['S']
xy3 = combine(xy1, xy2)
xy3.setValues(sourceDescription='combine ( "E", "S" )')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'e-s')
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['e-s']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
mdb.save()
#: The model database has been saved to "D:\abaqus_\Temp\tensile_simulation.cae".
