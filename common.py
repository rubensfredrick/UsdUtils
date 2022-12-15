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
