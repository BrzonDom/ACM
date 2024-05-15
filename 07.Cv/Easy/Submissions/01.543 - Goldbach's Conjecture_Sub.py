"""
543 - Goldbach's Conjecture
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=188&page=show_problem&problem=484

        In 1742, Christian Goldbach, a German amateur mathematician, sent a letter to Leonhard Euler in
    which he made the following conjecture:
        Every number greater than 2 can be written as the sum of three prime numbers.

        Goldbach was considering 1 as a primer number, a convention that is no longer followed. Later on,
    Euler re-expressed the conjecture as:
        Every even number greater than or equal to 4 can be expressed as the sum of two prime
    numbers.

        For example:
            • 8 = 3 + 5. Both 3 and 5 are odd prime numbers.
            • 20 = 3 + 17 = 7 + 13.
            • 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23.

        Today it is still unproven whether the conjecture is right. (Oh wait, I have the proof of course, but
    it is too long to write it on the margin of this page.)
        Anyway, your task is now to verify Goldbach’s conjecture as expressed by Euler for all even numbers
    less than a million

    Input:
            The input file will contain one or more test cases.
        Each test case consists of one even integer n with 6 ≤ n < 1000000.
        Input will be terminated by a value of 0 for n.

    Output:
            For each test case, print one line of the form n = a + b, where a and b are odd primes. Numbers and
        operators should be separated by exactly one blank like in the sample output below. If there is more
        than one pair of odd primes adding up to n, choose the pair where the difference b − a is maximized.
        If there is no such pair, print a line saying "Goldbach's conjecture is wrong."


    Sample:
        8
        20
        42
        0
            =>  8 = 3 + 5
                20 = 3 + 17
                42 = 5 + 37

