import cellprofiler as cp
import cellprofiler.modules as cpm

# create a pipeline object
pipeline = cp.Pipeline()

# add the LoadImages module to load the images
load_module = cpm.LoadImages()
load_module.module_num = 1
load_module.images = cp.ImageSet(
    'Experiment', 
    cp.ImagePlane(
        'Image',
        'path/to/experiment/images/*.tif'
    )
)
pipeline.add_module(load_module)

# add the LoadImages module for the negative control images
load_module_neg = cpm.LoadImages()
load_module_neg.module_num = 2
load_module_neg.images = cp.ImageSet(
    'NegativeControl',
    cp.ImagePlane(
        'Image',
        'path/to/negative/control/images/*.tif'
    )
)
pipeline.add_module(load_module_neg)

# add the LoadImages module for the positive control images
load_module_pos = cpm.LoadImages()
load_module_pos.module_num = 3
load_module_pos.images = cp.ImageSet(
    'PositiveControl',
    cp.ImagePlane(
        'Image',
        'path/to/positive/control/images/*.tif'
    )
)
pipeline.add_module(load_module_pos)

# add preprocessing modules to preprocess the images
preprocess_module = cpm.PreprocessImages()
preprocess_module.module_num = 4
preprocess_module.operation.value = "CorrectIlluminationApply"
pipeline.add_module(preprocess_module)

# run the pipeline
cpmeas, cpimg = pipeline.run()
