from collections import namedtuple
from pxr import Sdf

def sdfCreatePrimAtPath(parent, primPath, specifier=Sdf.SpecifierDef, typeName=""):
    if isinstance(parent, Sdf.Layer):
        parent = parent.pseudoRoot  # use the actual layer roots primSpec
    path = ""
    for name in str(primPath).split("/"):
        if not name:
            continue
        path += "/{}".format(name)
        # try getting by path first, then by `name` only (which will work on variant primspecs)
        primSpec = parent.GetPrimAtPath(path) or parent.nameChildren.get(name)
        if not primSpec:
            primSpec = Sdf.PrimSpec(parent, name, specifier, typeName)

        parent = primSpec
    return parent

def addVariantSetToInstanceName(layer, instanceName, setVar=True)
    VariantValues = namedtuple("VariantValues", ["on", "off"])
    VariantSet = "myVariantSet"
    myVariantSet = VariantValues("on", "off")

    rootPrimSpec = layer.GetPrimAtPath(layer.defaultPrim)
    instancePrim = rootPrimSpec.GetPrimAtPath(instanceName)
    if not instancePrim or VariantSet not in instancePrim.variantSets.keys():
        return False

    _path = Sdf.Path(layer.defaultPrim).AppendChild(instanceName)
    instancePrimSpec = sdfCreatePrimAtPath(
        layer,
        primPath=_path,
        specifier=Sdf.SpecifierOver
    )

    # If variant set already exists, fetch it, else create it
    if VariantSet in instancePrimSpec.variantSets.keys():
        variantSetSpec = instancePrimSpec.variantSets.get(VariantSet)
    else:
        variantSetSpec = Sdf.VariantSetSpec(instancePrimSpec, VariantSet)
        instancePrimSpec.variantSetNameList.prependedItems.append(VariantSet)

    # dept specific variant
    _variants = variantSetSpec.variants.keys()
    if myVariantSet.on not in _variants:
        Sdf.VariantSpec(variantSetSpec, myVariantSet.on)
    if myVariantSet.off not in _variants:
        Sdf.VariantSpec(variantSetSpec, myVariantSet.off)

    # Set variant value to the 'hasAnimFX' flag value
    instancePrimSpec.variantSelections[VariantSet] = myVariantSet.on if setVar else myVariantSet.off
