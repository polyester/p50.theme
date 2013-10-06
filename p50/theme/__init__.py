from Products.CMFCore.DirectoryView import registerDirectory

registerDirectory('skins', globals())

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
