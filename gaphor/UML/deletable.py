from gaphor.diagram.deletable import deletable
from gaphor.UML.uml import ConnectorEnd, ExtensionEnd, Property


@deletable.register
def connector_end_deletable(element: ConnectorEnd) -> bool:
    return False


@deletable.register
def property_deletable(element: Property) -> bool:
    return not element.association and not element.end


@deletable.register
def extension_end_deletable(element: ExtensionEnd) -> bool:
    return False