"""

InputOrg_Raw = """
8
20
42
0
"""

InputDbg_Raw = """
999968
6
568
43422
989838
46
10
999998
748386
8
0
"""

InputMor_Raw = """
378
306
370
52
80
106
176
154
36
222
122
254
442
320
14
384
172
120
484
188
328
486
492
424
134
304
104
396
88
230
268
144
66
270
234
128
360
200
502
224
334
162
462
278
388
452
160
114
28
488
266
312
512
420
40
402
290
448
494
282
126
394
302
204
322
504
286
192
380
214
490
412
324
240
206
146
210
156
34
22
454
386
72
318
444
404
500
20
102
60
300
220
366
38
472
478
30
24
272
456
474
330
336
252
16
236
350
158
92
326
342
58
86
376
202
112
54
464
368
414
294
374
108
346
208
356
348
466
152
430
426
482
496
164
308
344
406
398
280
198
184
212
446
364
316
288
314
78
390
130
82
26
506
150
372
340
362
124
42
258
310
170
186
246
476
244
96
284
440
242
178
480
10
416
70
76
216
174
62
90
166
352
56
392
68
142
262
238
232
74
50
338
140
292
296
432
468
358
510
226
418
148
400
354
182
498
132
44
450
508
274
382
12
194
168
332
428
180
458
196
84
228
250
116
18
248
422
110
98
64
410
190
438
136
100
46
298
94
460
118
434
32
264
218
48
138
276
408
377626
237134
541068
862576
156652
995472
730950
774888
35834
958544
484992
99342
890350
454170
166390
288314
258270
170808
346868
112620
581600
367468
256722
200686
511508
340770
561280
533386
90310
445220
303176
541806
207086
687382
20964
410600
542594
517292
154308
157464
523466
341948
617062
637750
343730
292658
213930
933938
59932
976610
789420
820142
138064
739680
504648
572352
488996
819282
289940
455236
211724
552320
770802
216186
627326
409470
271454
737380
377438
743550
649922
620422
987114
647182
714754
765418
679686
544596
428388
292960
629082
644270
188582
987130
898866
639824
190532
94584
406452
465134
801148
584718
22188
309260
495106
109606
800070
730830
400146
199656
125372
832994
290716
983200
223716
252892
316382
261272
813810
232786
718990
304622
379486
948516
670916
182702
311644
869934
80322
831894
349372
640048
800952
58070
357504
878012
161052
751242
49744
470410
492800
972466
621476
23248
984992
421446
173378
993244
164108
527016
978742
163644
161582
139934
39116
831472
931720
217266
529228
492456
441646
838570
677640
644580
231528
478338
620078
938870
75476
218712
833278
219712
462534
923528
289020
908168
97942
18128
426366
569728
38688
718262
507416
589264
193308
290538
888754
912966
926470
291958
705386
945410
312428
674422
950816
119210
126098
438208
803482
508870
26342
912062
406670
837482
718848
682732
554476
442318
412034
480212
921688
413354
37374
837122
247832
694818
298840
751932
320846
606640
528782
703466
520460
721590
855726
945262
276196
726798
544408
132474
567804
92796
692954
105072
622076
590290
991426
660176
514744
456344
57680
444476
91220
507022
456928
429408
357856
758314
190798
423730
45556
622266
539472
804556
134976
171522
561140
244882
205276
781618
762860
70080
246806
657680
378254
848534
644610
963894
667752
632594
297976
873712
940620
793748
636118
797324
577730
87592
621310
389140
410394
423658
98736
396408
44916
674932
999548
181048
326556
213458
14104
639608
429768
792724
158404
498802
382622
540420
173988
968984
642748
936154
539388
952102
164220
853344
391518
418392
895264
912184
42152
697822
587734
421296
617176
338264
508090
729676
52824
157350
754394
347844
544460
546192
214760
854464
790194
413192
463482
631076
261878
889116
544360
828544
678642
924316
330374
277754
992594
370150
51028
329076
878476
420664
777290
164166
259436
972540
535794
781518
961768
557870
782652
855710
300394
760098
972824
237044
742158
477250
537210
572460
209562
629102
857872
246856
475868
836002
296186
905698
498126
346850
382644
52448
732820
588420
975592
587200
283722
694268
984308
625110
775052
346116
328240
497472
235560
183056
386338
207032
76758
868238
574340
484904
80818
936418
978868
142580
467846
253802
572834
61262
249840
772990
442700
600214
423202
715530
684034
824656
709306
945936
804206
16208
953670
539896
476844
327408
271152
899850
683178
38822
4698
406062
98464
861598
103432
156
39210
689326
764722
187928
876028
33568
675618
705646
812490
268238
1650
209036
666084
518140
433582
42276
731146
654756
300454
141008
169148
643264
588892
416860
317418
299092
330914
35732
389358
40278
704224
73588
638632
151700
730714
105328
522886
590514
941006
829194
594096
210102
475720
332822
317374
707344
98966
831456
520590
474806
821820
793328
258750
531292
562992
543632
260778
160796
981180
356512
745162
733664
730544
704170
101820
69808
111366
739618
834682
466992
690972
772418
14910
20020
319462
399246
477228
534630
994326
25914
179708
989060
605048
950286
894904
374150
97590
699392
318700
758054
126534
561672
155190
577698
807688
455340
454534
526010
797968
232454
116566
439146
60864
665058
66688
417752
942684
568306
17264
271474
682236
868112
756592
572200
2174
721678
993192
469628
163036
588494
193724
430990
852552
316582
281770
514466
881776
396632
264058
613564
116788
986010
609280
51666
382462
435036
65346
499926
904898
72566
305362
726418
607732
655194
577936
197700
566514
364666
498188
98286
305820
739770
940348
592110
328364
693294
475160
964572
867658
712
406916
812788
641068
705920
601460
341196
945448
363174
282230
413714
1010
301322
396794
437370
689938
227266
879904
399748
301166
494356
911530
611172
881156
102698
447518
912604
181734
836620
778788
860126
991418
360476
714288
407550
838584
400328
645252
485598
147566
811236
402410
799144
746356
117332
154040
720052
286692
848678
756792
436778
897784
553632
432966
909280
919784
820692
73354
608238
80192
138188
162010
810862
935690
414676
774108
341716
119104
740690
891824
78802
477166
978434
810170
277518
250896
713586
591732
198298
401850
215032
193012
826964
394596
197592
366836
557660
570066
306280
308326
497060
881174
894812
330816
621626
713784
290532
400888
687694
810048
650334
939878
325642
723470
19048
872468
415916
27804
928494
869618
960592
632522
428004
798412
129976
4768
776764
561254
619656
273470
55932
450196
96660
304090
200800
721822
557942
460734
269370
691904
523598
776874
722512
480552
275458
548070
442246
466034
982884
507658
424572
891652
358974
487614
416276
468766
510548
706262
722364
24674
8622
664064
967310
894948
257126
324538
818060
794424
197034
905430
993626
654066
829188
835478
782050
266768
418236
393464
472294
254644
635590
734856
936566
258126
215556
156614
783930
290058
663294
21332
525232
771310
4104
598064
59038
783726
238940
373388
731316
244498
2614
401130
768158
120074
176258
99040
806564
436628
64350
345116
917722
906898
575040
814750
845148
428984
393478
518200
189458
995720
834892
271406
680192
978216
938696
737438
194804
623186
209002
830692
487004
459258
803454
252400
811262
283220
669796
415392
380678
233372
160184
49308
890194
38116
2098
716296
847250
452012
724302
841876
318330
146332
372456
510038
207494
19768
326546
386484
863350
859212
170490
733246
863622
29080
225990
211098
956162
372778
169090
876106
915770
681960
372538
804438
229446
853270
679366
392198
452524
80096
737148
262198
812810
652428
608164
989190
276276
414034
827580
715772
336428
273260
248748
501880
89818
955514
844500
950338
737146
321898
77762
720094
391922
198786
199324
435650
815894
239818
532082
690484
854340
627528
677422
362470
150016
494132
278190
593592
744518
221208
320338
321422
527752
36414
25518
198656
261406
93672
643200
812688
244250
381708
104096
12474
562894
210426
797112
914080
219668
519108
660428
816578
754534
538470
167338
781168
206218
290208
91800
925646
84744
929216
235418
90060
103236
56154
473554
519160
704446
57206
917190
893858
464456
33438
207858
290396
373354
8596
695760
912682
889132
594970
760872
679952
415534
998772
300870
196578
764856
540720
969286
346516
539644
634034
136488
459686
945118
429420
94908
956902
194606
395642
62948
721348
718938
490628
992618
517336
490196
100004
214100
115628
59602
593426
474116
324340
336364
299614
897064
193822
985028
199824
534472
237974
661350
742846
940394
193030
977784
225768
810442
936286
677568
515036
209684
294958
801664
804862
902052
282840
37184
786870
243748
258024
448800
976696
335226
936010
587492
109648
152706
158896
18868
120500
317500
570502
529878
228154
57932
380160
125112
656822
426116
296470
824854
242652
484900
0
"""

InputTst_Raw = """
8
20
34
42
28
568
306
370
52
80
0
"""


InputOrg_Raw = InputOrg_Raw[1:-1]
InputDbg_Raw = InputDbg_Raw[1:-1]
InputMor_Raw = InputMor_Raw[1:-1]
InputTst_Raw = InputTst_Raw[1:-1]

InputRaw_Lst = [InputOrg_Raw, InputDbg_Raw, InputMor_Raw, InputTst_Raw]

InputRaw = InputRaw_Lst[3]


def fndPrimeTable(num):

    PrmTable = [False, False] + [True for i in range(2, num +1)]
    prm = 2

    while (prm ** 2 <= num):
        if PrmTable[prm]:

            for indx in range(prm ** 2, num +1, prm):
                PrmTable[indx] = False

        prm += 1

    return PrmTable


if __name__ == '__main__':

    print("Input:")
    print(InputRaw)
    print()

    InLines = InputRaw.split("\n")

    maxInNum = 1_000_000
    PrmTable = fndPrimeTable(maxInNum)

    num = int(InLines.pop(0))
    case = 1

    while num:

        print(f"\t{case}.Case")
        print()
        print(f"\t\tNum.: {num}")
        print()

        PrmLst = []

        for indx, PrmBl in enumerate(PrmTable[:num+1]):
            if PrmBl:
                PrmLst.append(indx)

        print(f"\t\tPrime List:  {PrmLst}")
        print()

        GldCnjctr = 0

        if num % 2 == 0:
            prmLen = num // 2 + 1
        else:
            prmLen = num // 2 + 2

        for indx in range(2, prmLen):
            if PrmTable[indx] and PrmTable[num - indx]:

                if not GldCnjctr:
                    GldCnjctr = (indx, num - indx)

                print(f"\t\t\t{num} = {indx} + {num - indx}")
        print()

        if GldCnjctr:
            print(f"\t\t\tResult Goldbach Conjecture:")
            print(f"\t\t\t\t{num} = {GldCnjctr[0]} + {GldCnjctr[1]}")
        else:
            print(f"\t\t\tGoldbach's conjecture is wrong.")
        print()

        num = int(InLines.pop(0))
        case += 1

        if num:
            print()


"""__Output__"""
"""
Input:
8
20
34
42
28
568
306
370
52
80
0

	1.Case

		Num.: 8

		Prime List:  [2, 3, 5, 7]

			8 = 3 + 5

			Result Goldbach Conjecture:
				8 = 3 + 5


	2.Case

		Num.: 20

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19]

			20 = 3 + 17
			20 = 7 + 13

			Result Goldbach Conjecture:
				20 = 3 + 17


	3.Case

		Num.: 34

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

			34 = 3 + 31
			34 = 5 + 29
			34 = 11 + 23
			34 = 17 + 17

			Result Goldbach Conjecture:
				34 = 3 + 31


	4.Case

		Num.: 42

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

			42 = 5 + 37
			42 = 11 + 31
			42 = 13 + 29
			42 = 19 + 23

			Result Goldbach Conjecture:
				42 = 5 + 37


	5.Case

		Num.: 28

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19, 23]

			28 = 5 + 23
			28 = 11 + 17

			Result Goldbach Conjecture:
				28 = 5 + 23


	6.Case

		Num.: 568

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563]

			568 = 5 + 563
			568 = 11 + 557
			568 = 47 + 521
			568 = 59 + 509
			568 = 89 + 479
			568 = 101 + 467
			568 = 107 + 461
			568 = 137 + 431
			568 = 149 + 419
			568 = 167 + 401
			568 = 179 + 389
			568 = 251 + 317
			568 = 257 + 311

			Result Goldbach Conjecture:
				568 = 5 + 563


	7.Case

		Num.: 306

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

			306 = 13 + 293
			306 = 23 + 283
			306 = 29 + 277
			306 = 37 + 269
			306 = 43 + 263
			306 = 67 + 239
			306 = 73 + 233
			306 = 79 + 227
			306 = 83 + 223
			306 = 107 + 199
			306 = 109 + 197
			306 = 113 + 193
			306 = 127 + 179
			306 = 139 + 167
			306 = 149 + 157

			Result Goldbach Conjecture:
				306 = 13 + 293


	8.Case

		Num.: 370

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367]

			370 = 3 + 367
			370 = 11 + 359
			370 = 17 + 353
			370 = 23 + 347
			370 = 53 + 317
			370 = 59 + 311
			370 = 89 + 281
			370 = 101 + 269
			370 = 107 + 263
			370 = 113 + 257
			370 = 131 + 239
			370 = 137 + 233
			370 = 173 + 197
			370 = 179 + 191

			Result Goldbach Conjecture:
				370 = 3 + 367


	9.Case

		Num.: 52

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

			52 = 5 + 47
			52 = 11 + 41
			52 = 23 + 29

			Result Goldbach Conjecture:
				52 = 5 + 47


	10.Case

		Num.: 80

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]

			80 = 7 + 73
			80 = 13 + 67
			80 = 19 + 61
			80 = 37 + 43

			Result Goldbach Conjecture:
				80 = 7 + 73


Process finished with exit code 0

"""
