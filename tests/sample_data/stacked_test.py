from shapely.wkt import loads


stacked_linestrings_wkt = [
    "LineString (345719.97399999998742715 6659968.78182000014930964, 345719.92930000001797453 6659968.87170000001788139, 345719.88810999999986961 6659968.9556099995970726, 345719.87560000002849847 6659968.99466000031679869, 345719.83720000000903383 6659969.11460999958217144, 345719.79431000002659857 6659969.24631000030785799, 345719.72405999997863546 6659969.55485999956727028)",
    "LineString (345719.88810999999986961 6659968.9556099995970726, 345719.8744099999894388 6659968.94295999966561794, 345719.68180999998003244 6659968.76510000042617321, 345719.570609999995213 6659968.67380999960005283, 345719.47940000001108274 6659968.57459999993443489, 345719.36820999998599291 6659968.40400000009685755)",
    "LineString (345719.98209000000497326 6659968.82447000034153461, 345719.97399999998742715 6659968.78182000014930964, 345719.94199999998090789 6659968.61290000006556511, 345719.93258000002242625 6659968.57517000008374453, 345719.91820999997435138 6659968.51769999973475933)",
    "LineString (345719.7923999999766238 6659969.42678000032901764, 345719.80971000000135973 6659969.31689999997615814, 345719.85310000000754371 6659969.15919999964535236, 345719.87210999999660999 6659969.08189999964088202, 345719.87560000002849847 6659968.99466000031679869, 345719.87560000002849847 6659968.99459999985992908, 345719.8744099999894388 6659968.94295999966561794)",
    "LineString (345719.91661000001477078 6659969.00360000040382147, 345719.89860000001499429 6659969.08610999956727028, 345719.88481000001775101 6659969.13910000026226044, 345719.87641000002622604 6659969.17930999957025051, 345719.86469999997643754 6659969.34860000014305115)",
    "LineString (345719.93258000002242625 6659968.57517000008374453, 345719.97460999997565523 6659968.61710000038146973, 345720.01910999999381602 6659968.66579999960958958, 345720.08889999997336417 6659968.73139999993145466, 345720.15402000001631677 6659968.80001000035554171, 345720.16720000002533197 6659968.8139000004157424, 345720.28999999997904524 6659968.89010000042617321)",
    "LineString (345720.09100000001490116 6659968.95791000034660101, 345720.15402000001631677 6659968.80001000035554171)",
]

stacked_linestrings = [loads(s) for s in stacked_linestrings_wkt]

non_simple_geometry = "LINESTRING (346898.82089 6659415.30809, 346898.8401 6659415.3273, 346898.9953 6659415.4825, 346899.04451 6659415.53171, 346899.08421 6659415.5714, 346899.26885 6659415.8124, 346899.30801 6659415.86351, 346899.3345646174 6659415.895288996, 346899.3177072111 6659415.875115049, 346899.32601 6659415.88505, 346899.39691 6659415.96991, 346899.46041 6659416.1111, 346899.5128 6659416.18261)"

overlaps_and_cuts_self = [
    "LineString (346489.41260000038892031 6659430.1453000009059906, 346489.97759999986737967 6659430.23499999940395355, 346489.92810000013560057 6659430.15300000086426735, 346489.70100000035017729 6659430.24799999967217445)",
    "LineString (346490.51599999982863665 6659431.41970000043511391, 346490.39950000029057264 6659431.20849999971687794, 346490.25870000012218952 6659430.70030000060796738, 346489.91399999987334013 6659430.12979999929666519, 346489.68910000007599592 6659429.6205000001937151, 346489.53039999958127737 6659429.38240000046789646)",
]
overlaps_and_cuts_self_linestrings = [loads(ls) for ls in overlaps_and_cuts_self]

