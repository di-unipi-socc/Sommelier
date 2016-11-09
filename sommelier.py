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

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    check(args)
    path = args[0].split('--template-file=')[1]

    if os.path.isfile(path):
    	v = topologyvalidator.TopologyValidator()
        validation = v.validate(path)
        v.printValidation(validation)
    else:
        raise ValueError(_('"%(path)s" is not a valid file.')
                            % {'path': path})

if __name__ == '__main__':
    main()                

