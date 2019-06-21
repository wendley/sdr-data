#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Jun 10 19:08:59 2019
##################################################


from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import foo
import pmt


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp = samp = 32000

        ##################################################
        # Blocks
        ##################################################
        self.foo_periodic_msg_source_1 = foo.periodic_msg_source(pmt.intern("0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"), 500, 250, True, False)
        self.blocks_message_debug_0 = blocks.message_debug()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.foo_periodic_msg_source_1, 'out'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.foo_periodic_msg_source_1, 'out'), (self.blocks_message_debug_0, 'print_pdu'))

    def get_samp(self):
        return self.samp

    def set_samp(self, samp):
        self.samp = samp


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
