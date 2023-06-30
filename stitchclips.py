from pxr import UsdUtils, Sdf

results_out = "Output file path for top level result file, also used for manifest and topology"
results_clipPath = "clip file path where to stich the data"
results_usdFiles = "clip files"


outLayer = Sdf.Layer.FindOrOpen(results_out)
if not outLayer:
    outLayer = Sdf.Layer.CreateNew(results_out)
        
topologyLayerName = UsdUtils.GenerateClipTopologyName(results_out)
topologyLayer = Sdf.Layer.FindOrOpen(topologyLayerName)
if not topologyLayer:
    topologyLayer = Sdf.Layer.CreateNew(topologyLayerName)

manifestLayerName = UsdUtils.GenerateClipManifestName(results.out)
manifestLayer = Sdf.Layer.FindOrOpen(manifestLayerName)
if not manifestLayer:
    manifestLayer = Sdf.Layer.CreateNew(manifestLayerName)


UsdUtils.StitchClipsTopology(topologyLayer, results_usdFiles)
UsdUtils.StitchClipsManifest(manifestLayer, topologyLayer, 
                             results.usdFiles, results.clipPath)
UsdUtils.StitchClipsTemplate(outLayer, 
                             topologyLayer,
                             manifestLayer,
                             results_clipPath,
                             results.templatePath,
                             results.startTimeCode,
                             results.endTimeCode,
                             results.stride,
                             results.activeOffset,
                             results.interpolateMissingClipValues,
                             results.clipSet)
