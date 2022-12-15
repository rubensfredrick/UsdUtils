from pxr import Usd

stage = Usd.Stage.Open(self.file)

# Sets the variant selection to value, else stage wil be un loadable and following code will not work
myVariantSet = "myvariant"
for prim in stage.GetPrimAtPath("/root").GetAllChildren():
    _variantSets = prim.GetVariantSets()
    if _variantSets.HasVariantSet(myVariantSet):
        _variantSet = _variantSets.GetVariantSet(myVariantSet)
        _variantSet.SetVariantSelection("on")
