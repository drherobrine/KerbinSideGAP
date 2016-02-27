from classes import Location


LOCATIONS = [
    Location(
        "Arakebo", "Arakebo, a small island with radio telescope observatory and post-flight rehabilitation clinic for kerbonauts.",
        helipad=(8.39111766626083, -180.356277756363, 59.557318418917),
        staff_spawn=(8.39117236570734, 179.64703981633, 1771.23),
        vip_spawn=(8.36093440437406, 179.770392040949, 1534.8),
    ),
    Location(
        "Ben Bay", "KashCorp headquarter in the Ben Bay, not far from the KSC.",
        helipad=(13.2242, 295.8152, 0.66342106659431),
        staff_spawn=(13.2267284856279, 295.815858741656, 43.0),
    ),
    Location(
        "Black Krags", "Small air base beside the Black Krags mountain range, primarily used for basic flight training.",
        runway=(11.32069, 272.3123, 3.95622218117586),
        staff_spawn=(11.3190436505737, 272.31832328877, 323.52),
    ),
    Location(
        "Coaler Crater", "Small airfield located in beautiful region of lakes and shores called Coaler Crater.",
        runway=(35.4291, 261.0945, 1.27468948499299),
        staff_spawn=(35.4287640702456, -98.9153758895753, 70.0),
    ),
    Location(
        "Deadkerbal Pit", "Deadkerbal Pit, a small base located in the mountains on the edge of desert, the site of designing and testing of new rockets.",
        helipad=(14.80408, 232.4043, 0.647423580090617),
        staff_spawn=(14.7999169992282, 232.406711265302, 1742.4),
    ),
    Location(
        "Donby Hole", "Centre of geological study inside the strange natural formation known as the Donby Hole.",
        helipad=(13.72265, 70.40235, 4.16918409778737),
        staff_spawn=(13.724772787249, 70.4016040312687, 2751.12),
    ),
    Location(
        "Dull Spot", "Dull Spot, launch site deep in the Northern hemisphere.",
        runway=(63.88354, 187.5524, 5.56440248873082),
        aircraft_parking=(63.876730581286, 187.541044753361, 0),
        staff_spawn=(63.8777644197737, -172.452817957359, 419.68),
    ),
    Location(
        "Dundard's Edge", "Dundard's Edge, a big base which is used as a control centre and a training facility for kerbonauts. At the base they can master climbing, rafting and advanced flight operations along the canyons.",
        runway=(44.2745305491, 227.997128716, 5.79139948578552),
        helipad=(44.2596627339441, 227.959103657763, 3.63258934393491),
        aircraft_parking=(44.2652271461589, 227.991633524058, 7.0059563111281),
        staff_spawn=(44.2700526212791, 227.993888765279, 529.51),
        vip_spawn=(44.2502939656543, 227.93067365952, 535.0),
    ),
    Location(
        "Everkrest", "Small building on the slope of the Everkrest, one of the highest mountains on the Kerbin.",
        helipad=(-14.12746, 71.6633, 11.1473559292263),
    ),
    Location(
        "Goldpool", "Harbour and launch site in the tropics called Goldpool.",
        runway=(-1.109713, 17.36675, 12.7),
        aircraft_parking=(-1.11830095796059, 17.3664163269982, 0),
    ),
    Location(
        "Green Coast", "Big civil airport and cargo terminal at the Green Coast, most popular recreation region of the Kerbin with lakes, mountains and shores.",
        runway=(-3.49212750587159, -180.907612573732, 10.1218623958989),
        helipad=(-3.46855039750813, -180.83576085199, 17.727578496491),
        aircraft_parking=(-3.46086334625836, 179.157880920185, 19.7611088085687),
        staff_spawn=(-3.4617914926101, 179.152744860731, 224.0),
    ),
    Location(
        "Green Peaks", "Research centre in the hills known as Green Peaks dedicated to botanical and medical studies.",
        helipad=(-0.737477884591802, 74.9546379624789, 4.3608049378995),
        staff_spawn=(-0.739690623767908, 74.9552405548738, 1247.01),
    ),
    Location(
        "Guardian's Basin", "Tourist base with a helipad in a beautiful natural region known as Guardian's Basin.",
        helipad=(42.648578076753, 309.092889848643, 2.22296484943934),
        vip_spawn=(42.6439852694047, 309.101840670913, 723.41),
    ),
    Location(
        "Hanbert Cape", "Base at the South edge of the continent called Hanbert Cape in the honour of a great explorer Hanbert Kerman.",
        runway=(-22.61177, 219.7454, 4),
        helipad=(-22.639811206298, -140.243582605172, 15.800478739664),
        aircraft_parking=(-22.6172210200695, 219.74438555693, 0),
        staff_spawn=(-22.6158025699809, -140.25358447833, 2.28),
    ),
    Location(
        "Jeb's island resort", "Beautifull island in the neighborhood of KSC where Jebediah Kerman founded a small resort area.",
        helipad=(6.84000613509939, 297.685691246224, 3.7230232043145),
        vip_spawn=(6.88682943360179, -62.2708200755656, 4.6),
    ),
    Location(
        "Kerbal Space Centre", "KSC, the largest launch base and main rocket science research centre of the Kerbin.",
        runway=(-0.0486018819242725, 285.275555148506, 5.21495180286001),
        helipad=(-0.09674856, 285.3801, 110.515307085542),
        aircraft_parking=(-0.0568078672556827, 285.379812232193, 4.08197237481365),
        staff_spawn=(-0.0600857127900175, 285.351339902779, 136.31),
        vip_spawn=(-0.161098320623303, 285.293799973877, 67.31),
    ),
    Location(
        "Kerbin's Bottom", "Small research centre with a radio telescope on the cold island called Kerbin's Bottom.",
        runway=(-50.49029, 170.5781, 3.5951428669272),
        staff_spawn=(-50.493478931433, 170.581499944252, 105.64),
    ),
    Location(
        "Kerbin's Heart Science Centre", "Large geological research center at the origins of the river in the mountains which some call Kerbin's Heart.",
        helipad=(-6.726014, 28.59504, 14.8870334017556),
        staff_spawn=(-6.72488120459909, 28.593858001468, 234.5),
    ),
    Location(
        "Kerman Lake", "Big privately owned airport on the Kerman Lake in arguably the most densely populated area of the Kerbin.",
        runway=(11.27818, 296.4742, 7.0027331045596),
        aircraft_parking=(11.2648333742561, 296.489015547998, 14.4414839718072),
        staff_spawn=(11.2731441321938, 296.475034302488, 39.76),
        vip_spawn=(11.1068885449674, 296.573192707247, 3.01),
    ),
    Location(
        "KKVLA", "Karl Kerbansky's Very Large Array, the largest radio-telescope on the Kerbin and big research centre in the middle of Kerbin's Greater Desert.",
        runway=(10.64686, 227.9027, 49.1146477503702),
        helipad=(10.60579, 227.7325, 17.1318576134508),
        aircraft_parking=(10.614287914325, 227.895632512688, 33.7199208256789),
        staff_spawn=(10.6050653577387, 227.731025147663, 362.01),
    ),
    Location(
        "Lake Dermal", "Cargo base and civil regional airport near the Lake Dermal.",
        runway=(22.70452, 239.0602, 11.7423487747088),
        aircraft_parking=(22.7201784337474, 239.047522440594, 10.0549880374438),
        staff_spawn=(22.7156010150095, 239.054085282486, 562.33),
    ),
    Location(
        "Lodnie Isles", "Civil airport serving the archipelago of the Lodnie Isles.",
        runway=(29.73803, 14.19844, 7.79231754690409),
        helipad=(29.7149223787791, -345.746572894317, 18.2566157514234),
        aircraft_parking=(29.6785100726076, 14.2740452565825, 27.4903752031969),
    ),
    Location(
        "Lushlands", "National airport of the Lushlands, agricultural country at the largest continent of the Kerbin.",
        runway=(2.156698, 26.61129, 11.1349510354921),
        aircraft_parking=(2.16889872403586, 26.6080078679358, 16.3203378152102),
        staff_spawn=(2.15958314872837, 26.6079362984866, 774.61),
    ),
    Location(
        "Mount Snowey", "Launch complex atop the Mount Snowey, one of the highest peaks of Blizzard Mountain Range.",
        helipad=(20.41318, 281.8346, 2.63161667715758),
        staff_spawn=(20.4140385716034, 281.831244667874, 3488.33),
    ),
    Location(
        "Old KSC", "The former main launch base and nowadays a big centre of space industry known as the Old KSC.",
        runway=(20.6503990966372, -146.439906824075, 1.8113792745861),
        aircraft_parking=(20.6061343501, 213.51535633634, 6.47058665752411),
        staff_spawn=(20.6457962912605, 213.548356408135, 430.31),
    ),
    Location(
        "Polar Research Centre", "Research centre located not far from Kerbin's North Pole.",
        runway=(79.57256, 282.5903, 3.5),
        aircraft_parking=(79.5711227141705, 282.61567112086, 4),
        staff_spawn=(79.5707975982126, 282.625004069961, 34.21),
        vip_spawn=(79.2599594082688, 281.555229370229, 45.76),
    ),
    Location(
        "Round Range", "Big airport serving the mountain areas at the East of the largest continent of the Kerbin, located in the mountain valley known as Round Range.",
        runway=(-6.01204632159655, -260.611086414459, 19.4767766136204),
        helipad=(-6.018824, 99.5179, 2.60995918814092),
        aircraft_parking=(-5.99826561874289, 99.4318812340424, 14.5831762446323),
    ),
    Location(
        "Sanctuary Mouth", "Base on the mouth of the Sanctuary River, which was originally used as a launch site and cargo terminal, but was further supplemented with the passenger terminal to serve as a civil airport for nearby cities.",
        runway=(23.68121, 320.0558, 13.25),
        aircraft_parking=(23.6745237270573, -39.9171745249947, 0.6764015702066),
    ),
    Location(
        "Sandy Island", "Small remote transit base on the sandy island near the equator.",
        helipad=(-3.233412, 352.9952, 0.891081437817775),
        staff_spawn=(-3.2332964146938, -7.002906893419, 42.06),
    ),
    Location(
        "Sea's End", "Experimental multi-purpose base on the coast of internal sea.",
        runway=(-34.11739, 79.79356, 6.6),
        aircraft_parking=(-34.1177194534825, 79.7754702934163, 3.25300717812497),
        staff_spawn=(-34.1193653188907, 79.7760386970776, 6.16),
    ),
    Location(
        "South Hope", "Big airport on the South Hope Islands, which is poorly maintained but is now the only airport serving Southern part of the continent, so having significant passenger flow and relatively intensive air traffic.",
        runway=(-49.7963406866008, -343.005398962152, 18.2511628786569),
        aircraft_parking=(-49.8015307171188, 17.0512006457721, 22.8991516382666),
    ),
    Location(
        "South Point", "Small airfield to the South of the Green Coast serving some charter flights.",
        runway=(-17.82059, 166.4277, 2.22185672563501),
        staff_spawn=(-17.8275243586205, 166.428828729991, 235.67),
    ),
    Location(
        "South Pole Station", "Station in the arctic very close to South Pole used for snow properties research, which provides facility for training kerbonauts to survive in extreme environment.",
        runway=(-84.73943, 142.7313, 1),
        helipad=(-84.73068, 142.6664, 0.6),
        staff_spawn=(-84.738, 142.692, 31.3),
    ),
    Location(
        "The Shelf", "Small air base between two large bays on the small island far to the South, mainly used as a transit point for cargo for South Pole Station.",
        runway=(-53.81633, 197.9046, 8.22618901217356),
        staff_spawn=(-53.8197, 197.9009, 314.01),
    ),
]