# Generated from grammar/JSSParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,62,475,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,1,0,5,0,106,
        8,0,10,0,12,0,109,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,118,8,1,1,
        2,1,2,1,2,1,2,1,2,5,2,125,8,2,10,2,12,2,128,9,2,1,3,1,3,1,4,1,4,
        1,4,3,4,135,8,4,1,5,1,5,3,5,139,8,5,1,6,1,6,1,6,1,6,5,6,145,8,6,
        10,6,12,6,148,9,6,3,6,150,8,6,1,6,1,6,1,7,1,7,3,7,156,8,7,1,8,1,
        8,3,8,160,8,8,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,3,11,170,8,11,
        1,12,1,12,1,12,1,12,5,12,176,8,12,10,12,12,12,179,9,12,1,12,1,12,
        1,13,1,13,1,13,3,13,186,8,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,3,15,196,8,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,205,8,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,3,17,215,8,17,1,17,1,
        17,1,17,1,18,1,18,1,18,5,18,223,8,18,10,18,12,18,226,9,18,1,19,1,
        19,1,19,1,20,1,20,5,20,233,8,20,10,20,12,20,236,9,20,1,20,1,20,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,263,8,21,1,
        22,1,22,1,22,1,22,1,22,1,22,5,22,271,8,22,10,22,12,22,274,9,22,1,
        22,3,22,277,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,
        24,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,3,26,298,8,26,1,
        26,1,26,3,26,302,8,26,1,26,1,26,3,26,306,8,26,1,26,1,26,1,26,1,27,
        1,27,3,27,313,8,27,1,28,1,28,1,29,1,29,3,29,319,8,29,1,30,1,30,1,
        30,3,30,324,8,30,1,30,1,30,1,31,1,31,1,31,5,31,331,8,31,10,31,12,
        31,334,9,31,1,32,1,32,1,33,1,33,1,33,3,33,341,8,33,1,33,1,33,1,34,
        1,34,1,35,1,35,1,35,1,35,1,35,3,35,352,8,35,1,36,1,36,1,37,1,37,
        1,37,5,37,359,8,37,10,37,12,37,362,9,37,1,38,1,38,1,38,5,38,367,
        8,38,10,38,12,38,370,9,38,1,39,1,39,1,39,5,39,375,8,39,10,39,12,
        39,378,9,39,1,40,1,40,1,40,5,40,383,8,40,10,40,12,40,386,9,40,1,
        41,1,41,1,41,5,41,391,8,41,10,41,12,41,394,9,41,1,42,1,42,1,42,5,
        42,399,8,42,10,42,12,42,402,9,42,1,43,1,43,1,43,3,43,407,8,43,1,
        44,1,44,1,44,3,44,412,8,44,1,45,1,45,5,45,416,8,45,10,45,12,45,419,
        9,45,1,46,1,46,1,46,1,46,3,46,425,8,46,1,46,1,46,1,46,1,46,1,46,
        1,46,1,46,1,46,1,46,3,46,436,8,46,1,46,3,46,439,8,46,1,47,1,47,1,
        47,1,47,1,47,1,47,1,47,1,47,1,47,3,47,450,8,47,1,48,1,48,1,48,1,
        48,3,48,456,8,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,
        50,5,50,468,8,50,10,50,12,50,471,9,50,1,51,1,51,1,51,0,0,52,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,
        94,96,98,100,102,0,9,1,0,1,2,1,0,20,23,2,0,24,29,39,39,1,0,30,31,
        2,0,32,33,40,41,1,0,43,44,1,0,45,47,2,0,36,37,42,44,2,0,15,17,57,
        59,483,0,107,1,0,0,0,2,117,1,0,0,0,4,119,1,0,0,0,6,129,1,0,0,0,8,
        131,1,0,0,0,10,138,1,0,0,0,12,140,1,0,0,0,14,153,1,0,0,0,16,159,
        1,0,0,0,18,161,1,0,0,0,20,163,1,0,0,0,22,169,1,0,0,0,24,171,1,0,
        0,0,26,185,1,0,0,0,28,187,1,0,0,0,30,191,1,0,0,0,32,200,1,0,0,0,
        34,209,1,0,0,0,36,219,1,0,0,0,38,227,1,0,0,0,40,230,1,0,0,0,42,262,
        1,0,0,0,44,264,1,0,0,0,46,278,1,0,0,0,48,285,1,0,0,0,50,288,1,0,
        0,0,52,294,1,0,0,0,54,312,1,0,0,0,56,314,1,0,0,0,58,316,1,0,0,0,
        60,320,1,0,0,0,62,327,1,0,0,0,64,335,1,0,0,0,66,337,1,0,0,0,68,344,
        1,0,0,0,70,351,1,0,0,0,72,353,1,0,0,0,74,355,1,0,0,0,76,363,1,0,
        0,0,78,371,1,0,0,0,80,379,1,0,0,0,82,387,1,0,0,0,84,395,1,0,0,0,
        86,403,1,0,0,0,88,411,1,0,0,0,90,413,1,0,0,0,92,438,1,0,0,0,94,449,
        1,0,0,0,96,451,1,0,0,0,98,459,1,0,0,0,100,464,1,0,0,0,102,472,1,
        0,0,0,104,106,3,2,1,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,
        0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,5,
        0,0,1,111,1,1,0,0,0,112,118,3,24,12,0,113,118,3,34,17,0,114,115,
        3,4,2,0,115,116,5,54,0,0,116,118,1,0,0,0,117,112,1,0,0,0,117,113,
        1,0,0,0,117,114,1,0,0,0,118,3,1,0,0,0,119,120,3,6,3,0,120,121,3,
        14,7,0,121,126,3,8,4,0,122,123,5,55,0,0,123,125,3,8,4,0,124,122,
        1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,5,1,
        0,0,0,128,126,1,0,0,0,129,130,7,0,0,0,130,7,1,0,0,0,131,134,5,60,
        0,0,132,133,5,39,0,0,133,135,3,10,5,0,134,132,1,0,0,0,134,135,1,
        0,0,0,135,9,1,0,0,0,136,139,3,68,34,0,137,139,3,12,6,0,138,136,1,
        0,0,0,138,137,1,0,0,0,139,11,1,0,0,0,140,149,5,52,0,0,141,146,3,
        68,34,0,142,143,5,55,0,0,143,145,3,68,34,0,144,142,1,0,0,0,145,148,
        1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,150,1,0,0,0,148,146,
        1,0,0,0,149,141,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,
        5,53,0,0,152,13,1,0,0,0,153,155,3,16,8,0,154,156,3,20,10,0,155,154,
        1,0,0,0,155,156,1,0,0,0,156,15,1,0,0,0,157,160,3,18,9,0,158,160,
        5,60,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,17,1,0,0,0,161,162,
        7,1,0,0,162,19,1,0,0,0,163,164,5,52,0,0,164,165,5,58,0,0,165,166,
        5,53,0,0,166,21,1,0,0,0,167,170,3,14,7,0,168,170,5,4,0,0,169,167,
        1,0,0,0,169,168,1,0,0,0,170,23,1,0,0,0,171,172,5,5,0,0,172,173,5,
        60,0,0,173,177,5,50,0,0,174,176,3,26,13,0,175,174,1,0,0,0,176,179,
        1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,177,
        1,0,0,0,180,181,5,51,0,0,181,25,1,0,0,0,182,186,3,28,14,0,183,186,
        3,30,15,0,184,186,3,32,16,0,185,182,1,0,0,0,185,183,1,0,0,0,185,
        184,1,0,0,0,186,27,1,0,0,0,187,188,3,14,7,0,188,189,5,60,0,0,189,
        190,5,54,0,0,190,29,1,0,0,0,191,192,5,60,0,0,192,193,5,6,0,0,193,
        195,5,48,0,0,194,196,3,36,18,0,195,194,1,0,0,0,195,196,1,0,0,0,196,
        197,1,0,0,0,197,198,5,49,0,0,198,199,3,40,20,0,199,31,1,0,0,0,200,
        201,3,22,11,0,201,202,5,60,0,0,202,204,5,48,0,0,203,205,3,36,18,
        0,204,203,1,0,0,0,204,205,1,0,0,0,205,206,1,0,0,0,206,207,5,49,0,
        0,207,208,3,40,20,0,208,33,1,0,0,0,209,210,5,3,0,0,210,211,3,22,
        11,0,211,212,5,60,0,0,212,214,5,48,0,0,213,215,3,36,18,0,214,213,
        1,0,0,0,214,215,1,0,0,0,215,216,1,0,0,0,216,217,5,49,0,0,217,218,
        3,40,20,0,218,35,1,0,0,0,219,224,3,38,19,0,220,221,5,55,0,0,221,
        223,3,38,19,0,222,220,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,
        225,1,0,0,0,225,37,1,0,0,0,226,224,1,0,0,0,227,228,3,14,7,0,228,
        229,5,60,0,0,229,39,1,0,0,0,230,234,5,50,0,0,231,233,3,42,21,0,232,
        231,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,
        237,1,0,0,0,236,234,1,0,0,0,237,238,5,51,0,0,238,41,1,0,0,0,239,
        263,3,40,20,0,240,241,3,4,2,0,241,242,5,54,0,0,242,263,1,0,0,0,243,
        263,3,44,22,0,244,263,3,50,25,0,245,263,3,52,26,0,246,247,3,56,28,
        0,247,248,5,54,0,0,248,263,1,0,0,0,249,250,3,58,29,0,250,251,5,54,
        0,0,251,263,1,0,0,0,252,253,3,60,30,0,253,254,5,54,0,0,254,263,1,
        0,0,0,255,256,3,66,33,0,256,257,5,54,0,0,257,263,1,0,0,0,258,259,
        3,68,34,0,259,260,5,54,0,0,260,263,1,0,0,0,261,263,5,54,0,0,262,
        239,1,0,0,0,262,240,1,0,0,0,262,243,1,0,0,0,262,244,1,0,0,0,262,
        245,1,0,0,0,262,246,1,0,0,0,262,249,1,0,0,0,262,252,1,0,0,0,262,
        255,1,0,0,0,262,258,1,0,0,0,262,261,1,0,0,0,263,43,1,0,0,0,264,265,
        5,9,0,0,265,266,5,48,0,0,266,267,3,68,34,0,267,268,5,49,0,0,268,
        272,3,40,20,0,269,271,3,46,23,0,270,269,1,0,0,0,271,274,1,0,0,0,
        272,270,1,0,0,0,272,273,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,
        275,277,3,48,24,0,276,275,1,0,0,0,276,277,1,0,0,0,277,45,1,0,0,0,
        278,279,5,10,0,0,279,280,5,9,0,0,280,281,5,48,0,0,281,282,3,68,34,
        0,282,283,5,49,0,0,283,284,3,40,20,0,284,47,1,0,0,0,285,286,5,10,
        0,0,286,287,3,40,20,0,287,49,1,0,0,0,288,289,5,11,0,0,289,290,5,
        48,0,0,290,291,3,68,34,0,291,292,5,49,0,0,292,293,3,40,20,0,293,
        51,1,0,0,0,294,295,5,12,0,0,295,297,5,48,0,0,296,298,3,54,27,0,297,
        296,1,0,0,0,297,298,1,0,0,0,298,299,1,0,0,0,299,301,5,54,0,0,300,
        302,3,68,34,0,301,300,1,0,0,0,301,302,1,0,0,0,302,303,1,0,0,0,303,
        305,5,54,0,0,304,306,3,68,34,0,305,304,1,0,0,0,305,306,1,0,0,0,306,
        307,1,0,0,0,307,308,5,49,0,0,308,309,3,40,20,0,309,53,1,0,0,0,310,
        313,3,4,2,0,311,313,3,68,34,0,312,310,1,0,0,0,312,311,1,0,0,0,313,
        55,1,0,0,0,314,315,5,13,0,0,315,57,1,0,0,0,316,318,5,14,0,0,317,
        319,3,68,34,0,318,317,1,0,0,0,318,319,1,0,0,0,319,59,1,0,0,0,320,
        321,5,18,0,0,321,323,5,48,0,0,322,324,3,62,31,0,323,322,1,0,0,0,
        323,324,1,0,0,0,324,325,1,0,0,0,325,326,5,49,0,0,326,61,1,0,0,0,
        327,332,3,64,32,0,328,329,5,55,0,0,329,331,3,64,32,0,330,328,1,0,
        0,0,331,334,1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,63,1,0,0,
        0,334,332,1,0,0,0,335,336,3,90,45,0,336,65,1,0,0,0,337,338,5,19,
        0,0,338,340,5,48,0,0,339,341,3,100,50,0,340,339,1,0,0,0,340,341,
        1,0,0,0,341,342,1,0,0,0,342,343,5,49,0,0,343,67,1,0,0,0,344,345,
        3,70,35,0,345,69,1,0,0,0,346,347,3,90,45,0,347,348,3,72,36,0,348,
        349,3,70,35,0,349,352,1,0,0,0,350,352,3,74,37,0,351,346,1,0,0,0,
        351,350,1,0,0,0,352,71,1,0,0,0,353,354,7,2,0,0,354,73,1,0,0,0,355,
        360,3,76,38,0,356,357,5,35,0,0,357,359,3,76,38,0,358,356,1,0,0,0,
        359,362,1,0,0,0,360,358,1,0,0,0,360,361,1,0,0,0,361,75,1,0,0,0,362,
        360,1,0,0,0,363,368,3,78,39,0,364,365,5,34,0,0,365,367,3,78,39,0,
        366,364,1,0,0,0,367,370,1,0,0,0,368,366,1,0,0,0,368,369,1,0,0,0,
        369,77,1,0,0,0,370,368,1,0,0,0,371,376,3,80,40,0,372,373,7,3,0,0,
        373,375,3,80,40,0,374,372,1,0,0,0,375,378,1,0,0,0,376,374,1,0,0,
        0,376,377,1,0,0,0,377,79,1,0,0,0,378,376,1,0,0,0,379,384,3,82,41,
        0,380,381,7,4,0,0,381,383,3,82,41,0,382,380,1,0,0,0,383,386,1,0,
        0,0,384,382,1,0,0,0,384,385,1,0,0,0,385,81,1,0,0,0,386,384,1,0,0,
        0,387,392,3,84,42,0,388,389,7,5,0,0,389,391,3,84,42,0,390,388,1,
        0,0,0,391,394,1,0,0,0,392,390,1,0,0,0,392,393,1,0,0,0,393,83,1,0,
        0,0,394,392,1,0,0,0,395,400,3,86,43,0,396,397,7,6,0,0,397,399,3,
        86,43,0,398,396,1,0,0,0,399,402,1,0,0,0,400,398,1,0,0,0,400,401,
        1,0,0,0,401,85,1,0,0,0,402,400,1,0,0,0,403,406,3,88,44,0,404,405,
        5,38,0,0,405,407,3,86,43,0,406,404,1,0,0,0,406,407,1,0,0,0,407,87,
        1,0,0,0,408,409,7,7,0,0,409,412,3,88,44,0,410,412,3,90,45,0,411,
        408,1,0,0,0,411,410,1,0,0,0,412,89,1,0,0,0,413,417,3,94,47,0,414,
        416,3,92,46,0,415,414,1,0,0,0,416,419,1,0,0,0,417,415,1,0,0,0,417,
        418,1,0,0,0,418,91,1,0,0,0,419,417,1,0,0,0,420,421,5,56,0,0,421,
        422,5,60,0,0,422,424,5,48,0,0,423,425,3,100,50,0,424,423,1,0,0,0,
        424,425,1,0,0,0,425,426,1,0,0,0,426,439,5,49,0,0,427,428,5,52,0,
        0,428,429,3,68,34,0,429,430,5,53,0,0,430,439,1,0,0,0,431,432,5,56,
        0,0,432,439,5,60,0,0,433,435,5,48,0,0,434,436,3,100,50,0,435,434,
        1,0,0,0,435,436,1,0,0,0,436,437,1,0,0,0,437,439,5,49,0,0,438,420,
        1,0,0,0,438,427,1,0,0,0,438,431,1,0,0,0,438,433,1,0,0,0,439,93,1,
        0,0,0,440,450,3,102,51,0,441,450,5,60,0,0,442,450,5,7,0,0,443,450,
        3,96,48,0,444,450,3,98,49,0,445,446,5,48,0,0,446,447,3,68,34,0,447,
        448,5,49,0,0,448,450,1,0,0,0,449,440,1,0,0,0,449,441,1,0,0,0,449,
        442,1,0,0,0,449,443,1,0,0,0,449,444,1,0,0,0,449,445,1,0,0,0,450,
        95,1,0,0,0,451,452,5,8,0,0,452,453,5,60,0,0,453,455,5,48,0,0,454,
        456,3,100,50,0,455,454,1,0,0,0,455,456,1,0,0,0,456,457,1,0,0,0,457,
        458,5,49,0,0,458,97,1,0,0,0,459,460,3,18,9,0,460,461,5,48,0,0,461,
        462,3,68,34,0,462,463,5,49,0,0,463,99,1,0,0,0,464,469,3,68,34,0,
        465,466,5,55,0,0,466,468,3,68,34,0,467,465,1,0,0,0,468,471,1,0,0,
        0,469,467,1,0,0,0,469,470,1,0,0,0,470,101,1,0,0,0,471,469,1,0,0,
        0,472,473,7,8,0,0,473,103,1,0,0,0,44,107,117,126,134,138,146,149,
        155,159,169,177,185,195,204,214,224,234,262,272,276,297,301,305,
        312,318,323,332,340,351,360,368,376,384,392,400,406,411,417,424,
        435,438,449,455,469
    ]

