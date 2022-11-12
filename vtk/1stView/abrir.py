from vtk import vtkDICOMImageReader as dcmReader
from vtk import *

pathimage = "..\..\..\Volumenes\IMG_20211012_18.4dv\IMAGE\Y2018M12\D10\E0000001\I0000034.dcm"
source = dcmReader()
#leer DICOM, tambien se puede leer directorio con SetDirectoryName
source.SetFileName(pathimage)
source.Update()

#imageData = source.GetOutput()

colors = vtkNamedColors()
print(source.GetOutput().GetScalarTypeAsString())

castFilter = vtkImageCast()
castFilter.SetInputConnection(source.GetOutputPort())
castFilter.SetOutputScalarTypeToUnsignedChar()
castFilter.Update()

# Create an actor
actor = vtkImageActor()
actor.GetMapper().SetInputConnection(castFilter.GetOutputPort())

# Setup renderer
renderer = vtkRenderer()
renderer.AddActor(actor)
#renderer.SetBackground(colors.GetColor3d('DarkSlateGra'))
renderer.ResetCamera()

# Setup render window
renderWindow = vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetWindowName('Cast')

# Setup render window interactor
renderWindowInteractor = vtkRenderWindowInteractor()
style = vtkInteractorStyleImage()
renderWindowInteractor.SetInteractorStyle(style)

# Render and start interaction
renderWindowInteractor.SetRenderWindow(renderWindow)
renderWindow.Render()
renderWindowInteractor.Initialize()
renderWindowInteractor.Start()
