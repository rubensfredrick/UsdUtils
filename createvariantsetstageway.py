from pxr import Usd
from . import common

def createVariantSetOInStage(layer, subPrimName, myVariantSetName, myVariantName, attribNameValue={})
    stage = Usd.Stage.Open(layer, Usd.Stage.LoadNone)

    # Determine state to be written into the fragment.
    editPrimPath = stage.GetDefaultPrim().GetPath().AppendChild(subPrimName)
    editPrimSpec = common.sdfCreatePrimAtPath(layer, editPrimPath)
    editPrimSpec.kind = "edit"
    editPrimSpec.typeName = "Edit"

    # Create stage to create ALEdit prim.
    editPrim = stage.GetPrimAtPath(editPrimPath)

    # Ensure a variant set named "animatic" exists.
    variantSets = editPrim.GetVariantSets()
    variantSet = variantSets.AddVariantSet(myVariantSetName)

    variantSet.AddVariant(myVariantName)
    variantSet.SetVariantSelection(myVariantName)
    
    # Add attribute if required
    with variantSet.GetVariantEditContext():
        for key, val in attribNameValue.items():
            attribute = editPrim.CreateAttribute(key, val[0], False,)  # val can be attrib type like Sdf.ValueTypeNames.Asset
            attribute.Set(val[1])  # uri

    # to remove varaint selection
    variantSet.SetVariantSelection("")
