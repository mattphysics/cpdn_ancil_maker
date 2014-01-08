##############################################################################
#
#  Program : l19_data.py
#  Author  : Neil Massey
#  Purpose : Hybrid - eta level data for 19 levels for pp headers
#  Date    : 05/02/13
#
##############################################################################

def get_BLEV(level):
	BLEV  = [0.99699890613555908203,
			 0.97495591640472412109,
			 0.93041676282882690430,
			 0.86983227729797363281,
			 0.78750330209732055664,
			 0.67549401521682739258,
			 0.54141002893447875977,
			 0.40982252359390258789,
			 0.29886782169342041016,
			 0.21462798118591308594,
			 0.15287101268768310547,
			 0.10392451286315917969,
			 0.06302595138549804688,
			 0.03148680552840232849,
			 0.01062949001789093018,
			 0.00156006868928670883,
			 0.00000000000000000000,
			 0.00000000000000000000,
			 0.00000000000000000000]
	return BLEV[level]

##############################################################################

def get_BRLEV(level):
	BRLEV  = [1.00000000000000000000,
			  0.99400001764297485352,
			  0.95599997043609619141,
			  0.90499997138977050781,
			  0.83499997854232788086,
			  0.74060964584350585938,
			  0.61147761344909667969,
			  0.47272098064422607422,
			  0.34824669361114501953,
			  0.25052320957183837891,
			  0.17944884300231933594,
			  0.12681609392166137695, 
			  0.08157271146774291992,
			  0.04502478614449501038,
			  0.01847842335700988770,
			  0.00323968287557363510,
			  0.00000000000000000000,
			  0.00000000000000000000,
			  0.00000000000000000000]
	return BRLEV[level]

##############################################################################

def get_BHLEV(level):
	BHLEV = [0.00000000000000000000,
			 0.00000000000000000000,
			 0.00000000000000000000,
			 0.00000000000000000000,
			 472.51831054687500000000,
			 2408.03735351562500000000,
			 5809.32421875000000000000,
			 9469.93359375000000000000,
			 12323.53125000000000000000,
			 14006.97656250000000000000,
			 14688.06250000000000000000,
			 14577.72656250000000000000,
			 13660.08593750000000000000,
			 11801.44531250000000000000,
			 8861.73046875000000000000,
			 5529.41796875000000000000,
			 2959.43310546875000000000,
			 1479.71655273437500000000,
			 460.58813476562500000000]
	return BHLEV[level]

##############################################################################

def get_BHRLEV(level):
	BHRLEV = [0.00000000000000000000,
			  0.00000000000000000000,
			  0.00000000000000000000,
			  0.00000000000000000000,
			  0.00000000000000000000,
			  939.03735351562500000000,
			  3852.23779296875000000000,
			  7727.90234375000000000000,
			  11175.33203125000000000000,
			  13447.67968750000000000000,
			  14555.11718750000000000000,
			  14818.39453125000000000000,
			  14342.73046875000000000000,
			  12997.51953125000000000000,
			  10652.15625000000000000000,
			  7176.03125000000000000000,
			  4000.00000000000000000000,
			  2000.00000000000000000000,
			  1000.00000000000000000000]
	return BHRLEV[level]