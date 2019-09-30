
#--------------------------------------------------------------

# Global timestep output options
timeStepToStartOutputAt=0
forceOutputAtFirstCall=False

# Global screenshot output options
imageFileNamePadding=0
rescale_lookuptable=False

# Whether or not to request specific arrays from the adaptor.
requestSpecificArrays=False

# a root directory under which all Catalyst output goes
rootDirectory=''

# makes a cinema D index table
make_cinema_table=False

#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.
# paraview version 5.6.0
#--------------------------------------------------------------

from paraview.simple import *
from paraview import coprocessing

# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 5.6.0

      # ----------------------------------------------------------------
      # setup views used in the visualization
      # ----------------------------------------------------------------

      # trace generated using paraview version 5.6.0
      #
      # To ensure correct image size when batch processing, please search 
      # for and uncomment the line `# renderView*.ViewSize = [*,*]`

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # get the material library
      materialLibrary1 = GetMaterialLibrary()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [2384, 1434]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.CenterOfRotation = [15.0, 14.5, 14.5]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [72.95737816914938, 57.59046756467926, 80.98540521015448]
      renderView1.CameraFocalPoint = [15.00000000000003, 14.499999999999996, 14.499999999999991]
      renderView1.CameraViewUp = [0.2735519444211961, 0.6806591859136356, -0.6796119527603748]
      renderView1.CameraParallelScale = 25.406692031825003
      renderView1.Background = [0.32, 0.34, 0.43]
      renderView1.OSPRayMaterialLibrary = materialLibrary1

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView1.AxesGrid.XTitleFontFile = ''
      renderView1.AxesGrid.YTitleFontFile = ''
      renderView1.AxesGrid.ZTitleFontFile = ''
      renderView1.AxesGrid.XLabelFontFile = ''
      renderView1.AxesGrid.YLabelFontFile = ''
      renderView1.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='RenderView1_%t.png', freq=1, fittoscreen=0, magnification=1, width=2384, height=1568, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # ----------------------------------------------------------------
      # restore active view
      SetActiveView(renderView1)
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # create a new 'XML MultiBlock Data Reader'
      # create a producer from a simulation input
      input = coprocessor.CreateProducer(datadescription, 'input')

      # create a new 'Contour'
      contour1 = Contour(Input=input)
      contour1.ContourBy = ['POINTS', 'mandelbulb']
      contour1.Isosurfaces = [50.0]
      contour1.PointMergeMethod = 'Uniform Binning'

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from contour1
      contour1Display = Show(contour1, renderView1)

      # get color transfer function/color map for 'vtkBlockColors'
      vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
      vtkBlockColorsLUT.InterpretValuesAsCategories = 1
      vtkBlockColorsLUT.AnnotationsInitialized = 1
      vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
      vtkBlockColorsLUT.ActiveAnnotatedValues = ['0']
      vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]
      vtkBlockColorsLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

      # trace defaults for the display properties.
      contour1Display.Representation = 'Surface'
      contour1Display.ColorArrayName = ['FIELD', 'vtkBlockColors']
      contour1Display.LookupTable = vtkBlockColorsLUT
      contour1Display.OSPRayScaleArray = 'Normals'
      contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
      contour1Display.SelectOrientationVectors = 'None'
      contour1Display.ScaleFactor = 2.750505065917969
      contour1Display.SelectScaleArray = 'None'
      contour1Display.GlyphType = 'Arrow'
      contour1Display.GlyphTableIndexArray = 'None'
      contour1Display.GaussianRadius = 0.13752525329589843
      contour1Display.SetScaleArray = ['POINTS', 'Normals']
      contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
      contour1Display.OpacityArray = ['POINTS', 'Normals']
      contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
      contour1Display.DataAxesGrid = 'GridAxesRepresentation'
      contour1Display.SelectionCellLabelFontFile = ''
      contour1Display.SelectionPointLabelFontFile = ''
      contour1Display.PolarAxes = 'PolarAxesRepresentation'

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      contour1Display.DataAxesGrid.XTitleFontFile = ''
      contour1Display.DataAxesGrid.YTitleFontFile = ''
      contour1Display.DataAxesGrid.ZTitleFontFile = ''
      contour1Display.DataAxesGrid.XLabelFontFile = ''
      contour1Display.DataAxesGrid.YLabelFontFile = ''
      contour1Display.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      contour1Display.PolarAxes.PolarAxisTitleFontFile = ''
      contour1Display.PolarAxes.PolarAxisLabelFontFile = ''
      contour1Display.PolarAxes.LastRadialAxisTextFontFile = ''
      contour1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for vtkBlockColorsLUT in view renderView1
      vtkBlockColorsLUTColorBar = GetScalarBar(vtkBlockColorsLUT, renderView1)
      vtkBlockColorsLUTColorBar.Title = 'vtkBlockColors'
      vtkBlockColorsLUTColorBar.ComponentTitle = ''
      vtkBlockColorsLUTColorBar.TitleFontFile = ''
      vtkBlockColorsLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      vtkBlockColorsLUTColorBar.Visibility = 1

      # show color legend
      contour1Display.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # get opacity transfer function/opacity map for 'vtkBlockColors'
      vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(contour1)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'input': [1, 1]}
  coprocessor.SetUpdateFrequencies(freqs)
  if requestSpecificArrays:
    arrays = [['mandelbulb', 0]]
    coprocessor.SetRequestedArrays('input', arrays)
  coprocessor.SetInitialOutputOptions(timeStepToStartOutputAt,forceOutputAtFirstCall)

  if rootDirectory:
      coprocessor.SetRootDirectory(rootDirectory)

  if make_cinema_table:
      coprocessor.EnableCinemaDTable()

  return coprocessor


#--------------------------------------------------------------
# Global variable that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView and the update frequency
coprocessor.EnableLiveVisualization(False, 1)

# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor

    # setup requests for all inputs based on the requirements of the
    # pipeline.
    coprocessor.LoadRequestedData(datadescription)

# ------------------------ Processing method ------------------------

def DoCoProcessing(datadescription):
    "Callback to do co-processing for current timestep"
    global coprocessor

    # Update the coprocessor by providing it the newly generated simulation data.
    # If the pipeline hasn't been setup yet, this will setup the pipeline.
    coprocessor.UpdateProducers(datadescription)

    # Write output data, if appropriate.
    coprocessor.WriteData(datadescription);

    # Write image capture (Last arg: rescale lookup table), if appropriate.
    coprocessor.WriteImages(datadescription, rescale_lookuptable=rescale_lookuptable,
        image_quality=0, padding_amount=imageFileNamePadding)

    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
