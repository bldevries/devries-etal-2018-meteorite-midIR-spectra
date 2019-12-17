
BASEDIR_METS_OC_HTYPE = "data/"
BASEDIR_METS_HED = "data/"
BASEDIR_METS_IRON_STONE = "data/"

INFO_METS_OC_HTYPE = 	[{"name": "Bjelaja",\
							"type": "H",\
							"alteration": "6", \
							"dir": "BJELAJA_H6", \
							"filenames": [	"bjelaja_H6_S3_take1.0.dpt", "bjelaja_S1_take2.0.dpt", "bjelaja_S2_take2.0.dpt"], \
							},\
						{"name": "Bremervorde",\
							"type": "H",\
							"alteration": "3", \
							"dir": "BREMERVORDE_H3", \
							"filenames": [	"bremenvorde_S1_take2.0.dpt"], \
							#"BremervordeH3_S3_take1.0.dpt",,"bremervorde_S2_take1.0.dpt"
							},\
						{"name": "Charsonville",\
							"type": "H",\
							"alteration": "6", \
							"dir": "CHARSONVILLE_H6", \
							"filenames": [	"CharsonvilleH6_S1_take1.0.dpt"], \
							},\
						{"name": "Hessle",\
							"type": "H",\
							"alteration": "5", \
							"dir": "HESSLE_H5", \
							"filenames": [	"hessle_H5_S2.0.dpt"], \
							},\
							#"Hessle_S1_take5.0.dpt",
						{"name": "Menow",\
							"type": "H",\
							"alteration": "4", \
							"dir": "MENOW_H4", \
							"filenames": [	"MenowH4_S1_take2.0.dpt","menow_H4_S2.0.dpt"], \
							},\
						{"name": "Ochansk",\
							"type": "H",\
							"alteration": "4", \
							"dir": "OCHANSK_H4", \
							"filenames": [	"OchanskH4_S2_take2.0.dpt"], \
							#"OchanskH4_S1_take1.0.dpt",
							},\
						{"name": "Pultusk",\
							"type": "H",\
							"alteration": "5", \
							"dir": "PULTUSK_H5", \
							"filenames": [	"Pultusk_S1_take2.0.dpt"], \
							},\
						{"name": "Stalldalen",\
							"type": "H",\
							"alteration": "5", \
							"dir": "STALLDALEN_H5", \
							"filenames": [	"Stalldalen_S1_take2.0.dpt"], \
							},\
						]
INFO_METS_OC_HTYPE = sorted(INFO_METS_OC_HTYPE, key = lambda met: met["alteration"])





INFO_METS_OC_LTYPE = 	[{"name": "Bjurbole",\
							"type": "L",\
							"alteration": "4", \
							"dir": "BJURBOLE_L4", \
							"filenames": [	"Bjurbole_L4_S1_take4" ], \
							},\
						]
INFO_METS_OC_LTYPE = sorted(INFO_METS_OC_LTYPE, key = lambda met: met["alteration"])



INFO_METS_OC_LLTYPE = 	[{"name": "Ensisheim",\
							"type": "LL",\
							"alteration": "6", \
							"dir": "ENSISHEIM_LL6", \
							"filenames": [	"Ensisheim_LL6_take3" ], \
							},\
						{"name": "Soka-banja",\
							"type": "LL",\
							"alteration": "4", \
							"dir": "SOKABANJA_LL4", \
							"filenames": [	"Soka-banja_LL4_S1_take3" ], \
						},\
						]
INFO_METS_OC_LLTYPE = sorted(INFO_METS_OC_LLTYPE, key = lambda met: met["alteration"])



INFO_METS_HED = 		[{"name": "Bialystok",\
							"type": "How.",\
							"alteration": "-", \
							"dir": "BIALYSTOK_HOW", \
							"filenames": [	"BialystokHOW_S1_take1.0.dpt", \
											"BialystokHOW_S2_take1.0.dpt", \
											"BialystokHOW_S4boor_take1.0.dpt", \
											"BialystokHOW_S5_take1.0.dpt"], \
						},\
						{"name": "Juvinas",\
							"type": "Eucr.",\
							"alteration": "-", \
							"dir": "JUVINAS_EUCR", \
							"filenames": [	"JuvinasEUCR_S1b_take2.0.dpt","juvinas_EUCR_S2.0.dpt","juvinas_EUCR_S2_take2.0.dpt"], \
						},\
						{"name": "Luotolax",\
							"type": "How.",\
							"alteration": "-", \
							"dir": "LUOTOLAX2_HOW", \
							"filenames": [	"Luotolax2HOW_S1_take1.0.dpt"], \
						},\
						{"name": "Shalka",\
							"type": "Dio.",\
							"alteration": "-", \
							"dir": "SHALKA_DIO", \
							"filenames": [	"ShalkaDIO_S4_take1.0.dpt","shalka_S1_take1.0.dpt","shalka_S2_take1.0.dpt"], \
							#"ShalkaDIO_S3b_take2.0.dpt",
							},\
						{"name": "Stannern",\
							"type": "Eucr.",\
							"alteration": "-", \
							"dir": "STANNERN_EUCR", \
							"filenames": [	"StannernEUC_S3_take1.0.dpt","stannern_S1_take2.0.dpt","stannern_S2_take1.0.dpt"], \
							},\
						]
INFO_METS_HED = sorted(INFO_METS_HED, key = lambda met: met["type"])
						
						
INFO_METS_IRON_STONE = 	[{"name": "Seymehan",\
							"type": "Pal.",\
							"alteration": "-", \
							"dir": "PALLASITE", \
							"filenames": [	"Pal_S2_take2.0.dpt"], \
						},\
						]
INFO_METS_IRON_STONE = sorted(INFO_METS_IRON_STONE, key = lambda met: met["type"])
						