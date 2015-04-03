#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: IEEE 802.15.4 900 NHz Forwarder
# Author: Jay Kickliter
# Generated: Fri Apr  3 15:38:16 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import digital
from gnuradio import digital;import cmath
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import osmosdr
import sip
import sys
import time

from distutils.version import StrictVersion
class ieee802_15_4_900_MHz_ZMQ(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "IEEE 802.15.4 900 NHz Forwarder")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("IEEE 802.15.4 900 NHz Forwarder")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ieee802_15_4_900_MHz_ZMQ")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2.4e6
        self.oversampling = oversampling = 3
        self.const_symbols = const_symbols = [1, -1]
        self.channel = channel = 5
        self.tune_freq = tune_freq = (906+2*(channel-1))*1e6
        self.translate_taps = translate_taps = firdes.low_pass(1, samp_rate*oversampling,  samp_rate*0.9/2, samp_rate*0.5/2, firdes.WIN_HAMMING, 6.76)
        self.rx_mu = rx_mu = .25
        self.rrc_taps = rrc_taps = filter.firdes.root_raised_cosine( 4, 4, 1.0, .35, 11*32)
        self.rf_source = rf_source = 0
        self.freq_shift = freq_shift = -samp_rate*oversampling/4
        self.const_points = const_points = [1, -1]
        self.bpsk_const = bpsk_const = digital.constellation_calcdist((const_symbols), ([0,1]), 4, 1).base()
        self.balderf_rxvga = balderf_rxvga = 10

        ##################################################
        # Blocks
        ##################################################
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, "Spectrum")
        self.tabs_widget_1 = Qt.QWidget()
        self.tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_1)
        self.tabs_grid_layout_1 = Qt.QGridLayout()
        self.tabs_layout_1.addLayout(self.tabs_grid_layout_1)
        self.tabs.addTab(self.tabs_widget_1, "Constellation")
        self.tabs_widget_2 = Qt.QWidget()
        self.tabs_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_2)
        self.tabs_grid_layout_2 = Qt.QGridLayout()
        self.tabs_layout_2.addLayout(self.tabs_grid_layout_2)
        self.tabs.addTab(self.tabs_widget_2, "Setup")
        self.top_layout.addWidget(self.tabs)
        self._rx_mu_tool_bar = Qt.QToolBar(self)
        self._rx_mu_tool_bar.addWidget(Qt.QLabel("Mu (default 0.25)"+": "))
        self._rx_mu_line_edit = Qt.QLineEdit(str(self.rx_mu))
        self._rx_mu_tool_bar.addWidget(self._rx_mu_line_edit)
        self._rx_mu_line_edit.returnPressed.connect(
        	lambda: self.set_rx_mu(eng_notation.str_to_num(str(self._rx_mu_line_edit.text().toAscii()))))
        self.tabs_grid_layout_2.addWidget(self._rx_mu_tool_bar, 0,1,1,1)
        self._rf_source_options = (0, 1, )
        self._rf_source_labels = ("Live", "Recorded", )
        self._rf_source_tool_bar = Qt.QToolBar(self)
        self._rf_source_tool_bar.addWidget(Qt.QLabel("RF Source"+": "))
        self._rf_source_combo_box = Qt.QComboBox()
        self._rf_source_tool_bar.addWidget(self._rf_source_combo_box)
        for label in self._rf_source_labels: self._rf_source_combo_box.addItem(label)
        self._rf_source_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rf_source_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._rf_source_options.index(i)))
        self._rf_source_callback(self.rf_source)
        self._rf_source_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_rf_source(self._rf_source_options[i]))
        self.top_layout.addWidget(self._rf_source_tool_bar)
        self._balderf_rxvga_tool_bar = Qt.QToolBar(self)
        self._balderf_rxvga_tool_bar.addWidget(Qt.QLabel("RX VGA Gain (5-30)"+": "))
        self._balderf_rxvga_line_edit = Qt.QLineEdit(str(self.balderf_rxvga))
        self._balderf_rxvga_tool_bar.addWidget(self._balderf_rxvga_line_edit)
        self._balderf_rxvga_line_edit.returnPressed.connect(
        	lambda: self.set_balderf_rxvga(int(str(self._balderf_rxvga_line_edit.text().toAscii()))))
        self.tabs_grid_layout_2.addWidget(self._balderf_rxvga_tool_bar, 0,2,1,1)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_char, 1, "tcp://127.0.0.1:5555", 100)
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	10, samp_rate, 600e3, .35, 11*32))
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "bladerf" )
        self.osmosdr_source_0.set_sample_rate(samp_rate*oversampling)
        self.osmosdr_source_0.set_center_freq(tune_freq+freq_shift, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(balderf_rxvga, 0)
        self.osmosdr_source_0.set_if_gain(balderf_rxvga, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(int(oversampling), (translate_taps), -freq_shift, samp_rate*oversampling)
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(0, samp_rate)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.tabs_layout_0.addWidget(self._fosphor_qt_sink_c_0_win)
        self.digital_mpsk_receiver_cc_0 = digital.mpsk_receiver_cc(2, 0, cmath.pi/100.0, -0.5, 0.5, rx_mu, 0.01, 4, 0.001, 0.001)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(bpsk_const)
        self._const_symbols_tool_bar = Qt.QToolBar(self)
        self._const_symbols_tool_bar.addWidget(Qt.QLabel("Constellation Symbols"+": "))
        self._const_symbols_line_edit = Qt.QLineEdit(str(self.const_symbols))
        self._const_symbols_tool_bar.addWidget(self._const_symbols_line_edit)
        self._const_symbols_line_edit.returnPressed.connect(
        	lambda: self.set_const_symbols(eval(str(self._const_symbols_line_edit.text().toAscii()))))
        self.tabs_layout_2.addWidget(self._const_symbols_tool_bar)
        self._const_points_tool_bar = Qt.QToolBar(self)
        self._const_points_tool_bar.addWidget(Qt.QLabel("Constellation Points"+": "))
        self._const_points_line_edit = Qt.QLineEdit(str(self.const_points))
        self._const_points_tool_bar.addWidget(self._const_points_line_edit)
        self._const_points_line_edit.returnPressed.connect(
        	lambda: self.set_const_points(eval(str(self._const_points_line_edit.text().toAscii()))))
        self.tabs_layout_2.addWidget(self._const_points_tool_bar)
        self._channel_options = (1,2,3,4,5,6,7,8,9,10)
        self._channel_labels = ("1","2","3","4","5","6","7","8","9","10")
        self._channel_group_box = Qt.QGroupBox("Channel")
        self._channel_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._channel_button_group = variable_chooser_button_group()
        self._channel_group_box.setLayout(self._channel_box)
        for i, label in enumerate(self._channel_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._channel_box.addWidget(radio_button)
        	self._channel_button_group.addButton(radio_button, i)
        self._channel_callback = lambda i: Qt.QMetaObject.invokeMethod(self._channel_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._channel_options.index(i)))
        self._channel_callback(self.channel)
        self._channel_button_group.buttonClicked[int].connect(
        	lambda i: self.set_channel(self._channel_options[i]))
        self.top_layout.addWidget(self._channel_group_box)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/Users/jay/ieee802-15-4_BPSK_Packes_2.4MHz.dat", True)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=0 if rf_source == 0 else 1,
        	output_index=0,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_selector_0, 0), (self.fosphor_qt_sink_c_0, 0))    
        self.connect((self.blks2_selector_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blks2_selector_0, 1))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.zeromq_push_sink_0, 0))    
        self.connect((self.digital_mpsk_receiver_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blks2_selector_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_mpsk_receiver_cc_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ieee802_15_4_900_MHz_ZMQ")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_translate_taps(firdes.low_pass(1, self.samp_rate*self.oversampling,  self.samp_rate*0.9/2, self.samp_rate*0.5/2, firdes.WIN_HAMMING, 6.76))
        self.set_freq_shift(-self.samp_rate*self.oversampling/4)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(10, self.samp_rate, 600e3, .35, 11*32))
        self.fosphor_qt_sink_c_0.set_frequency_range(0, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate*self.oversampling)

    def get_oversampling(self):
        return self.oversampling

    def set_oversampling(self, oversampling):
        self.oversampling = oversampling
        self.set_translate_taps(firdes.low_pass(1, self.samp_rate*self.oversampling,  self.samp_rate*0.9/2, self.samp_rate*0.5/2, firdes.WIN_HAMMING, 6.76))
        self.set_freq_shift(-self.samp_rate*self.oversampling/4)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate*self.oversampling)

    def get_const_symbols(self):
        return self.const_symbols

    def set_const_symbols(self, const_symbols):
        self.const_symbols = const_symbols
        Qt.QMetaObject.invokeMethod(self._const_symbols_line_edit, "setText", Qt.Q_ARG("QString", repr(self.const_symbols)))

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        self.set_tune_freq((906+2*(self.channel-1))*1e6)
        self._channel_callback(self.channel)

    def get_tune_freq(self):
        return self.tune_freq

    def set_tune_freq(self, tune_freq):
        self.tune_freq = tune_freq
        self.osmosdr_source_0.set_center_freq(self.tune_freq+self.freq_shift, 0)

    def get_translate_taps(self):
        return self.translate_taps

    def set_translate_taps(self, translate_taps):
        self.translate_taps = translate_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.translate_taps))

    def get_rx_mu(self):
        return self.rx_mu

    def set_rx_mu(self, rx_mu):
        self.rx_mu = rx_mu
        self.digital_mpsk_receiver_cc_0.set_mu(self.rx_mu)
        Qt.QMetaObject.invokeMethod(self._rx_mu_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_mu)))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_rf_source(self):
        return self.rf_source

    def set_rf_source(self, rf_source):
        self.rf_source = rf_source
        self._rf_source_callback(self.rf_source)
        self.blks2_selector_0.set_input_index(int(0 if self.rf_source == 0 else 1))

    def get_freq_shift(self):
        return self.freq_shift

    def set_freq_shift(self, freq_shift):
        self.freq_shift = freq_shift
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(-self.freq_shift)
        self.osmosdr_source_0.set_center_freq(self.tune_freq+self.freq_shift, 0)

    def get_const_points(self):
        return self.const_points

    def set_const_points(self, const_points):
        self.const_points = const_points
        Qt.QMetaObject.invokeMethod(self._const_points_line_edit, "setText", Qt.Q_ARG("QString", repr(self.const_points)))

    def get_bpsk_const(self):
        return self.bpsk_const

    def set_bpsk_const(self, bpsk_const):
        self.bpsk_const = bpsk_const

    def get_balderf_rxvga(self):
        return self.balderf_rxvga

    def set_balderf_rxvga(self, balderf_rxvga):
        self.balderf_rxvga = balderf_rxvga
        Qt.QMetaObject.invokeMethod(self._balderf_rxvga_line_edit, "setText", Qt.Q_ARG("QString", str(self.balderf_rxvga)))
        self.osmosdr_source_0.set_gain(self.balderf_rxvga, 0)
        self.osmosdr_source_0.set_if_gain(self.balderf_rxvga, 0)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = ieee802_15_4_900_MHz_ZMQ()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
