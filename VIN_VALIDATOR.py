import sys
import os

print("\nWelcome to Bahars VIN Validator")
def start():
    VIN = input("\nPlease enter a vin number: ")
    VIN2 = VIN.upper()
    VIN = VIN2

    while len(VIN) != 17:
        print("\nAll VINs must be exactly 17 characters")
        VIN = input("Please enter a vin number: ")

    # print("Analyzing VIN")
    # WMI LOOKUP TABLE
    dict2 = {
        "AAV": "Volkswagen South Africa",
        "AC5": "Hyundai South Africa",
        "ADD": "Hyundai South Africa",
        "AFA": "Ford South Africa",
        "AHT": "Toyota South Africa",
        "JA3": "Mitsubishi",
        "JA4": "Mitsubishi",
        "JA": "Isuzu",
        "JD": "Daihatsu",
        "JF": "Fuji Heavy Industries (Subaru)",
        "JH": "Honda",
        "JK": "Kawasaki (motorcycles)",
        "JL5": "Mitsubishi Fuso",
        "JMB": "Mitsubishi Motors",
        "JMY": "Mitsubishi Motors",
        "JMZ": "Mazda",
        "JN": "Nissan",
        "JS": "Suzuki",
        "JT": "Toyota",
        "JY": "Yamaha (motorcycles)",
        "KL": "Daewoo General Motors South Korea",
        "KM": "Hyundai",
        "KMY": "Daelim (motorcycles)",
        "KM1": "Hyosung (motorcycles)",
        "KN": "Kia",
        "KNM": "Renault Samsung",
        "KPA": "SsangYong",
        "KPT": "SsangYong",
        "LAN": "Changzhou Yamasaki Motorcycle",
        "LBB": "Zhejiang Qianjiang Motorcycle (Keeway/Generic)",
        "LBE": "Beijing Hyundai",
        "LBM": "Zongshen Piaggio",
        "LBP": "Chongqing Jainshe Yamaha (motorcycles)",
        "LB2": "Geely Motorcycles",
        "LCE": "Hangzhou Chunfeng Motorcycles (CFMOTO)",
        "LDC": "Dong Feng Peugeot Citroen (DPCA), China",
        "LDD": "Dandong Huanghai Automobile",
        "LDN": "SouEast Motor",
        "LDY": "Zhongtong Coach, China",
        "LET": "Jiangling-Isuzu Motors, China",
        "LE4": "Beijing Benz, China",
        "LFB": "FAW, China (busses)",
        "LFG": "Taizhou Chuanl Motorcycle Manufacturing",
        "LFP": "FAW, China (passenger vehicles)",
        "LFT": "FAW, China (trailers)",
        "LFV": "FAW-Volkswagen, China",
        "LFW": "FAW JieFang, China",
        "LFY": "Changshu Light Motorcycle Factory",
        "LGB": "Dong Feng (DFM), China",
        "LGH": "Qoros (formerly Dong Feng (DFM)), China",
        "LGX": "BYD Auto, China",
        "LHB": "Beijing Automotive Industry Holding",
        "LH1": "FAW-Haima, China",
        "LJC": "JAC, China",
        "LJ1": "JAC, China",
        "LKL": "Suzhou King Long, China",
        "LL6": "Hunan Changfeng Manufacture Joint-Stock",
        "LL8": "Linhai (ATV)",
        "LMC": "Suzuki Hong Kong (motorcycles)",
        "LPR": "Yamaha Hong Kong (motorcycles)",
        "LSG": "Shanghai General Motors, China",
        "LSJ": "MG Motor UK Limited - SAIC Motor, Shanghai, China",
        "LSV": "Shanghai Volkswagen, China",
        "LSY": "Brilliance Zhonghua",
        "LTV": "Toyota Tian Jin",
        "LUC": "Guangqi Honda, China",
        "LVS": "Ford Chang An",
        "LVV": "Chery, China",
        "LVZ": "Dong Feng Sokon Motor Company (DFSK)",
        "LZM": "MAN China",
        "LZE": "Isuzu Guangzhou, China",
        "LZG": "Shaanxi Automobile Group, China",
        "LZP": "Zhongshan Guochi Motorcycle (Baotian)",
        "LZY": "Yutong Zhengzhou, China",
        "LZZ": "Chongqing Shuangzing Mech & Elec (Howo)",
        "L4B": "Xingyue Group (motorcycles)",
        "L5C": "KangDi (ATV)",
        "L5K": "Zhejiang Yongkang Easy Vehicle",
        "L5N": "Zhejiang Taotao, China (ATV & motorcycles)",
        "L5Y": "Merato Motorcycle Taizhou Zhongneng",
        "L85": "Zhejiang Yongkang Huabao Electric Appliance",
        "L8X": "Zhejiang Summit Huawin Motorcycle",
        "MAB": "Mahindra & Mahindra",
        "MAC": "Mahindra & Mahindra",
        "MAJ": "Ford India",
        "MAK": "Honda Siel Cars India",
        "MAL": "Hyundai",
        "MAT": "Tata Motors",
        "MA1": "Mahindra & Mahindra",
        "MA3": "Suzuki India (Maruti)",
        "MA6": "GM India",
        "MA7": "Mitsubishi India (formerly Honda)",
        "MBH": "Suzuki India (Maruti)",
        "MBJ": "Toyota India",
        "MBR": "Mercedes-Benz India",
        "MB1": "Ashok Leyland",
        "MCA": "Fiat India",
        "MCB": "GM India",
        "MC2": "Volvo Eicher commercial vehicles limited.",
        "MDH": "Nissan India",
        "MD2": "Bajaj Auto",
        "MEE": "Renault India",
        "MEX": "Volkswagen India",
        "MHF": "Toyota Indonesia",
        "MHR": "Honda Indonesia",
        "MLC": "Suzuki Thailand",
        "MLH": "Honda Thailand",
        "MMB": "Mitsubishi Thailand",
        "MMC": "Mitsubishi Thailand",
        "MMM": "Chevrolet Thailand",
        "MMT": "Mitsubishi Thailand",
        "MM8": "Mazda Thailand",
        "MNB": "Ford Thailand",
        "MNT": "Nissan Thailand",
        "MPA": "Isuzu Thailand",
        "MP1": "Isuzu Thailand",
        "MRH": "Honda Thailand",
        "MR0": "Toyota Thailand",
        "NLA": "Honda Türkiye",
        "NLE": "Mercedes-Benz Türk Truck",
        "NLH": "Hyundai Assan",
        "NM0": "Ford Turkey",
        "NM4": "Tofaş Türk",
        "NMT": "Toyota Türkiye",
        "PE1": "Ford Phillipines",
        "PE3": "Mazda Phillipines",
        "PL1": "Proton, Malaysia",
        "PNA": "NAZA, Malaysia (Peugeot)",
        "RFB": "Kymco, Taiwan",
        "RFG": "Sanyang SYM, Taiwan",
        "RFL": "Adly, Taiwan",
        "RFT": "CPI, Taiwan",
        "RF3": "Aeon Motor, Taiwan",
        "SAL": "Land Rover",
        "SAJ": "Jaguar",
        "SAR": "Rover",
        "SB1": "Toyota UK",
        "SBM": "McLaren",
        "SCA": "Rolls Royce",
        "SCB": "Bentley",
        "SCC": "Lotus Cars",
        "SCE": "DeLorean Motor Cars N. Ireland (UK)",
        "SCF": "Aston",
        "SDB": "Peugeot UK (formerly Talbot)",
        "SED": "General Motors Luton Plant",
        "SEY": "LDV",
        "SFA": "Ford UK",
        "SFD": "Alexander Dennis UK",
        "SHH": "Honda UK",
        "SHS": "Honda UK",
        "SJN": "Nissan UK",
        "SKF": "Vauxhall",
        "SLP": "JCB Research UK",
        "SMT": "Triumph Motorcycles",
        "SUF": "Fiat Auto Poland",
        "SUL": "FSC (Poland)",
        "SUP": "FSO-Daewoo (Poland)",
        "SUU": "Solaris Bus & Coach (Poland)",
        "TCC": "Micro Compact Car AG (smart 1998-1999)",
        "TDM": "QUANTYA Swiss Electric Movement (Switzerland)",
        "TMA": "Hyundai Motor Manufacturing Czech",
        "TMB": "Škoda (Czech Republic)",
        "TMK": "Karosa (Czech Republic)",
        "TMP": "Škoda trolleybuses (Czech Republic)",
        "TMT": "Tatra (Czech Republic)",
        "TM9": "Škoda trolleybuses (Czech Republic)",
        "TNE": "TAZ",
        "TN9": "Karosa (Czech Republic)",
        "TRA": "Ikarus Bus",
        "TRU": "Audi Hungary",
        "TSE": "Ikarus Egyedi Autobuszgyar, (Hungary)",
        "TSM": "Suzuki Hungary",
        "TW1": "Toyota Caetano Portugal",
        "TYA": "Mitsubishi Trucks Portugal",
        "TYB": "Mitsubishi Trucks Portugal",
        "UU1": "Renault Dacia, (Romania)",
        "UU3": "ARO",
        "UU6": "Daewoo Romania",
        "U5Y": "Kia Motors Slovakia",
        "U6Y": "Kia Motors Slovakia",
        "VAG": "Magna Steyr Puch",
        "VAN": "MAN Austria",
        "VBK": "KTM (Motorcycles)",
        "VF1": "Renault",
        "VF2": "Renault",
        "VF3": "Peugeot",
        "VF4": "Talbot",
        "VF6": "Renault (Trucks & Buses)",
        "VF7": "Citroën",
        "VF8": "Matra",
        "VG5": "MBK (motorcycles)",
        "VLU": "Scania France",
        "VN1": "SOVAB (France)",
        "VNE": "Irisbus (France)",
        "VNK": "Toyota France",
        "VNV": "Renault-Nissan",
        "VSA": "Mercedes-Benz Spain",
        "VSE": "Suzuki Spain (Santana Motors)",
        "VSK": "Nissan Spain",
        "VSS": "SEAT",
        "VSX": "Opel Spain",
        "VS6": "Ford Spain",
        "VS7": "Citroën Spain",
        "VS9": "Carrocerias Ayats (Spain)",
        "VTH": "Derbi (motorcycles)",
        "VTT": "Suzuki Spain (motorcycles)",
        "VV9": "TAURO Spain",
        "VWA": "Nissan Spain",
        "VWV": "Volkswagen Spain",
        "VX1": "Zastava / Yugo Serbia",
        "WAG": "Neoplan",
        "WAU": "Audi",
        "WA1": "Audi SUV",
        "WBA": "BMW",
        "WBS": "BMW M",
        "WDA": "Daimler",
        "WDB": "Mercedes-Benz",
        "WDC": "DaimlerChrysler",
        "WDD": "Mercedes-Benz",
        "WDF": "Mercedes-Benz (commercial vehicles)",
        "WEB": "Evobus GmbH (Mercedes-Bus)",
        "WJM": "Iveco Magirus",
        "WF0": "Ford Germany",
        "WMA": "MAN Germany",
        "WME": "smart",
        "WMW": "MINI",
        "WMX": "Mercedes-AMG",
        "WP0": "Porsche",
        "WP1": "Porsche SUV",
        "W0L": "Opel",
        "WUA": "quattro GmbH",
        "WVG": "Volkswagen MPV/SUV",
        "WVW": "Volkswagen",
        "WV1": "Volkswagen Commercial Vehicles",
        "WV2": "Volkswagen Bus/Van",
        "WV3": "Volkswagen Trucks",
        "XLB": "Volvo (NedCar)",
        "XLE": "Scania Netherlands",
        "XLR": "DAF (trucks)",
        "XMC": "Mitsubishi (NedCar)",
        "XTA": "Lada/AutoVaz (Russia)",
        "XTT": "UAZ/Sollers (Russia)",
        "XUF": "General Motors Russia",
        "XUU": "AvtoTor (Russia, General Motors SKD)",
        "XW8": "Volkswagen Group Russia",
        "XWB": "UZ-Daewoo (Uzbekistan)",
        "XWE": "AvtoTor (Russia, Hyundai-Kia SKD)",
        "X4X": "AvtoTor (Russia, BMW SKD)",
        "X7L": "Renault AvtoFramos (Russia)",
        "X7M": "Hyundai TagAZ (Russia)",
        "YBW": "Volkswagen Belgium",
        "YCM": "Mazda Belgium",
        "YE2": "Van Hool (buses)",
        "YK1": "Saab-Valmet Finland",
        "YS2": "Scania AB",
        "YS3": "Saab",
        "YS4": "Scania Bus",
        "YTN": "Saab NEVS",
        "YU7": "Husaberg (motorcycles)",
        "YV1": "Volvo Cars",
        "YV4": "Volvo Cars",
        "YV2": "Volvo Trucks",
        "YV3": "Volvo Buses",
        "Y6D": "Zaporozhets/AvtoZAZ (Ukraine)",
        "ZAA": "Autobianchi",
        "ZAM": "Maserati",
        "ZAP": "Piaggio/Vespa/Gilera",
        "ZAR": "Alfa Romeo",
        "ZBN": "Benelli",
        "Z8M": "Marussia (Russia)",
        "ZCG": "Cagiva SpA / MV Agusta",
        "ZCF": "Iveco",
        "ZDM": "Ducati Motor Holdings SpA",
        "ZDF": "Ferrari Dino",
        "ZD0": "Yamaha Italy",
        "ZD3": "Beta Motor",
        "ZD4": "Aprilia",
        "ZFA": "Fiat",
        "ZFC": "Fiat V.I.",
        "ZFF": "Ferrari",
        "ZGU": "Moto Guzzi",
        "ZHW": "Lamborghini",
        "ZJM": "Malaguti",
        "ZJN": "Innocenti",
        "ZKH": "Husqvarna Motorcycles Italy",
        "ZLA": "Lancia",
        "ZOM": "OM",
        "1B3": "Dodge",
        "1C3": "Chrysler",
        "1C6": "Chrysler",
        "1D3": "Dodge",
        "1FA": "Ford Motor Company",
        "1FB": "Ford Motor Company",
        "1FC": "Ford Motor Company",
        "1FD": "Ford Motor Company",
        "1FM": "Ford Motor Company",
        "1FT": "Ford Motor Company",
        "1FU": "Freightliner",
        "1FV": "Freightliner",
        "1F9": "FWD Corp.",
        "1G": "General Motors USA",
        "1GC": "Chevrolet Truck USA",
        "1GT": "GMC Truck USA",
        "1G1": "Chevrolet USA",
        "1G2": "Pontiac USA",
        "1G3": "Oldsmobile USA",
        "1G4": "Buick USA",
        "1G6": "Cadillac USA",
        "1G8": "Saturn USA",
        "1GM": "Pontiac USA",
        "1GY": "Cadillac USA",
        "1H": "Honda USA",
        "1HD": "Harley-Davidson",
        "1J4": "Jeep",
        "1L": "Lincoln USA",
        "1ME": "Mercury USA",
        "1M1": "Mack Truck USA",
        "1M2": "Mack Truck USA",
        "1M3": "Mack Truck USA",
        "1M4": "Mack Truck USA",
        "1M9": "Mynatt Truck & Equipment",
        "1N": "Nissan USA",
        "1NX": "NUMMI USA",
        "1P3": "Plymouth USA",
        "1R9": "Roadrunner Hay Squeeze USA",
        "1VW": "Volkswagen USA",
        "1XK": "Kenworth USA",
        "1XP": "Peterbilt USA",
        "1YV": "Mazda USA (AutoAlliance International)",
        "1ZV": "Ford (AutoAlliance International)",
        "2A4": "Chrysler Canada",
        "2B3": "Dodge Canada",
        "2B7": "Dodge Canada",
        "2C3": "Chrysler Canada",
        "2CN": "CAMI",
        "2D3": "Dodge Canada",
        "2FA": "Ford Motor Company Canada",
        "2FB": "Ford Motor Company Canada",
        "2FC": "Ford Motor Company Canada",
        "2FM": "Ford Motor Company Canada",
        "2FT": "Ford Motor Company Canada",
        "2FU": "Freightliner",
        "2FV": "Freightliner",
        "2FZ": "Sterling",
        "2G": "General Motors Canada",
        "2G1": "Chevrolet Canada",
        "2G2": "Pontiac Canada",
        "2G3": "Oldsmobile Canada",
        "2G4": "Buick Canada",
        "2HG": "Honda Canada",
        "2HK": "Honda Canada",
        "2HJ": "Honda Canada",
        "2HM": "Hyundai Canada",
        "2M": "Mercury",
        "2NV": "Nova Bus Canada",
        "2P3": "Plymouth Canada",
        "2T": "Toyota Canada",
        "2V4": "Volkswagen Canada",
        "2V8": "Volkswagen Canada",
        "2WK": "Western Star",
        "2WL": "Western Star",
        "2WM": "Western Star",
        "3C4": "Chrysler Mexico",
        "3D3": "Dodge Mexico",
        "3FA": "Ford Motor Company Mexico",
        "3FE": "Ford Motor Company Mexico",
        "3G": "General Motors Mexico",
        "3H": "Honda Mexico",
        "3JB": "BRP Mexico (all-terrain vehicles)",
        "3MZ": "Mazda Mexico",
        "3N": "Nissan Mexico",
        "3P3": "Plymouth Mexico",
        "3VW": "Volkswagen Mexico",
        "4F": "Mazda USA",
        "4JG": "Mercedes-Benz USA",
        "4M": "Mercury",
        "4RK": "Nova Bus USA",
        "4S": "Subaru-Isuzu Automotive",
        "4T": "Toyota",
        "4UF": "Arctic Cat Inc.",
        "4US": "BMW USA",
        "4UZ": "Frt-Thomas Bus",
        "4V1": "Volvo",
        "4V2": "Volvo",
        "4V3": "Volvo",
        "4V4": "Volvo",
        "4V5": "Volvo",
        "4V6": "Volvo",
        "4VL": "Volvo",
        "4VM": "Volvo",
        "4VZ": "Volvo",
        "538": "Zero Motorcycles (USA)",
        "5F": "Honda USA-Alabama",
        "5L": "Lincoln",
        "5N1": "Nissan USA",
        "5NP": "Hyundai USA",
        "5T": "Toyota USA - trucks",
        "5YJ": "Tesla Motors",
        "6AB": "MAN Australia",
        "6F4": "Nissan Motor Company Australia",
        "6F5": "Kenworth Australia",
        "6FP": "Ford Motor Company Australia",
        "6G1": "General Motors-Holden (post Nov 2002)",
        "6G2": "Pontiac Australia (GTO & G8)",
        "6H8": "General Motors-Holden (pre Nov 2002)",
        "6MM": "Mitsubishi Motors Australia",
        "6T1": "Toyota Motor Corporation Australia",
        "6U9": "Privately Imported car in Australia",
        "8AD": "Peugeot Argentina",
        "8AF": "Ford Motor Company Argentina",
        "8AG": "Chevrolet Argentina",
        "8AJ": "Toyota Argentina",
        "8AK": "Suzuki Argentina",
        "8AP": "Fiat Argentina",
        "8AW": "Volkswagen Argentina",
        "8A1": "Renault Argentina",
        "8GD": "Peugeot Chile",
        "8GG": "Chevrolet Chile",
        "935": "Citroën Brazil",
        "936": "Peugeot Brazil",
        "93H": "Honda Brazil",
        "93R": "Toyota Brazil",
        "93U": "Audi Brazil",
        "93V": "Audi Brazil",
        "93X": "Mitsubishi Motors Brazil",
        "93Y": "Renault Brazil",
        "94D": "Nissan Brazil",
        "9BD": "Fiat Brazil",
        "9BF": "Ford Motor Company Brazil",
        "9BG": "Chevrolet Brazil",
        "9BM": "Mercedes-Benz Brazil",
        "9BR": "Toyota Brazil",
        "9BS": "Scania Brazil",
        "9BW": "Volkswagen Brazil",
        "9FB": "Renault Colombia"
    }
    # DEFINING WMI
    WMI = VIN[0:3]

    # Validating the WMI against the dictionairy
    WMI_LOOKUP = (dict2.get(WMI))

    # print(WMI)



    check_digit_value = {
        'A': '1',
        'B': '2',
        'C': '3',
        'D': '4',
        'E': '5',
        'F': '6',
        'G': '7',
        'H': '8',
        'J': '1',
        'K': '2',
        'L': '3',
        'M': '4',
        'N': '5',
        'P': '7',
        'R': '9',
        'S': '2',
        'T': '3',
        'U': '4',
        'V': '5',
        'W': '6',
        'X': '7',
        'Y': '8',
        'Z': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '0': '0'
    }
    # Defining Character 1 of the VIN
    # Defining the value assigned to char 1
    # multiplying char 1 by the weight factor
    # Repeated for each character of the VIN
    char1 = VIN[0:1]
    char1_value = check_digit_value.get(char1)
    char1_weight = (int(char1_value) * 8)

    char2 = VIN[1:2]
    char2_value = check_digit_value.get(char2)
    char2_weight = (int(char2_value) * 7)

    char3 = VIN[2:3]
    char3_value = check_digit_value.get(char3)
    char3_weight = (int(char3_value) * 6)

    char4 = VIN[3:4]
    char4_value = check_digit_value.get(char4)
    char4_weight = (int(char4_value) * 5)

    char5 = VIN[4:5]
    char5_value = check_digit_value.get(char5)
    char5_weight = (int(char5_value) * 4)

    char6 = VIN[5:6]
    char6_value = check_digit_value.get(char6)
    char6_weight = (int(char6_value) * 3)

    char7 = VIN[6:7]
    char7_value = check_digit_value.get(char7)
    char7_weight = (int(char7_value) * 2)

    char8 = VIN[7:8]
    char8_value = check_digit_value.get(char8)
    char8_weight = (int(char8_value) * 10)

    # Character 9 is excluded as this is the check digit

    char10 = VIN[10:11]
    char10_value = check_digit_value.get(char10)
    char10_weight = (int(char10_value) * 9)

    char11 = VIN[11:12]
    char11_value = check_digit_value.get(char11)
    char11_weight = (int(char11_value) * 8)

    char12 = VIN[12:13]
    char12_value = check_digit_value.get(char12)
    char12_weight = (int(char12_value) * 7)

    char13 = VIN[13:14]
    char13_value = check_digit_value.get(char13)
    char13_weight = (int(char13_value) * 6)

    char14 = VIN[13:14]
    char14_value = check_digit_value.get(char14)
    char14_weight = (int(char14_value) * 5)

    char15 = VIN[14:15]
    char15_value = check_digit_value.get(char15)
    char15_weight = (int(char15_value) * 4)

    char16 = VIN[15:16]
    char16_value = check_digit_value.get(char16)
    char16_weight = (int(char16_value) * 3)

    char17 = VIN[16:17]
    char17_value = check_digit_value.get(char17)
    char17_weight = (int(char17_value) * 2)

    # print(char1_weight)
    # print(char2_weight)
    Final_Weight = (
                       char1_weight + char2_weight + char3_weight + char4_weight + char5_weight +
                       char6_weight + char7_weight + char8_weight + char10_weight + char11_weight +
                       char12_weight + char13_weight + char14_weight + char15_weight + char16_weight + char17_weight
                   ) % 11
    print('\nYou entered: ', VIN)
    print('Location of Production/Manufacturer: ', WMI_LOOKUP)
    print('The calculated check digit is:', Final_Weight)
    print('The actual check digit is:', VIN[8:9])
    if Final_Weight == VIN[8:9]:
        print('\nThe calculated check digit matches the actual check digit, this vin looks okay to use')
        #COUNT = - 1
    elif Final_Weight != VIN[8:9:]:
        print(
            '\nThe calculated check digit does not match the actual check digit of the VIN, \nare you sure this is valid VIN number?')
        #COUNT = - 1
COUNT = 0
COUNT =- 1
while COUNT < 4:
    start()