results_in_non_simple_from_branches_and_nodes_wkt_list = [
    "LineString (346898.82220000028610229 6659415.30949999950826168, "
    "346899.08420000039041042 6659415.57139999978244305, 346899.3080000001937151 "
    "6659415.86350000090897083, 346899.39690000005066395 "
    "6659415.96990000084042549, 346899.46040000021457672 "
    "6659416.11119999922811985, 346899.5127999996766448 "
    "6659416.18260000087320805)",
    "LineString (346898.97690000012516975 6659415.77639999985694885, "
    "346899.04449999984353781 6659415.53170000016689301)",
    "LineString (346899.05719999969005585 6659415.24919999949634075, "
    "346898.995299999602139 6659415.48249999992549419)",
    "LineString (346899.31544413580559194 6659415.87240951787680387, "
    "346899.33299999963492155 6659416.03099999949336052, 346899.29729999974370003 "
    "6659416.12890000082552433)",
    "LineString (346898.84009999968111515 6659415.32740000076591969, "
    "346898.79559999983757734 6659415.44969999976456165, 346898.75109999999403954 "
    "6659415.59249999932944775, 346898.68759999983012676 "
    "6659415.74180000089108944, 346898.56859999988228083 "
    "6659415.89259999990463257, 346898.4256999995559454 "
    "6659416.02749999985098839, 346898.35900000017136335 "
    "6659416.16410000063478947, 346898.3335999995470047 "
    "6659416.26090000011026859, 346898.3240999998524785 "
    "6659416.38000000081956387, 346898.35269999969750643 "
    "6659416.51009999960660934, 346898.37330000009387732 "
    "6659416.56729999929666519)",
    "LineString (346899.26889999955892563 6659415.8125, 346899.35039999987930059 "
    "6659415.8205999992787838, 346899.401999999769032 6659415.85370000079274178)",
    "LineString (346899.32600000035017729 6659415.88499999977648258, "
    "346899.41789999976754189 6659415.86559999920427799, 346899.50779999978840351 "
    "6659415.85370000079274178, 346899.59910000022500753 "
    "6659415.88539999909698963, 346899.72350000031292439 "
    "6659415.91980000026524067, 346899.83330000005662441 "
    "6659415.97939999960362911, 346899.98139999993145466 "
    "6659416.10109999962151051, 346900.24870000034570694 "
    "6659416.40010000020265579, 346900.5014000004157424 "
    "6659416.64479999989271164, 346900.58069999981671572 "
    "6659416.72550000064074993, 346900.63889999967068434 "
    "6659416.86969999969005585, 346900.68389999959617853 "
    "6659416.92530000023543835, 346900.78050000034272671 "
    "6659416.97819999977946281, 346900.88760000001639128 "
    "6659417.01920000091195107, 346900.95509999990463257 "
    "6659417.0892999991774559, 346901.12179999984800816 "
    "6659417.31420000083744526, 346901.32820000033825636 "
    "6659417.55629999935626984, 346901.5411999998614192 6659417.8181999996304512, "
    "346901.57560000009834766 6659417.88169999979436398, 346901.59410000033676624 "
    "6659417.90289999917149544, 346901.63379999995231628 "
    "6659417.93600000068545341, 346901.8136999998241663 "
    "6659418.13040000014007092, 346901.82820000033825636 "
    "6659418.1436999998986721, 346901.88379999995231628 "
    "6659418.17809999920427799, 346901.92080000042915344 "
    "6659418.2653999999165535, 346901.95920000039041042 "
    "6659418.31829999946057796, 346901.98429999966174364 "
    "6659418.36329999938607216)",
]
results_in_non_simple_from_branches_and_nodes_linestring_list = [
    loads(s) for s in results_in_non_simple_from_branches_and_nodes_wkt_list
]

