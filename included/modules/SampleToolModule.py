#!/usr/bin/python

from included.ModuleTemplate import ToolTemplate

class Module(ToolTemplate):
    
    name = "SampleToolModule"

    def set_options(self):
        super(Module, self).set_options()

        self.options.add_argument('-p', '--print_message', help="Message to print")

    
    def get_targets(self, args):
        '''
        This module is used to build out a target list and output file list, depending on the arguments. Should return a
        list in the format [(target, output), (target, output), etc, etc]
        '''

        return []

    def build_cmd(self, args):
        '''
        Create the actual command that will be executed. Use {target} and {output} as placeholders.
        '''
        
        return ''

    def process_output(self, cmds):
        '''
        Process the output generated by the earlier commands.
        '''