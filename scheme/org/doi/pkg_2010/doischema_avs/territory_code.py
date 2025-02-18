from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class TerritoryCode(Enum):
    """
    Allowed values for Territories not included in the ISO 3166-1 list.

    :cvar AD: Andorra.
    :cvar AE: The United Arab Emirates.
    :cvar AF: Afghanistan.
    :cvar AG: Antigua and Barbuda.
    :cvar AI: Anguilla.
    :cvar AL: Albania.
    :cvar AM: Armenia.
    :cvar AO: Angola.
    :cvar AQ: Antarctica.
    :cvar AR: Argentina.
    :cvar AS: American Samoa.
    :cvar AT: Austria.
    :cvar AU: Australia.
    :cvar AW: Aruba.
    :cvar AX: Aaland Islands.
    :cvar AZ: Azerbaijan.
    :cvar BA: Bosnia and Herzegovina.
    :cvar BB: Barbados.
    :cvar BD: Bangladesh.
    :cvar BE: Belgium.
    :cvar BF: Burkina Faso.
    :cvar BG: Bulgaria.
    :cvar BH: Bahrain.
    :cvar BI: Burundi.
    :cvar BJ: Benin.
    :cvar BL: Saint Barthelemy.
    :cvar BM: Bermuda.
    :cvar BN: Brunei.
    :cvar BO: Bolivia.
    :cvar BQ: Bonaire, Sint Eustatius and Saba.
    :cvar BR: Brazil.
    :cvar BS: The Bahamas.
    :cvar BT: Bhutan.
    :cvar BV: Bouvet Island.
    :cvar BW: Botswana.
    :cvar BY: Belarus.
    :cvar BZ: Belize.
    :cvar CA: Canada.
    :cvar CC: Cocos Islands.
    :cvar CD: The Democratic Republic of the Congo.
    :cvar CF: The Central African Republic.
    :cvar CG: The Congo.
    :cvar CH: Switzerland.
    :cvar CI: Cote d'Ivoire.
    :cvar CK: Cook Islands.
    :cvar CL: Chile.
    :cvar CM: Cameroon.
    :cvar CN: China.
    :cvar CO: Colombia.
    :cvar CR: Costa Rica.
    :cvar CU: Cuba.
    :cvar CW: Curacao.
    :cvar CV: Cape Verde.
    :cvar CX: Christmas Island.
    :cvar CY: Cyprus.
    :cvar CZ: Czechia.
    :cvar DE: Germany.
    :cvar DJ: Djibouti.
    :cvar DK: Denmark.
    :cvar DM: Dominica.
    :cvar DO: The Dominican Republic.
    :cvar DZ: Algeria.
    :cvar EC: Ecuador.
    :cvar EE: Estonia.
    :cvar EG: Egypt.
    :cvar EH: Western Sahara.
    :cvar ER: Eritrea.
    :cvar ES: Spain.
    :cvar ET: Ethiopia.
    :cvar FI: Finland.
    :cvar FJ: Fiji.
    :cvar FK: Falkland Islands.
    :cvar FM: Micronesia.
    :cvar FO: Faroe Islands.
    :cvar FR: France.
    :cvar GA: Gabon.
    :cvar GB: The United Kingdom.
    :cvar GD: Grenada.
    :cvar GE: Georgia.
    :cvar GF: French Guiana.
    :cvar GG: Guernsey.
    :cvar GH: Ghana.
    :cvar GI: Gibraltar.
    :cvar GL: Greenland.
    :cvar GM: The Gambia.
    :cvar GN: Guinea.
    :cvar GP: Guadeloupe.
    :cvar GQ: Equatorial Guinea.
    :cvar GR: Greece.
    :cvar GS: South Georgia and The South Sandwich Islands.
    :cvar GT: Guatemala.
    :cvar GU: Guam.
    :cvar GW: Guinea-Bissau.
    :cvar GY: Guyana.
    :cvar HK: Hong Kong.
    :cvar HM: Heard Island and McDonald Islands.
    :cvar HN: Honduras.
    :cvar HR: Croatia.
    :cvar HT: Haiti.
    :cvar HU: Hungary.
    :cvar ID: Indonesia.
    :cvar IE: Ireland.
    :cvar IL: Israel.
    :cvar IM: Isle of Man.
    :cvar IN: India.
    :cvar IO: The British Indian Ocean Territory.
    :cvar IQ: Iraq.
    :cvar IR: Iran.
    :cvar IS: Iceland.
    :cvar IT: Italy.
    :cvar JE: Jersey.
    :cvar JM: Jamaica.
    :cvar JO: Jordan.
    :cvar JP: Japan.
    :cvar KE: Kenya.
    :cvar KG: Kyrgyzstan.
    :cvar KH: Cambodia.
    :cvar KI: Kiribati.
    :cvar KM: The Comoros.
    :cvar KN: Saint Kitts and Nevis.
    :cvar KP: The Democratic People's Republic of Korea.
    :cvar KR: The Republic of Korea.
    :cvar KW: Kuwait.
    :cvar KY: Cayman Islands.
    :cvar KZ: Kazakhstan.
    :cvar LA: Laos.
    :cvar LB: Lebanon.
    :cvar LC: Saint Lucia.
    :cvar LI: Liechtenstein.
    :cvar LK: Sri Lanka.
    :cvar LR: Liberia.
    :cvar LS: Lesotho.
    :cvar LT: Lithuania.
    :cvar LU: Luxembourg.
    :cvar LV: Latvia.
    :cvar LY: Libya.
    :cvar MA: Morocco.
    :cvar MC: Monaco.
    :cvar MD: Moldova.
    :cvar ME: Montenegro.
    :cvar MF: Saint Martin.
    :cvar MG: Madagascar.
    :cvar MH: The Marshall Islands.
    :cvar MK: North Macedonia.
    :cvar ML: Mali.
    :cvar MM: Myanmar.
    :cvar MN: Mongolia.
    :cvar MO: Macao.
    :cvar MP: Northern Mariana Islands.
    :cvar MQ: Martinique.
    :cvar MR: Mauritania.
    :cvar MS: Montserrat.
    :cvar MT: Malta.
    :cvar MU: Mauritius.
    :cvar MV: Maldives.
    :cvar MW: Malawi.
    :cvar MX: Mexico.
    :cvar MY: Malaysia.
    :cvar MZ: Mozambique.
    :cvar NA: Namibia.
    :cvar NC: New Caledonia.
    :cvar NE: The Niger.
    :cvar NF: Norfolk Island.
    :cvar NG: Nigeria.
    :cvar NI: Nicaragua.
    :cvar NL: The Netherlands.
    :cvar NO: Norway.
    :cvar NP: Nepal.
    :cvar NR: Nauru.
    :cvar NU: Niue.
    :cvar NZ: New Zealand.
    :cvar OM: Oman.
    :cvar PA: Panama.
    :cvar PE: Peru.
    :cvar PF: French Polynesia.
    :cvar PG: Papua New Guinea.
    :cvar PH: The Philippines.
    :cvar PK: Pakistan.
    :cvar PL: Poland.
    :cvar PM: Saint Pierre and Miquelon.
    :cvar PN: Pitcairn.
    :cvar PR: Puerto Rico.
    :cvar PS: Palestine, State of.
    :cvar PT: Portugal.
    :cvar PW: Palau.
    :cvar PY: Paraguay.
    :cvar QA: Qatar.
    :cvar RE: Reunion.
    :cvar RO: Romania.
    :cvar RS: Serbia.
    :cvar RU: Russia.
    :cvar RW: Rwanda.
    :cvar SA: Saudi Arabia.
    :cvar SB: Solomon Islands.
    :cvar SC: Seychelles.
    :cvar SD: The Sudan.
    :cvar SE: Sweden.
    :cvar SG: Singapore.
    :cvar SH: Saint Helena.
    :cvar SI: Slovenia.
    :cvar SJ: Svalbard and Jan Mayen.
    :cvar SK: Slovakia.
    :cvar SL: Sierra Leone.
    :cvar SM: San Marino.
    :cvar SN: Senegal.
    :cvar SO: Somalia.
    :cvar SR: Suriname.
    :cvar SS: South Sudan.
    :cvar ST: Sao Tome and Principe.
    :cvar SV: El Salvador.
    :cvar SX: Sint Maarten.
    :cvar SY: Syria.
    :cvar SZ: Eswatini.
    :cvar TC: Turks and Caicos Islands.
    :cvar TD: Chad.
    :cvar TF: The French Southern Territories.
    :cvar TG: Togo.
    :cvar TH: Thailand.
    :cvar TJ: Tajikistan.
    :cvar TK: Tokelau.
    :cvar TL: Timor-Leste.
    :cvar TM: Turkmenistan.
    :cvar TN: Tunisia.
    :cvar TO: Tonga.
    :cvar TR: Turkey.
    :cvar TT: Trinidad and Tobago.
    :cvar TV: Tuvalu.
    :cvar TW: Taiwan (Province of China).
    :cvar TZ: Tanzania.
    :cvar UA: Ukraine.
    :cvar UG: Uganda.
    :cvar UM: United States Minor Outlying Islands.
    :cvar US: The United States.
    :cvar UY: Uruguay.
    :cvar UZ: Uzbekistan.
    :cvar VA: The Holy See.
    :cvar VC: Saint Vincent and The Grenadines.
    :cvar VE: Venezuela.
    :cvar VG: British Virgin Islands.
    :cvar VI: US Virgin Islands.
    :cvar VN: Viet Nam.
    :cvar VU: Vanuatu.
    :cvar WF: Wallis and Futuna.
    :cvar WS: Samoa.
    :cvar XX: Country unknown.
    :cvar YE: Yemen.
    :cvar YT: Mayotte.
    :cvar ZA: South Africa.
    :cvar ZM: Zambia.
    :cvar ZW: Zimbabwe.
    :cvar ANHH: Netherlands Antilles.
    :cvar CSH: Czechoslovakia.
    :cvar CSHH: Czechoslovakia.
    :cvar DD: German Democratic Republic.
    :cvar DDDE: German Democratic Republic.
    :cvar SCG: Serbia and Montenegro.
    :cvar CSXX: Serbia and Montenegro.
    :cvar SU: USSR.
    :cvar SUHH: USSR.
    :cvar VD: Vietnam, Democratic Republic of.
    :cvar VDVN: Vietnam, Democratic Republic of.
    :cvar YD: Yemen, Democratic (South Yemen).
    :cvar YDYE: Yemen, Democratic (South Yemen).
    :cvar YU: Yugoslavia.
    :cvar YUCS: Yugoslavia.
    :cvar XK: Kosovo.
    """

    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CW = "CW"
    CV = "CV"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    XX = "XX"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"
    ANHH = "ANHH"
    CSH = "CSH"
    CSHH = "CSHH"
    DD = "DD"
    DDDE = "DDDE"
    SCG = "SCG"
    CSXX = "CSXX"
    SU = "SU"
    SUHH = "SUHH"
    VD = "VD"
    VDVN = "VDVN"
    YD = "YD"
    YDYE = "YDYE"
    YU = "YU"
    YUCS = "YUCS"
    XK = "XK"