very_edgy_linestring_wkt_list = [
    "LineString (346477.98163914011092857 6659476.01762896403670311, "
    "346479.09436202549841255 6659476.96214955300092697, 346479.93537350866245106 "
    "6659477.1950450399890542, 346480.50467358954483643 "
    "6659476.85864044725894928, 346480.64699860982364044 "
    "6659476.15995398443192244, 346479.88361895584966987 "
    "6659475.75885619968175888, 346478.84852789965225384 "
    "6659475.52596071269363165)",
    "LineString (346474.75991822779178619 6659478.24954405426979065, "
    "346474.9928137154201977 6659478.30776792671531439, 346474.94752848171629012 "
    "6659478.54713273327797651, 346475.43919673340860754 "
    "6659478.39833839330822229, 346475.32274898956529796 "
    "6659478.82531345449388027, 346475.98908885702257976 "
    "6659478.50831681862473488, 346475.97615021880483255 "
    "6659479.04527030419558287, 346476.68130600085714832 "
    "6659478.74121230654418468, 346477.06946514692390338 "
    "6659479.10996349528431892, 346476.6554287244216539 6659479.5110612791031599, "
    "346477.59347999410238117 6659479.20700328145176172)",
    "LineString (346479.22374840750126168 6659479.20053396187722683, "
    "346479.05554611090337858 6659480.05448408331722021, 346479.97418942325748503 "
    "6659479.53693855460733175, 346479.35313478956231847 "
    "6659480.49439778178930283, 346480.68581452441867441 "
    "6659480.14505455084145069, 346479.92243487044470385 "
    "6659480.93431148119270802, 346481.48801009292947128 "
    "6659480.63672280218452215)",
    "LineString (346475.2515864793676883 6659476.01762896403670311, "
    "346477.06299582769861445 6659477.32443142216652632, 346476.610143490601331 "
    "6659476.17289262264966965, 346478.33098237152444199 "
    "6659477.84197695087641478, 346478.30510509514715523 "
    "6659477.1044745733961463, 346479.67660074459854513 "
    "6659478.55360205192118883)",
]
very_edgy_linestring_list = [loads(s) for s in very_edgy_linestring_wkt_list]

not_so_edgy_linestrings = [
    "LineString (346457.71063794760266319 6659475.89921558275818825, "
    "346459.81883675989229232 6659478.93502187263220549, 346462.81247907329816371 "
    "6659481.38053249474614859, 346463.27628281200304627 "
    "6659486.01856988202780485, 346468.46245189028559253 "
    "6659487.11483326368033886, 346466.4385810304665938 "
    "6659491.62637872248888016)",
    "LineString (346458.55391747254179791 6659466.24366502277553082, "
    "346464.79418595688184723 6659477.54361065663397312, 346473.31130915856920183 "
    "6659487.15699724014848471, 346487.64706108212703839 "
    "6659495.25248067919164896, 346494.39329728146549314 "
    "6659497.86664720717817545)",
    "LineString (346449.19351474597351626 6659472.73691736441105604, "
    "346454.59050370543263853 6659482.09732009097933769, 346453.83155213296413422 "
    "6659490.8674271497875452, 346457.28899818513309583 "
    "6659496.93903972953557968, 346462.51733123965095729 "
    "6659499.5532062565907836, 346468.92625562899047509 "
    "6659502.50468459352850914)",
    "LineString (346438.98983249446609989 6659477.79659451358020306, "
    "346440.84504744922742248 6659481.00105670839548111, 346444.21816554892575368 "
    "6659483.02492756769061089)",
]
not_so_edgy_linestrings_list = [loads(s) for s in not_so_edgy_linestrings]

should_or_shouldnt_pass_sharp_turns = [
    "LineString (353004.18410000018775463 6666732.97519999928772449, "
    "353935.52500000037252903 6667286.83049999922513962, 354443.39089999999850988 "
    "6667702.35720000043511391, 354739.72479999996721745 "
    "6668273.85830000042915344, 355266.37799999956041574 "
    "6670003.83999999985098839, 355099.55889999959617853 "
    "6672316.69969999976456165, 354231.72379999980330467 "
    "6674179.37010000087320805, 352517.2203999999910593 "
    "6678201.04480000026524067)",
    "LineString (345697.22200000006705523 6659728.68679999932646751, "
    "345697.90240000002086163 6659728.46189999952912331, 345698.37550000008195639 "
    "6659728.12419999949634075, 345698.70449999999254942 "
    "6659727.65279999934136868, 345698.95839999988675117 "
    "6659727.34420000016689301, 345699.00629999954253435 "
    "6659727.24120000004768372, 345698.99710000026971102 "
    "6659727.09840000048279762, 345699.05759999994188547 "
    "6659726.77239999920129776, 345699.14099999982863665 "
    "6659726.44219999946653843, 345699.13850000035017729 "
    "6659726.16699999943375587, 345698.84900000039488077 "
    "6659725.75699999928474426)",
]

should_pass_sharp_turns_ls_list = [
    loads(s) for s in should_or_shouldnt_pass_sharp_turns
]
