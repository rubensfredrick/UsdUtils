from pxr import Usd
from . import common

def createVariantSetOInStage(layer)
    stage = Usd.Stage.Open(layer, Usd.Stage.LoadNone)

    # Determine state to be written into the fragment.
    editPrimPath = self.editPrimPath(stage, layer)
    editPrimSpec = common.sdfCreatePrimAtPath(layer, editPrimPath)
    editPrimSpec.kind = self.EditPrimKind
    editPrimSpec.typeName = "ALEdit"

    # Create stage to create ALEdit prim.
    editPrim = stage.GetPrimAtPath(editPrimPath)

    # Ensure a variant set named "animatic" exists.
    variantSets = editPrim.GetVariantSets()
    variantSet = variantSets.AddVariantSet(self.VariantSetName)

    variantSet.AddVariant(self.AnimaticVariantName)
    variantSet.SetVariantSelection(self.AnimaticVariantName)
    with variantSet.GetVariantEditContext():
        attribute = editPrim.CreateAttribute(
            self.IdentifierAttributeName, self.IdentifierAttributeValue, False,
        )
        attribute.Set(self.animaticTechVariantUri(layer))

    variantSet.AddVariant(self.StoryboardVariantName)
    variantSet.SetVariantSelection(self.StoryboardVariantName)
    with variantSet.GetVariantEditContext():
        attribute = editPrim.CreateAttribute(
            self.IdentifierAttributeName, self.IdentifierAttributeValue, False,
        )
        attribute.Set(self.storyboardTechVariantUri(layer))

    variantSet.SetVariantSelection("")