class JSSParser ( Parser ):

    grammarFileName = "JSSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'const'", "'function'", "'void'", 
                     "'class'", "'constructor'", "'this'", "'new'", "'if'", 
                     "'else'", "'while'", "'for'", "'break'", "'return'", 
                     "'true'", "'false'", "'null'", "'input'", "'console.log'", 
                     "'int'", "'real'", "'str'", "'bool'", "'**='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'=='", "'!='", "'>='", 
                     "'<='", "'&&'", "'||'", "'++'", "'--'", "'**'", "'='", 
                     "'>'", "'<'", "'!'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "LET", "CONST", "FUNCTION", "VOID", "CLASS", 
                      "CONSTRUCTOR", "THIS", "NEW", "IF", "ELSE", "WHILE", 
                      "FOR", "BREAK", "RETURN", "TRUE", "FALSE", "NULL", 
                      "INPUT", "CONSOLE_LOG", "INT_TYPE", "REAL_TYPE", "STR_TYPE", 
                      "BOOL_TYPE", "POW_ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                      "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "EQ_EQ", 
                      "NEQ", "GE", "LE", "AND", "OR", "INC", "DEC", "POW", 
                      "ASSIGN", "GT", "LT", "NOT", "PLUS", "MINUS", "MULT", 
                      "DIV", "MOD", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", "REAL_LITERAL", 
                      "INT_LITERAL", "STRING_LITERAL", "ID", "LINE_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_topLevelDeclaration = 1
    RULE_variableDeclaration = 2
    RULE_variableModifier = 3
    RULE_variableDeclarator = 4
    RULE_initializer = 5
    RULE_arrayLiteral = 6
    RULE_type = 7
    RULE_baseType = 8
    RULE_primitiveType = 9
    RULE_arraySuffix = 10
    RULE_returnType = 11
    RULE_classDeclaration = 12
    RULE_classMember = 13
    RULE_fieldDeclaration = 14
    RULE_constructorDeclaration = 15
    RULE_methodDeclaration = 16
    RULE_functionDeclaration = 17
    RULE_parameterList = 18
    RULE_parameter = 19
    RULE_block = 20
    RULE_statement = 21
    RULE_ifStatement = 22
    RULE_elseIfBlock = 23
    RULE_elseBlock = 24
    RULE_whileStatement = 25
    RULE_forStatement = 26
    RULE_forInit = 27
    RULE_breakStatement = 28
    RULE_returnStatement = 29
    RULE_inputStatement = 30
    RULE_inputArgumentList = 31
    RULE_inputArgument = 32
    RULE_consoleLogStatement = 33
    RULE_expression = 34
    RULE_assignmentExpression = 35
    RULE_assignmentOperator = 36
    RULE_logicalOrExpression = 37
    RULE_logicalAndExpression = 38
    RULE_equalityExpression = 39
    RULE_relationalExpression = 40
    RULE_additiveExpression = 41
    RULE_multiplicativeExpression = 42
    RULE_powerExpression = 43
    RULE_unaryExpression = 44
    RULE_postfixExpression = 45
    RULE_postfixSuffix = 46
    RULE_primaryExpression = 47
    RULE_newExpression = 48
    RULE_castExpression = 49
    RULE_argumentList = 50
    RULE_literal = 51

    ruleNames =  [ "program", "topLevelDeclaration", "variableDeclaration", 
                   "variableModifier", "variableDeclarator", "initializer", 
                   "arrayLiteral", "type", "baseType", "primitiveType", 
                   "arraySuffix", "returnType", "classDeclaration", "classMember", 
                   "fieldDeclaration", "constructorDeclaration", "methodDeclaration", 
                   "functionDeclaration", "parameterList", "parameter", 
                   "block", "statement", "ifStatement", "elseIfBlock", "elseBlock", 
                   "whileStatement", "forStatement", "forInit", "breakStatement", 
                   "returnStatement", "inputStatement", "inputArgumentList", 
                   "inputArgument", "consoleLogStatement", "expression", 
                   "assignmentExpression", "assignmentOperator", "logicalOrExpression", 
                   "logicalAndExpression", "equalityExpression", "relationalExpression", 
                   "additiveExpression", "multiplicativeExpression", "powerExpression", 
                   "unaryExpression", "postfixExpression", "postfixSuffix", 
                   "primaryExpression", "newExpression", "castExpression", 
                   "argumentList", "literal" ]

    EOF = Token.EOF
    LET=1
    CONST=2
    FUNCTION=3
    VOID=4
    CLASS=5
    CONSTRUCTOR=6
    THIS=7
    NEW=8
    IF=9
    ELSE=10
    WHILE=11
    FOR=12
    BREAK=13
    RETURN=14
    TRUE=15
    FALSE=16
    NULL=17
    INPUT=18
    CONSOLE_LOG=19
    INT_TYPE=20
    REAL_TYPE=21
    STR_TYPE=22
    BOOL_TYPE=23
    POW_ASSIGN=24
    PLUS_ASSIGN=25
    MINUS_ASSIGN=26
    MULT_ASSIGN=27
    DIV_ASSIGN=28
    MOD_ASSIGN=29
    EQ_EQ=30
    NEQ=31
    GE=32
    LE=33
    AND=34
    OR=35
    INC=36
    DEC=37
    POW=38
    ASSIGN=39
    GT=40
    LT=41
    NOT=42
    PLUS=43
    MINUS=44
    MULT=45
    DIV=46
    MOD=47
    LPAREN=48
    RPAREN=49
    LBRACE=50
    RBRACE=51
    LBRACK=52
    RBRACK=53
    SEMI=54
    COMMA=55
    DOT=56
    REAL_LITERAL=57
    INT_LITERAL=58
    STRING_LITERAL=59
    ID=60
    LINE_COMMENT=61
    WS=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(JSSParser.EOF, 0)

        def topLevelDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.TopLevelDeclarationContext)
            else:
                return self.getTypedRuleContext(JSSParser.TopLevelDeclarationContext,i)


        def getRuleIndex(self):
            return JSSParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = JSSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 46) != 0):
                self.state = 104
                self.topLevelDeclaration()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(JSSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(JSSParser.ClassDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(JSSParser.FunctionDeclarationContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(JSSParser.VariableDeclarationContext,0)


        def SEMI(self):
            return self.getToken(JSSParser.SEMI, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_topLevelDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelDeclaration" ):
                listener.enterTopLevelDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelDeclaration" ):
                listener.exitTopLevelDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelDeclaration" ):
                return visitor.visitTopLevelDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def topLevelDeclaration(self):

        localctx = JSSParser.TopLevelDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topLevelDeclaration)
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.classDeclaration()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.functionDeclaration()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.variableDeclaration()
                self.state = 115
                self.match(JSSParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableModifier(self):
            return self.getTypedRuleContext(JSSParser.VariableModifierContext,0)


        def type_(self):
            return self.getTypedRuleContext(JSSParser.TypeContext,0)


        def variableDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.VariableDeclaratorContext)
            else:
                return self.getTypedRuleContext(JSSParser.VariableDeclaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.COMMA)
            else:
                return self.getToken(JSSParser.COMMA, i)

        def getRuleIndex(self):
            return JSSParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = JSSParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.variableModifier()
            self.state = 120
            self.type_()
            self.state = 121
            self.variableDeclarator()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 122
                self.match(JSSParser.COMMA)
                self.state = 123
                self.variableDeclarator()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(JSSParser.LET, 0)

        def CONST(self):
            return self.getToken(JSSParser.CONST, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_variableModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableModifier" ):
                listener.enterVariableModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableModifier" ):
                listener.exitVariableModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableModifier" ):
                return visitor.visitVariableModifier(self)
            else:
                return visitor.visitChildren(self)




    def variableModifier(self):

        localctx = JSSParser.VariableModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(JSSParser.ASSIGN, 0)

        def initializer(self):
            return self.getTypedRuleContext(JSSParser.InitializerContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarator" ):
                return visitor.visitVariableDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarator(self):

        localctx = JSSParser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variableDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(JSSParser.ID)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 132
                self.match(JSSParser.ASSIGN)
                self.state = 133
                self.initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(JSSParser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer" ):
                listener.enterInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer" ):
                listener.exitInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer" ):
                return visitor.visitInitializer(self)
            else:
                return visitor.visitChildren(self)




    def initializer(self):

        localctx = JSSParser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_initializer)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 36, 37, 42, 43, 44, 48, 57, 58, 59, 60]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.expression()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.arrayLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(JSSParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(JSSParser.RBRACK, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JSSParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.COMMA)
            else:
                return self.getToken(JSSParser.COMMA, i)

        def getRuleIndex(self):
            return JSSParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = JSSParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(JSSParser.LBRACK)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162040288614515072) != 0):
                self.state = 141
                self.expression()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 142
                    self.match(JSSParser.COMMA)
                    self.state = 143
                    self.expression()
                    self.state = 148
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 151
            self.match(JSSParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(JSSParser.BaseTypeContext,0)


        def arraySuffix(self):
            return self.getTypedRuleContext(JSSParser.ArraySuffixContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = JSSParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.baseType()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 154
                self.arraySuffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(JSSParser.PrimitiveTypeContext,0)


        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_baseType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseType" ):
                listener.enterBaseType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseType" ):
                listener.exitBaseType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = JSSParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_baseType)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.primitiveType()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(JSSParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(JSSParser.INT_TYPE, 0)

        def REAL_TYPE(self):
            return self.getToken(JSSParser.REAL_TYPE, 0)

        def STR_TYPE(self):
            return self.getToken(JSSParser.STR_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(JSSParser.BOOL_TYPE, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = JSSParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraySuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(JSSParser.LBRACK, 0)

        def INT_LITERAL(self):
            return self.getToken(JSSParser.INT_LITERAL, 0)

        def RBRACK(self):
            return self.getToken(JSSParser.RBRACK, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_arraySuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraySuffix" ):
                listener.enterArraySuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraySuffix" ):
                listener.exitArraySuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraySuffix" ):
                return visitor.visitArraySuffix(self)
            else:
                return visitor.visitChildren(self)




    def arraySuffix(self):

        localctx = JSSParser.ArraySuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arraySuffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(JSSParser.LBRACK)
            self.state = 164
            self.match(JSSParser.INT_LITERAL)
            self.state = 165
            self.match(JSSParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(JSSParser.TypeContext,0)


        def VOID(self):
            return self.getToken(JSSParser.VOID, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_returnType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnType" ):
                listener.enterReturnType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnType" ):
                listener.exitReturnType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = JSSParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnType)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 60]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.type_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(JSSParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(JSSParser.CLASS, 0)

        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(JSSParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(JSSParser.RBRACE, 0)

        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(JSSParser.ClassMemberContext,i)


        def getRuleIndex(self):
            return JSSParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = JSSParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(JSSParser.CLASS)
            self.state = 172
            self.match(JSSParser.ID)
            self.state = 173
            self.match(JSSParser.LBRACE)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152921504622575632) != 0):
                self.state = 174
                self.classMember()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(JSSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDeclaration(self):
            return self.getTypedRuleContext(JSSParser.FieldDeclarationContext,0)


        def constructorDeclaration(self):
            return self.getTypedRuleContext(JSSParser.ConstructorDeclarationContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(JSSParser.MethodDeclarationContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_classMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassMember" ):
                listener.enterClassMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassMember" ):
                listener.exitClassMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMember" ):
                return visitor.visitClassMember(self)
            else:
                return visitor.visitChildren(self)




    def classMember(self):

        localctx = JSSParser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_classMember)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.fieldDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.constructorDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.methodDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(JSSParser.TypeContext,0)


        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def SEMI(self):
            return self.getToken(JSSParser.SEMI, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_fieldDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDeclaration" ):
                listener.enterFieldDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDeclaration" ):
                listener.exitFieldDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclaration" ):
                return visitor.visitFieldDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclaration(self):

        localctx = JSSParser.FieldDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fieldDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.type_()
            self.state = 188
            self.match(JSSParser.ID)
            self.state = 189
            self.match(JSSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def CONSTRUCTOR(self):
            return self.getToken(JSSParser.CONSTRUCTOR, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(JSSParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(JSSParser.ParameterListContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_constructorDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDeclaration" ):
                listener.enterConstructorDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDeclaration" ):
                listener.exitConstructorDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDeclaration" ):
                return visitor.visitConstructorDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constructorDeclaration(self):

        localctx = JSSParser.ConstructorDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constructorDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(JSSParser.ID)
            self.state = 192
            self.match(JSSParser.CONSTRUCTOR)
            self.state = 193
            self.match(JSSParser.LPAREN)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152921504622575616) != 0):
                self.state = 194
                self.parameterList()


            self.state = 197
            self.match(JSSParser.RPAREN)
            self.state = 198
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(JSSParser.ReturnTypeContext,0)


        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(JSSParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(JSSParser.ParameterListContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = JSSParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.returnType()
            self.state = 201
            self.match(JSSParser.ID)
            self.state = 202
            self.match(JSSParser.LPAREN)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152921504622575616) != 0):
                self.state = 203
                self.parameterList()


            self.state = 206
            self.match(JSSParser.RPAREN)
            self.state = 207
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(JSSParser.FUNCTION, 0)

        def returnType(self):
            return self.getTypedRuleContext(JSSParser.ReturnTypeContext,0)


        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(JSSParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(JSSParser.ParameterListContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = JSSParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(JSSParser.FUNCTION)
            self.state = 210
            self.returnType()
            self.state = 211
            self.match(JSSParser.ID)
            self.state = 212
            self.match(JSSParser.LPAREN)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152921504622575616) != 0):
                self.state = 213
                self.parameterList()


            self.state = 216
            self.match(JSSParser.RPAREN)
            self.state = 217
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.ParameterContext)
            else:
                return self.getTypedRuleContext(JSSParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.COMMA)
            else:
                return self.getToken(JSSParser.COMMA, i)

        def getRuleIndex(self):
            return JSSParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = JSSParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.parameter()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 220
                self.match(JSSParser.COMMA)
                self.state = 221
                self.parameter()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(JSSParser.TypeContext,0)


        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = JSSParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.type_()
            self.state = 228
            self.match(JSSParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(JSSParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(JSSParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.StatementContext)
            else:
                return self.getTypedRuleContext(JSSParser.StatementContext,i)


        def getRuleIndex(self):
            return JSSParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = JSSParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(JSSParser.LBRACE)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2181180587031657350) != 0):
                self.state = 231
                self.statement()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
            self.match(JSSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(JSSParser.BlockContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(JSSParser.VariableDeclarationContext,0)


        def SEMI(self):
            return self.getToken(JSSParser.SEMI, 0)

        def ifStatement(self):
            return self.getTypedRuleContext(JSSParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(JSSParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(JSSParser.ForStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(JSSParser.BreakStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(JSSParser.ReturnStatementContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(JSSParser.InputStatementContext,0)


        def consoleLogStatement(self):
            return self.getTypedRuleContext(JSSParser.ConsoleLogStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = JSSParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.block()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.variableDeclaration()
                self.state = 241
                self.match(JSSParser.SEMI)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.ifStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.whileStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 245
                self.forStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 246
                self.breakStatement()
                self.state = 247
                self.match(JSSParser.SEMI)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 249
                self.returnStatement()
                self.state = 250
                self.match(JSSParser.SEMI)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 252
                self.inputStatement()
                self.state = 253
                self.match(JSSParser.SEMI)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 9)
                self.state = 255
                self.consoleLogStatement()
                self.state = 256
                self.match(JSSParser.SEMI)
                pass
            elif token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 36, 37, 42, 43, 44, 48, 57, 58, 59, 60]:
                self.enterOuterAlt(localctx, 10)
                self.state = 258
                self.expression()
                self.state = 259
                self.match(JSSParser.SEMI)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 11)
                self.state = 261
                self.match(JSSParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(JSSParser.IF, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(JSSParser.BlockContext,0)


        def elseIfBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.ElseIfBlockContext)
            else:
                return self.getTypedRuleContext(JSSParser.ElseIfBlockContext,i)


        def elseBlock(self):
            return self.getTypedRuleContext(JSSParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = JSSParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(JSSParser.IF)
            self.state = 265
            self.match(JSSParser.LPAREN)
            self.state = 266
            self.expression()
            self.state = 267
            self.match(JSSParser.RPAREN)
            self.state = 268
            self.block()
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 269
                    self.elseIfBlock() 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 275
                self.elseBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(JSSParser.ELSE, 0)

        def IF(self):
            return self.getToken(JSSParser.IF, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(JSSParser.BlockContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_elseIfBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfBlock" ):
                listener.enterElseIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfBlock" ):
                listener.exitElseIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfBlock" ):
                return visitor.visitElseIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseIfBlock(self):

        localctx = JSSParser.ElseIfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elseIfBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(JSSParser.ELSE)
            self.state = 279
            self.match(JSSParser.IF)
            self.state = 280
            self.match(JSSParser.LPAREN)
            self.state = 281
            self.expression()
            self.state = 282
            self.match(JSSParser.RPAREN)
            self.state = 283
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(JSSParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(JSSParser.BlockContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = JSSParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(JSSParser.ELSE)
            self.state = 286
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(JSSParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(JSSParser.BlockContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = JSSParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(JSSParser.WHILE)
            self.state = 289
            self.match(JSSParser.LPAREN)
            self.state = 290
            self.expression()
            self.state = 291
            self.match(JSSParser.RPAREN)
            self.state = 292
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(JSSParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.SEMI)
            else:
                return self.getToken(JSSParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(JSSParser.BlockContext,0)


        def forInit(self):
            return self.getTypedRuleContext(JSSParser.ForInitContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JSSParser.ExpressionContext,i)


        def getRuleIndex(self):
            return JSSParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = JSSParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(JSSParser.FOR)
            self.state = 295
            self.match(JSSParser.LPAREN)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162040288614515078) != 0):
                self.state = 296
                self.forInit()


            self.state = 299
            self.match(JSSParser.SEMI)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162040288614515072) != 0):
                self.state = 300
                self.expression()


            self.state = 303
            self.match(JSSParser.SEMI)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162040288614515072) != 0):
                self.state = 304
                self.expression()


            self.state = 307
            self.match(JSSParser.RPAREN)
            self.state = 308
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(JSSParser.VariableDeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = JSSParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forInit)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.variableDeclaration()
                pass
            elif token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 36, 37, 42, 43, 44, 48, 57, 58, 59, 60]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(JSSParser.BREAK, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = JSSParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(JSSParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(JSSParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = JSSParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(JSSParser.RETURN)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162040288614515072) != 0):
                self.state = 317
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(JSSParser.INPUT, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def inputArgumentList(self):
            return self.getTypedRuleContext(JSSParser.InputArgumentListContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_inputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStatement" ):
                listener.enterInputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStatement" ):
                listener.exitInputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStatement" ):
                return visitor.visitInputStatement(self)
            else:
                return visitor.visitChildren(self)




    def inputStatement(self):

        localctx = JSSParser.InputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_inputStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(JSSParser.INPUT)
            self.state = 321
            self.match(JSSParser.LPAREN)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162009296130507136) != 0):
                self.state = 322
                self.inputArgumentList()


            self.state = 325
            self.match(JSSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inputArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.InputArgumentContext)
            else:
                return self.getTypedRuleContext(JSSParser.InputArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.COMMA)
            else:
                return self.getToken(JSSParser.COMMA, i)

        def getRuleIndex(self):
            return JSSParser.RULE_inputArgumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputArgumentList" ):
                listener.enterInputArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputArgumentList" ):
                listener.exitInputArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputArgumentList" ):
                return visitor.visitInputArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def inputArgumentList(self):

        localctx = JSSParser.InputArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_inputArgumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.inputArgument()
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 328
                self.match(JSSParser.COMMA)
                self.state = 329
                self.inputArgument()
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(JSSParser.PostfixExpressionContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_inputArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputArgument" ):
                listener.enterInputArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputArgument" ):
                listener.exitInputArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputArgument" ):
                return visitor.visitInputArgument(self)
            else:
                return visitor.visitChildren(self)




    def inputArgument(self):

        localctx = JSSParser.InputArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_inputArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.postfixExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConsoleLogStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSOLE_LOG(self):
            return self.getToken(JSSParser.CONSOLE_LOG, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(JSSParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_consoleLogStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsoleLogStatement" ):
                listener.enterConsoleLogStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsoleLogStatement" ):
                listener.exitConsoleLogStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsoleLogStatement" ):
                return visitor.visitConsoleLogStatement(self)
            else:
                return visitor.visitChildren(self)




    def consoleLogStatement(self):

        localctx = JSSParser.ConsoleLogStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_consoleLogStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(JSSParser.CONSOLE_LOG)
            self.state = 338
            self.match(JSSParser.LPAREN)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162040288614515072) != 0):
                self.state = 339
                self.argumentList()


            self.state = 342
            self.match(JSSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(JSSParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = JSSParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.assignmentExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(JSSParser.PostfixExpressionContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(JSSParser.AssignmentOperatorContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(JSSParser.AssignmentExpressionContext,0)


        def logicalOrExpression(self):
            return self.getTypedRuleContext(JSSParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_assignmentExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = JSSParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignmentExpression)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.postfixExpression()
                self.state = 347
                self.assignmentOperator()
                self.state = 348
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.logicalOrExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(JSSParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(JSSParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(JSSParser.MINUS_ASSIGN, 0)

        def MULT_ASSIGN(self):
            return self.getToken(JSSParser.MULT_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(JSSParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(JSSParser.MOD_ASSIGN, 0)

        def POW_ASSIGN(self):
            return self.getToken(JSSParser.POW_ASSIGN, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = JSSParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 550812778496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(JSSParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.OR)
            else:
                return self.getToken(JSSParser.OR, i)

        def getRuleIndex(self):
            return JSSParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = JSSParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.logicalAndExpression()
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 356
                self.match(JSSParser.OR)
                self.state = 357
                self.logicalAndExpression()
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(JSSParser.EqualityExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.AND)
            else:
                return self.getToken(JSSParser.AND, i)

        def getRuleIndex(self):
            return JSSParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = JSSParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.equalityExpression()
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 364
                self.match(JSSParser.AND)
                self.state = 365
                self.equalityExpression()
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(JSSParser.RelationalExpressionContext,i)


        def EQ_EQ(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.EQ_EQ)
            else:
                return self.getToken(JSSParser.EQ_EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.NEQ)
            else:
                return self.getToken(JSSParser.NEQ, i)

        def getRuleIndex(self):
            return JSSParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = JSSParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.relationalExpression()
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 372
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 373
                self.relationalExpression()
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(JSSParser.AdditiveExpressionContext,i)


        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.GT)
            else:
                return self.getToken(JSSParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.GE)
            else:
                return self.getToken(JSSParser.GE, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.LT)
            else:
                return self.getToken(JSSParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.LE)
            else:
                return self.getToken(JSSParser.LE, i)

        def getRuleIndex(self):
            return JSSParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = JSSParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.additiveExpression()
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3311419785216) != 0):
                self.state = 380
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3311419785216) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 381
                self.additiveExpression()
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(JSSParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.PLUS)
            else:
                return self.getToken(JSSParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.MINUS)
            else:
                return self.getToken(JSSParser.MINUS, i)

        def getRuleIndex(self):
            return JSSParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = JSSParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.multiplicativeExpression()
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43 or _la==44:
                self.state = 388
                _la = self._input.LA(1)
                if not(_la==43 or _la==44):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 389
                self.multiplicativeExpression()
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def powerExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.PowerExpressionContext)
            else:
                return self.getTypedRuleContext(JSSParser.PowerExpressionContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.MULT)
            else:
                return self.getToken(JSSParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.DIV)
            else:
                return self.getToken(JSSParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.MOD)
            else:
                return self.getToken(JSSParser.MOD, i)

        def getRuleIndex(self):
            return JSSParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = JSSParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.powerExpression()
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 246290604621824) != 0):
                self.state = 396
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 246290604621824) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 397
                self.powerExpression()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(JSSParser.UnaryExpressionContext,0)


        def POW(self):
            return self.getToken(JSSParser.POW, 0)

        def powerExpression(self):
            return self.getTypedRuleContext(JSSParser.PowerExpressionContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_powerExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpression" ):
                listener.enterPowerExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpression" ):
                listener.exitPowerExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpression" ):
                return visitor.visitPowerExpression(self)
            else:
                return visitor.visitChildren(self)




    def powerExpression(self):

        localctx = JSSParser.PowerExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_powerExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.unaryExpression()
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 404
                self.match(JSSParser.POW)
                self.state = 405
                self.powerExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(JSSParser.UnaryExpressionContext,0)


        def NOT(self):
            return self.getToken(JSSParser.NOT, 0)

        def PLUS(self):
            return self.getToken(JSSParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(JSSParser.MINUS, 0)

        def INC(self):
            return self.getToken(JSSParser.INC, 0)

        def DEC(self):
            return self.getToken(JSSParser.DEC, 0)

        def postfixExpression(self):
            return self.getTypedRuleContext(JSSParser.PostfixExpressionContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = JSSParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37, 42, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30992484007936) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 409
                self.unaryExpression()
                pass
            elif token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 48, 57, 58, 59, 60]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.postfixExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(JSSParser.PrimaryExpressionContext,0)


        def postfixSuffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.PostfixSuffixContext)
            else:
                return self.getTypedRuleContext(JSSParser.PostfixSuffixContext,i)


        def getRuleIndex(self):
            return JSSParser.RULE_postfixExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixExpression" ):
                listener.enterPostfixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixExpression" ):
                listener.exitPostfixExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExpression" ):
                return visitor.visitPostfixExpression(self)
            else:
                return visitor.visitChildren(self)




    def postfixExpression(self):

        localctx = JSSParser.PostfixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_postfixExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.primaryExpression()
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 76842668642009088) != 0):
                self.state = 414
                self.postfixSuffix()
                self.state = 419
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(JSSParser.DOT, 0)

        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(JSSParser.ArgumentListContext,0)


        def LBRACK(self):
            return self.getToken(JSSParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(JSSParser.RBRACK, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_postfixSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixSuffix" ):
                listener.enterPostfixSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixSuffix" ):
                listener.exitPostfixSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixSuffix" ):
                return visitor.visitPostfixSuffix(self)
            else:
                return visitor.visitChildren(self)




    def postfixSuffix(self):

        localctx = JSSParser.PostfixSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_postfixSuffix)
        self._la = 0 # Token type
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(JSSParser.DOT)
                self.state = 421
                self.match(JSSParser.ID)
                self.state = 422
                self.match(JSSParser.LPAREN)
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162040288614515072) != 0):
                    self.state = 423
                    self.argumentList()


                self.state = 426
                self.match(JSSParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(JSSParser.LBRACK)
                self.state = 428
                self.expression()
                self.state = 429
                self.match(JSSParser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.match(JSSParser.DOT)
                self.state = 432
                self.match(JSSParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 433
                self.match(JSSParser.LPAREN)
                self.state = 435
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162040288614515072) != 0):
                    self.state = 434
                    self.argumentList()


                self.state = 437
                self.match(JSSParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(JSSParser.LiteralContext,0)


        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def THIS(self):
            return self.getToken(JSSParser.THIS, 0)

        def newExpression(self):
            return self.getTypedRuleContext(JSSParser.NewExpressionContext,0)


        def castExpression(self):
            return self.getTypedRuleContext(JSSParser.CastExpressionContext,0)


        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = JSSParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_primaryExpression)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.literal()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.match(JSSParser.ID)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.match(JSSParser.THIS)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 443
                self.newExpression()
                pass
            elif token in [20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 444
                self.castExpression()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 6)
                self.state = 445
                self.match(JSSParser.LPAREN)
                self.state = 446
                self.expression()
                self.state = 447
                self.match(JSSParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(JSSParser.NEW, 0)

        def ID(self):
            return self.getToken(JSSParser.ID, 0)

        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(JSSParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_newExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewExpression" ):
                listener.enterNewExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewExpression" ):
                listener.exitNewExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewExpression" ):
                return visitor.visitNewExpression(self)
            else:
                return visitor.visitChildren(self)




    def newExpression(self):

        localctx = JSSParser.NewExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_newExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(JSSParser.NEW)
            self.state = 452
            self.match(JSSParser.ID)
            self.state = 453
            self.match(JSSParser.LPAREN)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2162040288614515072) != 0):
                self.state = 454
                self.argumentList()


            self.state = 457
            self.match(JSSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(JSSParser.PrimitiveTypeContext,0)


        def LPAREN(self):
            return self.getToken(JSSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(JSSParser.RPAREN, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_castExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpression" ):
                listener.enterCastExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpression" ):
                listener.exitCastExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpression" ):
                return visitor.visitCastExpression(self)
            else:
                return visitor.visitChildren(self)




    def castExpression(self):

        localctx = JSSParser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_castExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.primitiveType()
            self.state = 460
            self.match(JSSParser.LPAREN)
            self.state = 461
            self.expression()
            self.state = 462
            self.match(JSSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JSSParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.COMMA)
            else:
                return self.getToken(JSSParser.COMMA, i)

        def getRuleIndex(self):
            return JSSParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = JSSParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.expression()
            self.state = 469
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 465
                self.match(JSSParser.COMMA)
                self.state = 466
                self.expression()
                self.state = 471
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(JSSParser.INT_LITERAL, 0)

        def REAL_LITERAL(self):
            return self.getToken(JSSParser.REAL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(JSSParser.STRING_LITERAL, 0)

        def TRUE(self):
            return self.getToken(JSSParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(JSSParser.FALSE, 0)

        def NULL(self):
            return self.getToken(JSSParser.NULL, 0)

        def getRuleIndex(self):
            return JSSParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = JSSParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1008806316531220480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





