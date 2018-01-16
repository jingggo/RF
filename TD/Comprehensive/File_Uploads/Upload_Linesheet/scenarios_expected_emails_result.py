EMAIL_EXPECTED_WARNINGS_INFO_EF = {
    'SCENARIO005' : '''WARNING(S):
line 1: [ER-80080] Color Code 001 with Color Description WHITE cannot be added for EF Style ES005A, since color code 002 with Color Description WHITE already exists for EF Style ES005A. Color Description cannot be duplicated.-/ES005A/001/WHITE/S/SMALL
line 2: [ER-80080] Color Code 100 with Color Description BLUE cannot be added for EF Style ES005B, since color code  with Color Description BLUE already exists for EF Style ES005B. Color Description cannot be duplicated.-/ES005B/100/BLUE/S/SMALL
''',
'SCENARIO009' : '''WARNING(S):
line 1: [ER-80082] Size Code S with Size LARGE cannot be added for EF Style ES009A, since size code L with Size LARGE already exists. Size cannot be duplicated. -/ES009A/001/RED/S/LARGE
line 2: [ER-80082] Size Code S with Size LARGE cannot be added for EF Style ES009B, since size code  with Size LARGE already exists. Size cannot be duplicated. -/ES009B/001/RED/S/LARGE
''',
'SCENARIO014' : '''WARNING(S):
line 1: [ER-80055] The style color, ES014A,002, to be dropped doesn't exist in our system yet.-/ES014A/002/BLUE/S/SMALL
line 2: [ER-80180] The style, ES014B, to be dropped does not exist in our system yet. -/ES014B/001/RED/S/SMALL
''',
'SCENARIO017' : '''WARNING(S):
line 1: [ER-80080] Color Code 002 with Color Description RED cannot be added for EF Style ES017A, since color code 001 with Color Description RED already exists for EF Style ES017A. Color Description cannot be duplicated.-/ES017A/002/RED/S/SMALL
line 2: [ER-80080] Color Code 001 with Color Description WHITE cannot be added for EF Style ES017A, since color code 002 with Color Description WHITE already exists for EF Style ES017A. Color Description cannot be duplicated.-/ES017A/001/WHITE/S/SMALL
line 3: [ER-80080] Color Code 001 with Color Description BLUE cannot be added for EF Style ES017B, since color code  with Color Description BLUE already exists for EF Style ES017B. Color Description cannot be duplicated.-/ES017B/001/BLUE/S/SMALL
line 4: [ER-80080] Color Code 001 with Color Description BLUE cannot be added for EF Style ES017C, since color code  with Color Description BLUE already exists for EF Style ES017C. Color Description cannot be duplicated.-/ES017C/001/BLUE/S/SMALL
''',
'SCENARIO020' : '''WARNING(S):
line 1: [ER-80082] Size Code 40 with Size LARGE cannot be added for EF Style ES020A, since size code 42 with Size LARGE already exists. Size cannot be duplicated. -/ES020A/001/RED/40/LARGE
line 2: [ER-80082] Size Code 42 with Size SMALL cannot be added for EF Style ES020A, since size code 40 with Size SMALL already exists. Size cannot be duplicated. -/ES020A/001/RED/42/SMALL
line 3: [ER-80082] Size Code 40 with Size LARGE cannot be added for EF Style ES020B, since size code  with Size LARGE already exists. Size cannot be duplicated. -/ES020B/001/RED/40/LARGE
line 4: [ER-80082] Size Code 40 with Size LARGE cannot be added for EF Style ES020C, since size code  with Size LARGE already exists. Size cannot be duplicated. -/ES020C/001/RED/40/LARGE
''',
'SCENARIO023' : '''WARNING(S):
line 1: [ER-80080] Color Code 001 with Color Description WHITE cannot be added for EF Style ES023A, since color code 002 with Color Description WHITE already exists for EF Style ES023A. Color Description cannot be duplicated.-2300/ES023A/001/WHITE/S/SMALL
line 2: [ER-80080] Color Code 001 with Color Description WHITE cannot be added for EF Style ES023B, since color code  with Color Description WHITE already exists for EF Style ES023B. Color Description cannot be duplicated.-2310/ES023B/001/WHITE/S/SMALL
''',
'SCENARIO026' : '''WARNING(S):
line 1: [ER-80082] Size Code S with Size LARGE cannot be added for EF Style ES026A, since size code L with Size LARGE already exists. Size cannot be duplicated. -2600/ES026A/001/RED/S/LARGE
line 2: [ER-80082] Size Code S with Size LARGE cannot be added for EF Style ES026B, since size code  with Size LARGE already exists. Size cannot be duplicated. -2610/ES026B/001/RED/S/LARGE
''',
'SCENARIO029' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES029A,001,SMALL, already exists in the system under a different upc number, 2901, than the one in flat file, 2900.-2900/ES029A/001/BLACK/S/SMALL
''',
'SCENARIO030' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES030A,001,SMALL, already exists in the system under a different upc number, 3001, than the one in flat file, 3000.-3000/ES030A/002/RED/S/SMALL
line 2: [ER-80033] The style/color/size combination, ES030B,001,SMALL, already exists in the system under a different upc number, 3011, than the one in flat file, 3010.-3010/ES030B//RED/S/SMALL
line 3: [ER-80033] The style/color/size combination, ES030C,,SMALL, already exists in the system under a different upc number, 3021, than the one in flat file, 3020.-3020/ES030C/001/RED/S/SMALL
''',
'SCENARIO031' : '''WARNING(S):
line 1: [ER-80080] Color Code 001 with Color Description BLACK cannot be added for EF Style ES031A, since color code 002 with Color Description BLACK already exists for EF Style ES031A. Color Description cannot be duplicated.-3100/ES031A/001/BLACK/S/SMALL
''',
'SCENARIO032' : '''WARNING(S):
line 1: [ER-80086] Color Code 002 with Color Description RED cannot be added for EF Style ES032A, since color code 002 with Color Description BLACK already exists for EF Style ES032A. Color Code cannot be duplicated.-3200/ES032A/002/RED/S/SMALL
''',
'SCENARIO035' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES035A,001,SMALL, already exists in the system under a different upc number, 3501, than the one in flat file, 3500.-3500/ES035A/001/RED/S/SMALLA
''',
'SCENARIO036' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES036A,001,SMALL, already exists in the system under a different upc number, 3601, than the one in flat file, 3600.-3600/ES036A/001/RED/40/SMALL
line 2: [ER-80033] The style/color/size combination, ES036B,001,SMALL, already exists in the system under a different upc number, 3611, than the one in flat file, 3610.-3610/ES036B/001/RED//SMALL
line 3: [ER-80033] The style/color/size combination, ES036C,001,SMALL, already exists in the system under a different upc number, 3621, than the one in flat file, 3620.-3620/ES036C/001/RED/S/SMALL
''',
'SCENARIO037' : '''WARNING(S):
line 1: [ER-80082] Size Code 40 with Size LARGE cannot be added for EF Style ES037A, since size code 42 with Size LARGE already exists. Size cannot be duplicated. -3700/ES037A/001/BLACK/40/LARGE
''',
'SCENARIO038' : '''WARNING(S):
line 1: [ER-80175] Size Code 42 with Size SMALL cannot be added for EF Style ES038A, since size code 42 with Size LARGE already exists for EF Style ES038A. Size Code cannot be duplicated. -3800/ES038A/001/RED/42/SMALL
''',
'SCENARIO039' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES039A,001,SMALL, already exists in the system under a different upc number, 3910, than the one in flat file, 3900.-3900/ES039A/001/RED/42/SMALL
''',
'SCENARIO041' : '''WARNING(S):
line 1: [ER-80032] The UPC number, 4100, already exists in the database, for a different style, ES041B, than the one specified in the flat file, ES041A.-4100/ES041A/001/RED/S/SMALL
''',
'SCENARIO049' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES049A,001,SMALL, already exists in the system under a different upc number, 4910, than the one in flat file, 4900.-4900/ES049A/001/RED/S/SMALL
''',
'SCENARIO050' : '''WARNING(S):
line 1: [ER-80032] The UPC number, 5000, already exists in the database, for a different style, ES050C, than the one specified in the flat file, ES050A.-5000/ES050A/001/RED/S/SMALL
''',
'SCENARIO051' : '''WARNING(S):
line 1: [ER-80032] The UPC number, 5100, already exists in the database, for a different style, ES051B, than the one specified in the flat file, ES051A.-5100/ES051A/001/RED/S/SMALL
''',
'SCENARIO058' : '''WARNING(S):
line 1: [ER-80180] The style, ES058A, to be dropped does not exist in our system yet. -5800.0/ES058A/001/RED/S/SMALL
''',
'SCENARIO059' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES059A,001,SMALL, already exists in the system under a different upc number, 5910.0, than the one in flat file, 5900.0.-5900.0/ES059A/001/RED/S/SMALL
''',
'SCENARIO061' : '''WARNING(S):
line 1: [ER-80180] The style, ES061A, to be dropped does not exist in our system yet. -6100.0/ES061A/001/RED/S/SMALL
''',
'SCENARIO062' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES062A,001,SMALL, already exists in the system under a different upc number, 62A123468789, than the one in flat file, 062A123468789.-062A123468789/ES062A/001/RED/S/SMALL
''',
'SCENARIO063' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES063A,001,SMALL, already exists in the system under a different upc number, 63A123468780, than the one in flat file, 063A123468789.-063A123468789/ES063A/001/RED/S/SMALL
''',
'SCENARIO066' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES066A,001,SMALL, already exists in the system under a different upc number, 66A123467789, than the one in flat file, 66A1234677890.-66A1234677890/ES066A/001/RED/S/SMALL
''',
'SCENARIO068' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES068A,001,SMALL, already exists in the system under a different upc number, 68A1234687899, than the one in flat file, 68A1234687890.-68A1234687890/ES068A/001/RED/S/SMALL
''',
'SCENARIO072' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES072A,001,SMALL, already exists in the system under a different upc number, 72A123456789, than the one in flat file, 072A123456789.-072A123456789/ES072A/001/RED/S/SMALL
''',
'SCENARIO074' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES074A,001,SMALL, already exists in the system under a different upc number, 74A1234567890, than the one in flat file, 074A123456789.-074A123456789/ES074A/001/RED/S/SMALL
''',
'SCENARIO076' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES076A,001,SMALL, already exists in the system under a different upc number, 76A123456789, than the one in flat file, 76A1234567890.-76A1234567890/ES076A/001/RED/S/SMALL
''',
'SCENARIO078' : '''WARNING(S):
line 1: [ER-80033] The style/color/size combination, ES078A,001,SMALL, already exists in the system under a different upc number, 78A1234578899, than the one in flat file, 78A1234578890.-78A1234578890/ES078A/001/RED/S/SMALL
''',
'SCENARIO081' : '''WARNING(S):
line 1: [ER-80056] Corporate Division is missing or not existent in our system yet.
''',
'SCENARIO082' : '''WARNING(S):
line 1: [ER-80056] Corporate Division is missing or not existent in our system yet.
''',
'SCENARIO083' : '''WARNING(S):
line 1: [ER-80072] Corporate Division is a buyer corporate division.
''',
'SCENARIO084' : '''WARNING(S):
line 1: Required field EF Style is blank.-8400.0//001/RED/S/SMALL
''',
'SCENARIO085' : '''WARNING(S):
line 1: Required field Color Description is blank.-8500.0/ES085A/001//S/SMALL
''',
'SCENARIO086' : '''WARNING(S):
line 1: Required field Size is blank.-8600.0/ES086A/001/RED/S/
''',
'SCENARIO092' : '''WARNING(S):
line 1: [ER-80077] Short Color Description WHT already exists in the system under style ES092A. Color Description in the system is WHITE, and Color Description in the linesheet is BLACK.  -/ES092A/001/BLACK/S/SMALL
line 2: [ER-80077] Short Color Description WHT already exists in the system under style ES092A. Color Description in the system is WHITE, and Color Description in the linesheet is BLUE.  -/ES092A/002/BLUE/S/SMALL
''',
'SCENARIO093' : '''WARNING(S):
line 1: [ER-80078] Short Color Description 012345BLACKA exceeds the maximum of 10 characters.-/ES093A/001/BLACK/S/SMALL
''',
'SCENARIO099' : '''WARNING(S):
line 1: [ER-80088] zReserve25 PTN-003 already exists in the system under ES099A, WHITE, and Color Description in the linesheet is BLACK.-/ES099A/001/BLACK/S/SMALL
line 2: [ER-80088] zReserve25 PTN-003 already exists in the system under ES099A, WHITE, and Color Description in the linesheet is BLUE.-/ES099A/002/BLUE/S/SMALL
''',
'SCENARIO100' : '''WARNING(S):
line 1: [ER-80089] zReserve25 PATTERN10012345678900000000000000000000000000000000000 can not exceed 30 characters.-/ES100A/001/BLACK/S/SMALL
''',
'SCENARIO101' : '''WARNING(S):
line 5: [ER-80174] Retail Price is not a valid number.-/ES101A/001/BLACK/S/SMALL
''',
'SCENARIO102' : '''WARNING(S):
line 5: [ER-80173] Wholesale Price is not a valid number.-/ES102A/001/BLACK/S/SMALL
''',
'SCENARIO103' : '''WARNING(S):
line 4: [ER-80169] Estimated Cost is not a valid number.-/ES103A/001/BLACK/S/SMALL
''',
'SCENARIO104' : '''WARNING(S):
line 1: Required field Fashion Season is blank.-/ES104A/001/BLACK/S/SMALL
line 2: [ER-80051] The season, ABC, is not defined in our system.-/ES104A/001/BLACK/S/SMALL
''',
'SCENARIO105' : '''WARNING(S):
line 2: [ER-80170] zReserve20 is not a valid number.-/ES105A/001/BLACK/S/SMALL
'''

}
# print EMAIL_EXPECTED_WARNINGS_INFO['SCENARIO005']