import os
import sys
import topologyvalidator

from toscaparser.utils.gettextutils import _
import toscaparser.utils.urlutils

def check(args):
    if len(args) < 1:
        msg = _('The program requires a template or a CSAR file as an '
                'argument. Please refer to the usage documentation.')
        raise ValueError(msg)
    if "--template-file=" not in args[0]:
        msg = _('The program expects "--template-file" as the first '
                'argument. Please refer to the usage documentation.')
        raise ValueError(msg)

# Print the errors
def printError(errorList):

    codeError = errorList[0]
    if codeError == 1.1:
        print '1.1 - MISSING_REQUIREMENT_DEFINITION: The requirement is assigned but not defined.'
    elif codeError == 1.2:
        print '1.2 - NODE_TYPE_NOT_COHERENT: The type "%s" of the target node "%s" is not valid (as it differs from that indicated in the requirement definition).' % (errorList[1], errorList[2])
    elif codeError == 1.3:
        print '1.3 - CAPABILITY_TYPE_NOT_COHERENT: The type of the target capability is not valid (as it differs from that indicated in the requirement definition).'
    elif codeError == 1.4:
        print '1.4 - MISSING_CAPABILITY_ERROR: The target node template "%s" is not offering any capability whose type is compatible with "%s" (indicated in the requirement definition).' % (errorList[1], errorList[2])
    elif codeError == 1.5:
        print '1.5 - RELATIONSHIP_TYPE_NOT_COHERENT: The type of the outgoing relationship is not valid (as it differs from that indicated in the requirement definition).'
    elif codeError == 2.1:
        print '2.1 - CAPABILITY_VALID_TARGET_TYPE_ NOT_COHERENT: The type of the target capability "%s" is not valid (as it differs from that indicated in the definition of the type of the outgoing relationship).' %(errorList[1])
    elif codeError == 2.2:
        print '2.2 - MISSING_CAPABILITY_VALID_TARGET_TYPE: The target node template "%s" is not offering any capability whose type is compatible with those indicated as valid targets for the type of the outgoing relationship.' % (errorList[1])
    elif codeError == 3.1:
        print '3.1 - CAPABILITY_VALID_SOURCE_TYPE_ NOT_COHERENT: The node type "%s" is not a valid source type for the capability targeted by the outgoing relationship (as it differs from those indicated in the capability type).' % (errorList[1])               
    elif codeError == 3.2:
        print '3.2 - CAPABILITY_DEFINITION_VALID_SOURCE_TYPE_NOT_COHERENT: The node type "%s" is not a valid source type for the capability targeted by the outgoing relationship (as it differs from those indicated in the capability definitions in the type of "%s").' % (errorList[1], errorList[2])                

# Prints the result of the validation
def printValidation(validation):
    isCorrect = True
    for nodeName in validation:
        reqs = validation.get(nodeName).keys()
        for req in reqs:
            infoList = validation.get(nodeName).get(req)
            if infoList != []:
                print "\nNODE TEMPLATE: ",nodeName
                print "REQUIREMENT: ",req
            for info in infoList:
                isCorrect = False
                printError(info)
    if isCorrect:
        print "The application topology is valid."

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    check(args)
    path = args[0].split('--template-file=')[1]

    if os.path.isfile(path):
    	v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        printValidation(validation)
    else:
        raise ValueError(_('"%(path)s" is not a valid file.')
                            % {'path': path})

if __name__ == '__main__':
    main()                

