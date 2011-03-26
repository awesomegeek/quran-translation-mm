# Quran translation file separator
# This script will separate Quran Ayas to individual Sura files
# Author : Naing Tun Win 
# Last Modify : 10:45 PM Monday, March 21, 2011
import codecs
aya_range = [[0,7],[7,293],[293,493],[493,669],[669,789],[789,954],[954,1160],[1160,1235],[1235,1364],[1364,1473],[1473,1596],[1596,1707],[1707,1750],[1750,1802],[1802,1901],[1901,2029],[2029,2140],[2140,2250],[2250,2348],[2348,2483],[2483,2595],[2595,2673],[2673,2791],[2791,2855],[2855,2932],[2932,3159],[3159,3252],[3252,3340],[3340,3409],[3409,3469],[3469,3503],[3503,3533],[3533,3606],[3606,3660],[3660,3705],[3705,3788],[3788,3970],[3970,4058],[4058,4133],[4133,4218],[4218,4272],[4272,4325],[4325,4414],[4414,4473],[4473,4510],[4510,4545],[4545,4583],[4583,4612],[4612,4630],[4630,4675],[4675,4735],[4735,4784],[4784,4846],[4846,4901],[4901,4979],[4979,5075],[5075,5104],[5104,5126],[5126,5150],[5150,5163],[5163,5177],[5177,5188],[5188,5199],[5199,5217],[5217,5229],[5229,5241],[5241,5271],[5271,5323],[5323,5375],[5375,5419],[5419,5447],[5447,5475],[5475,5495],[5495,5551],[5551,5591],[5591,5622],[5622,5672],[5672,5712],[5712,5758],[5758,5800],[5800,5829],[5829,5848],[5848,5884],[5884,5909],[5909,5931],[5931,5948],[5948,5967],[5967,5993],[5993,6023],[6023,6043],[6043,6058],[6058,6079],[6079,6090],[6090,6098],[6098,6106],[6106,6125],[6125,6130],[6130,6138],[6138,6146],[6146,6157],[6157,6168],[6168,6176],[6176,6179],[6179,6188],[6188,6193],[6193,6197],[6197,6204],[6204,6207],[6207,6213],[6213,6216],[6216,6221],[6221,6225],[6225,6230],[6230,6236]]
print aya_range[3][1]
trans = codecs.open( "all_sura.txt", "r", "utf-8" )
ayas = trans.readlines();
trans.close()
sura = 0
for ar in aya_range:
	sura+=1
	fname = "%03d.txt" % (sura,)
	surafile = codecs.open(fname, encoding='utf-8', mode='w+')
	print 'Started..', fname
	surafile.writelines(ayas[ar[0]:ar[1]])	
	surafile.close()