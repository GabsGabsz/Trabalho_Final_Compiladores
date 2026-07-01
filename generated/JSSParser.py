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
        4,1,64,496,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,1,0,5,0,112,8,0,10,0,12,0,115,9,0,1,0,1,0,1,
        1,1,1,1,1,3,1,122,8,1,1,2,1,2,1,2,1,2,1,2,5,2,129,8,2,10,2,12,2,
        132,9,2,1,3,1,3,1,4,1,4,1,4,3,4,139,8,4,1,5,1,5,3,5,143,8,5,1,6,
        1,6,1,6,1,6,5,6,149,8,6,10,6,12,6,152,9,6,3,6,154,8,6,1,6,1,6,1,
        7,1,7,3,7,160,8,7,1,8,1,8,3,8,164,8,8,1,9,1,9,1,10,1,10,1,10,4,10,
        171,8,10,11,10,12,10,172,1,11,1,11,3,11,177,8,11,1,12,1,12,1,12,
        1,12,5,12,183,8,12,10,12,12,12,186,9,12,1,12,1,12,1,13,1,13,1,13,
        3,13,193,8,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,203,8,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,212,8,16,1,16,1,16,1,
        16,1,17,1,17,1,17,1,17,1,17,3,17,222,8,17,1,17,1,17,1,17,1,18,1,
        18,1,18,5,18,230,8,18,10,18,12,18,233,9,18,1,19,1,19,1,19,1,20,1,
        20,5,20,240,8,20,10,20,12,20,243,9,20,1,20,1,20,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,270,8,21,1,22,1,22,1,22,1,
        22,1,22,1,22,5,22,278,8,22,10,22,12,22,281,9,22,1,22,3,22,284,8,
        22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,1,
        25,1,25,1,25,1,25,1,26,1,26,1,26,3,26,305,8,26,1,26,1,26,3,26,309,
        8,26,1,26,1,26,3,26,313,8,26,1,26,1,26,1,26,1,27,1,27,3,27,320,8,
        27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,5,30,329,8,30,10,30,12,30,
        332,9,30,1,31,1,31,1,32,1,32,3,32,338,8,32,1,33,1,33,1,33,3,33,343,
        8,33,1,33,1,33,1,34,1,34,1,34,5,34,350,8,34,10,34,12,34,353,9,34,
        1,35,1,35,1,36,1,36,1,36,3,36,360,8,36,1,36,1,36,1,37,1,37,1,38,
        1,38,1,38,1,38,1,38,3,38,371,8,38,1,39,1,39,1,40,1,40,1,40,5,40,
        378,8,40,10,40,12,40,381,9,40,1,41,1,41,1,41,5,41,386,8,41,10,41,
        12,41,389,9,41,1,42,1,42,1,42,5,42,394,8,42,10,42,12,42,397,9,42,
        1,43,1,43,1,43,5,43,402,8,43,10,43,12,43,405,9,43,1,44,1,44,1,44,
        5,44,410,8,44,10,44,12,44,413,9,44,1,45,1,45,1,45,5,45,418,8,45,
        10,45,12,45,421,9,45,1,46,1,46,1,46,3,46,426,8,46,1,47,1,47,1,47,
        3,47,431,8,47,1,48,1,48,5,48,435,8,48,10,48,12,48,438,9,48,1,49,
        1,49,1,49,1,49,3,49,444,8,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,
        1,49,1,49,3,49,455,8,49,1,49,1,49,1,49,3,49,460,8,49,1,50,1,50,1,
        50,1,50,1,50,1,50,1,50,1,50,1,50,3,50,471,8,50,1,51,1,51,1,51,1,
        51,3,51,477,8,51,1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,
        53,5,53,489,8,53,10,53,12,53,492,9,53,1,54,1,54,1,54,0,0,55,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,
        94,96,98,100,102,104,106,108,0,9,1,0,1,2,1,0,20,23,2,0,24,31,41,
        41,1,0,32,33,2,0,34,35,42,43,1,0,45,46,1,0,47,49,2,0,38,39,44,46,
        2,0,15,17,59,61,505,0,113,1,0,0,0,2,121,1,0,0,0,4,123,1,0,0,0,6,
        133,1,0,0,0,8,135,1,0,0,0,10,142,1,0,0,0,12,144,1,0,0,0,14,157,1,
        0,0,0,16,163,1,0,0,0,18,165,1,0,0,0,20,170,1,0,0,0,22,176,1,0,0,
        0,24,178,1,0,0,0,26,192,1,0,0,0,28,194,1,0,0,0,30,198,1,0,0,0,32,
        207,1,0,0,0,34,216,1,0,0,0,36,226,1,0,0,0,38,234,1,0,0,0,40,237,
        1,0,0,0,42,269,1,0,0,0,44,271,1,0,0,0,46,285,1,0,0,0,48,292,1,0,
        0,0,50,295,1,0,0,0,52,301,1,0,0,0,54,319,1,0,0,0,56,321,1,0,0,0,
        58,323,1,0,0,0,60,325,1,0,0,0,62,333,1,0,0,0,64,335,1,0,0,0,66,339,
        1,0,0,0,68,346,1,0,0,0,70,354,1,0,0,0,72,356,1,0,0,0,74,363,1,0,
        0,0,76,370,1,0,0,0,78,372,1,0,0,0,80,374,1,0,0,0,82,382,1,0,0,0,
        84,390,1,0,0,0,86,398,1,0,0,0,88,406,1,0,0,0,90,414,1,0,0,0,92,422,
        1,0,0,0,94,430,1,0,0,0,96,432,1,0,0,0,98,459,1,0,0,0,100,470,1,0,
        0,0,102,472,1,0,0,0,104,480,1,0,0,0,106,485,1,0,0,0,108,493,1,0,
        0,0,110,112,3,2,1,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,0,
        0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,113,1,0,0,0,116,117,5,0,
        0,1,117,1,1,0,0,0,118,122,3,24,12,0,119,122,3,34,17,0,120,122,3,
        42,21,0,121,118,1,0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,3,1,
        0,0,0,123,124,3,6,3,0,124,125,3,14,7,0,125,130,3,8,4,0,126,127,5,
        57,0,0,127,129,3,8,4,0,128,126,1,0,0,0,129,132,1,0,0,0,130,128,1,
        0,0,0,130,131,1,0,0,0,131,5,1,0,0,0,132,130,1,0,0,0,133,134,7,0,
        0,0,134,7,1,0,0,0,135,138,5,62,0,0,136,137,5,41,0,0,137,139,3,10,
        5,0,138,136,1,0,0,0,138,139,1,0,0,0,139,9,1,0,0,0,140,143,3,74,37,
        0,141,143,3,12,6,0,142,140,1,0,0,0,142,141,1,0,0,0,143,11,1,0,0,
        0,144,153,5,54,0,0,145,150,3,74,37,0,146,147,5,57,0,0,147,149,3,
        74,37,0,148,146,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,
        1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,153,145,1,0,0,0,153,154,
        1,0,0,0,154,155,1,0,0,0,155,156,5,55,0,0,156,13,1,0,0,0,157,159,
        3,16,8,0,158,160,3,20,10,0,159,158,1,0,0,0,159,160,1,0,0,0,160,15,
        1,0,0,0,161,164,3,18,9,0,162,164,5,62,0,0,163,161,1,0,0,0,163,162,
        1,0,0,0,164,17,1,0,0,0,165,166,7,1,0,0,166,19,1,0,0,0,167,168,5,
        54,0,0,168,169,5,60,0,0,169,171,5,55,0,0,170,167,1,0,0,0,171,172,
        1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,21,1,0,0,0,174,177,3,
        14,7,0,175,177,5,4,0,0,176,174,1,0,0,0,176,175,1,0,0,0,177,23,1,
        0,0,0,178,179,5,5,0,0,179,180,5,62,0,0,180,184,5,52,0,0,181,183,
        3,26,13,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,
        1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,188,5,53,0,0,188,25,
        1,0,0,0,189,193,3,28,14,0,190,193,3,30,15,0,191,193,3,32,16,0,192,
        189,1,0,0,0,192,190,1,0,0,0,192,191,1,0,0,0,193,27,1,0,0,0,194,195,
        3,14,7,0,195,196,5,62,0,0,196,197,5,56,0,0,197,29,1,0,0,0,198,199,
        5,62,0,0,199,200,5,6,0,0,200,202,5,50,0,0,201,203,3,36,18,0,202,
        201,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,205,5,51,0,0,205,
        206,3,40,20,0,206,31,1,0,0,0,207,208,3,22,11,0,208,209,5,62,0,0,
        209,211,5,50,0,0,210,212,3,36,18,0,211,210,1,0,0,0,211,212,1,0,0,
        0,212,213,1,0,0,0,213,214,5,51,0,0,214,215,3,40,20,0,215,33,1,0,
        0,0,216,217,5,3,0,0,217,218,3,22,11,0,218,219,5,62,0,0,219,221,5,
        50,0,0,220,222,3,36,18,0,221,220,1,0,0,0,221,222,1,0,0,0,222,223,
        1,0,0,0,223,224,5,51,0,0,224,225,3,40,20,0,225,35,1,0,0,0,226,231,
        3,38,19,0,227,228,5,57,0,0,228,230,3,38,19,0,229,227,1,0,0,0,230,
        233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,37,1,0,0,0,233,231,
        1,0,0,0,234,235,3,14,7,0,235,236,5,62,0,0,236,39,1,0,0,0,237,241,
        5,52,0,0,238,240,3,42,21,0,239,238,1,0,0,0,240,243,1,0,0,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,244,1,0,0,0,243,241,1,0,0,0,244,245,
        5,53,0,0,245,41,1,0,0,0,246,270,3,40,20,0,247,248,3,4,2,0,248,249,
        5,56,0,0,249,270,1,0,0,0,250,270,3,44,22,0,251,270,3,50,25,0,252,
        270,3,52,26,0,253,254,3,62,31,0,254,255,5,56,0,0,255,270,1,0,0,0,
        256,257,3,64,32,0,257,258,5,56,0,0,258,270,1,0,0,0,259,260,3,66,
        33,0,260,261,5,56,0,0,261,270,1,0,0,0,262,263,3,72,36,0,263,264,
        5,56,0,0,264,270,1,0,0,0,265,266,3,74,37,0,266,267,5,56,0,0,267,
        270,1,0,0,0,268,270,5,56,0,0,269,246,1,0,0,0,269,247,1,0,0,0,269,
        250,1,0,0,0,269,251,1,0,0,0,269,252,1,0,0,0,269,253,1,0,0,0,269,
        256,1,0,0,0,269,259,1,0,0,0,269,262,1,0,0,0,269,265,1,0,0,0,269,
        268,1,0,0,0,270,43,1,0,0,0,271,272,5,9,0,0,272,273,5,50,0,0,273,
        274,3,74,37,0,274,275,5,51,0,0,275,279,3,40,20,0,276,278,3,46,23,
        0,277,276,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,
        0,280,283,1,0,0,0,281,279,1,0,0,0,282,284,3,48,24,0,283,282,1,0,
        0,0,283,284,1,0,0,0,284,45,1,0,0,0,285,286,5,10,0,0,286,287,5,9,
        0,0,287,288,5,50,0,0,288,289,3,74,37,0,289,290,5,51,0,0,290,291,
        3,40,20,0,291,47,1,0,0,0,292,293,5,10,0,0,293,294,3,40,20,0,294,
        49,1,0,0,0,295,296,5,11,0,0,296,297,5,50,0,0,297,298,3,74,37,0,298,
        299,5,51,0,0,299,300,3,40,20,0,300,51,1,0,0,0,301,302,5,12,0,0,302,
        304,5,50,0,0,303,305,3,54,27,0,304,303,1,0,0,0,304,305,1,0,0,0,305,
        306,1,0,0,0,306,308,5,56,0,0,307,309,3,56,28,0,308,307,1,0,0,0,308,
        309,1,0,0,0,309,310,1,0,0,0,310,312,5,56,0,0,311,313,3,58,29,0,312,
        311,1,0,0,0,312,313,1,0,0,0,313,314,1,0,0,0,314,315,5,51,0,0,315,
        316,3,40,20,0,316,53,1,0,0,0,317,320,3,4,2,0,318,320,3,60,30,0,319,
        317,1,0,0,0,319,318,1,0,0,0,320,55,1,0,0,0,321,322,3,74,37,0,322,
        57,1,0,0,0,323,324,3,60,30,0,324,59,1,0,0,0,325,330,3,74,37,0,326,
        327,5,57,0,0,327,329,3,74,37,0,328,326,1,0,0,0,329,332,1,0,0,0,330,
        328,1,0,0,0,330,331,1,0,0,0,331,61,1,0,0,0,332,330,1,0,0,0,333,334,
        5,13,0,0,334,63,1,0,0,0,335,337,5,14,0,0,336,338,3,74,37,0,337,336,
        1,0,0,0,337,338,1,0,0,0,338,65,1,0,0,0,339,340,5,18,0,0,340,342,
        5,50,0,0,341,343,3,68,34,0,342,341,1,0,0,0,342,343,1,0,0,0,343,344,
        1,0,0,0,344,345,5,51,0,0,345,67,1,0,0,0,346,351,3,70,35,0,347,348,
        5,57,0,0,348,350,3,70,35,0,349,347,1,0,0,0,350,353,1,0,0,0,351,349,
        1,0,0,0,351,352,1,0,0,0,352,69,1,0,0,0,353,351,1,0,0,0,354,355,3,
        96,48,0,355,71,1,0,0,0,356,357,5,19,0,0,357,359,5,50,0,0,358,360,
        3,106,53,0,359,358,1,0,0,0,359,360,1,0,0,0,360,361,1,0,0,0,361,362,
        5,51,0,0,362,73,1,0,0,0,363,364,3,76,38,0,364,75,1,0,0,0,365,366,
        3,96,48,0,366,367,3,78,39,0,367,368,3,76,38,0,368,371,1,0,0,0,369,
        371,3,80,40,0,370,365,1,0,0,0,370,369,1,0,0,0,371,77,1,0,0,0,372,
        373,7,2,0,0,373,79,1,0,0,0,374,379,3,82,41,0,375,376,5,37,0,0,376,
        378,3,82,41,0,377,375,1,0,0,0,378,381,1,0,0,0,379,377,1,0,0,0,379,
        380,1,0,0,0,380,81,1,0,0,0,381,379,1,0,0,0,382,387,3,84,42,0,383,
        384,5,36,0,0,384,386,3,84,42,0,385,383,1,0,0,0,386,389,1,0,0,0,387,
        385,1,0,0,0,387,388,1,0,0,0,388,83,1,0,0,0,389,387,1,0,0,0,390,395,
        3,86,43,0,391,392,7,3,0,0,392,394,3,86,43,0,393,391,1,0,0,0,394,
        397,1,0,0,0,395,393,1,0,0,0,395,396,1,0,0,0,396,85,1,0,0,0,397,395,
        1,0,0,0,398,403,3,88,44,0,399,400,7,4,0,0,400,402,3,88,44,0,401,
        399,1,0,0,0,402,405,1,0,0,0,403,401,1,0,0,0,403,404,1,0,0,0,404,
        87,1,0,0,0,405,403,1,0,0,0,406,411,3,90,45,0,407,408,7,5,0,0,408,
        410,3,90,45,0,409,407,1,0,0,0,410,413,1,0,0,0,411,409,1,0,0,0,411,
        412,1,0,0,0,412,89,1,0,0,0,413,411,1,0,0,0,414,419,3,92,46,0,415,
        416,7,6,0,0,416,418,3,92,46,0,417,415,1,0,0,0,418,421,1,0,0,0,419,
        417,1,0,0,0,419,420,1,0,0,0,420,91,1,0,0,0,421,419,1,0,0,0,422,425,
        3,94,47,0,423,424,5,40,0,0,424,426,3,92,46,0,425,423,1,0,0,0,425,
        426,1,0,0,0,426,93,1,0,0,0,427,428,7,7,0,0,428,431,3,94,47,0,429,
        431,3,96,48,0,430,427,1,0,0,0,430,429,1,0,0,0,431,95,1,0,0,0,432,
        436,3,100,50,0,433,435,3,98,49,0,434,433,1,0,0,0,435,438,1,0,0,0,
        436,434,1,0,0,0,436,437,1,0,0,0,437,97,1,0,0,0,438,436,1,0,0,0,439,
        440,5,58,0,0,440,441,5,62,0,0,441,443,5,50,0,0,442,444,3,106,53,
        0,443,442,1,0,0,0,443,444,1,0,0,0,444,445,1,0,0,0,445,460,5,51,0,
        0,446,447,5,54,0,0,447,448,3,74,37,0,448,449,5,55,0,0,449,460,1,
        0,0,0,450,451,5,58,0,0,451,460,5,62,0,0,452,454,5,50,0,0,453,455,
        3,106,53,0,454,453,1,0,0,0,454,455,1,0,0,0,455,456,1,0,0,0,456,460,
        5,51,0,0,457,460,5,38,0,0,458,460,5,39,0,0,459,439,1,0,0,0,459,446,
        1,0,0,0,459,450,1,0,0,0,459,452,1,0,0,0,459,457,1,0,0,0,459,458,
        1,0,0,0,460,99,1,0,0,0,461,471,3,108,54,0,462,471,5,62,0,0,463,471,
        5,7,0,0,464,471,3,102,51,0,465,471,3,104,52,0,466,467,5,50,0,0,467,
        468,3,74,37,0,468,469,5,51,0,0,469,471,1,0,0,0,470,461,1,0,0,0,470,
        462,1,0,0,0,470,463,1,0,0,0,470,464,1,0,0,0,470,465,1,0,0,0,470,
        466,1,0,0,0,471,101,1,0,0,0,472,473,5,8,0,0,473,474,5,62,0,0,474,
        476,5,50,0,0,475,477,3,106,53,0,476,475,1,0,0,0,476,477,1,0,0,0,
        477,478,1,0,0,0,478,479,5,51,0,0,479,103,1,0,0,0,480,481,3,18,9,
        0,481,482,5,50,0,0,482,483,3,74,37,0,483,484,5,51,0,0,484,105,1,
        0,0,0,485,490,3,74,37,0,486,487,5,57,0,0,487,489,3,74,37,0,488,486,
        1,0,0,0,489,492,1,0,0,0,490,488,1,0,0,0,490,491,1,0,0,0,491,107,
        1,0,0,0,492,490,1,0,0,0,493,494,7,8,0,0,494,109,1,0,0,0,46,113,121,
        130,138,142,150,153,159,163,172,176,184,192,202,211,221,231,241,
        269,279,283,304,308,312,319,330,337,342,351,359,370,379,387,395,
        403,411,419,425,430,436,443,454,459,470,476,490
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
                     "'int'", "'real'", "'str'", "'bool'", "'**='", "'&&='", 
                     "'||='", "'+='", "'-='", "'*='", "'/='", "'%='", "'=='", 
                     "'!='", "'>='", "'<='", "'&&'", "'||'", "'++'", "'--'", 
                     "'**'", "'='", "'>'", "'<'", "'!'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "LET", "CONST", "FUNCTION", "VOID", "CLASS", 
                      "CONSTRUCTOR", "THIS", "NEW", "IF", "ELSE", "WHILE", 
                      "FOR", "BREAK", "RETURN", "TRUE", "FALSE", "NULL", 
                      "INPUT", "CONSOLE_LOG", "INT_TYPE", "REAL_TYPE", "STR_TYPE", 
                      "BOOL_TYPE", "POW_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", 
                      "PLUS_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "EQ_EQ", "NEQ", "GE", "LE", "AND", "OR", 
                      "INC", "DEC", "POW", "ASSIGN", "GT", "LT", "NOT", 
                      "PLUS", "MINUS", "MULT", "DIV", "MOD", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", 
                      "DOT", "REAL_LITERAL", "INT_LITERAL", "STRING_LITERAL", 
                      "ID", "LINE_COMMENT", "WS" ]

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
    RULE_forCondition = 28
    RULE_forUpdate = 29
    RULE_expressionList = 30
    RULE_breakStatement = 31
    RULE_returnStatement = 32
    RULE_inputStatement = 33
    RULE_inputArgumentList = 34
    RULE_inputArgument = 35
    RULE_consoleLogStatement = 36
    RULE_expression = 37
    RULE_assignmentExpression = 38
    RULE_assignmentOperator = 39
    RULE_logicalOrExpression = 40
    RULE_logicalAndExpression = 41
    RULE_equalityExpression = 42
    RULE_relationalExpression = 43
    RULE_additiveExpression = 44
    RULE_multiplicativeExpression = 45
    RULE_powerExpression = 46
    RULE_unaryExpression = 47
    RULE_postfixExpression = 48
    RULE_postfixSuffix = 49
    RULE_primaryExpression = 50
    RULE_newExpression = 51
    RULE_castExpression = 52
    RULE_argumentList = 53
    RULE_literal = 54

    ruleNames =  [ "program", "topLevelDeclaration", "variableDeclaration", 
                   "variableModifier", "variableDeclarator", "initializer", 
                   "arrayLiteral", "type", "baseType", "primitiveType", 
                   "arraySuffix", "returnType", "classDeclaration", "classMember", 
                   "fieldDeclaration", "constructorDeclaration", "methodDeclaration", 
                   "functionDeclaration", "parameterList", "parameter", 
                   "block", "statement", "ifStatement", "elseIfBlock", "elseBlock", 
                   "whileStatement", "forStatement", "forInit", "forCondition", 
                   "forUpdate", "expressionList", "breakStatement", "returnStatement", 
                   "inputStatement", "inputArgumentList", "inputArgument", 
                   "consoleLogStatement", "expression", "assignmentExpression", 
                   "assignmentOperator", "logicalOrExpression", "logicalAndExpression", 
                   "equalityExpression", "relationalExpression", "additiveExpression", 
                   "multiplicativeExpression", "powerExpression", "unaryExpression", 
                   "postfixExpression", "postfixSuffix", "primaryExpression", 
                   "newExpression", "castExpression", "argumentList", "literal" ]

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
    AND_ASSIGN=25
    OR_ASSIGN=26
    PLUS_ASSIGN=27
    MINUS_ASSIGN=28
    MULT_ASSIGN=29
    DIV_ASSIGN=30
    MOD_ASSIGN=31
    EQ_EQ=32
    NEQ=33
    GE=34
    LE=35
    AND=36
    OR=37
    INC=38
    DEC=39
    POW=40
    ASSIGN=41
    GT=42
    LT=43
    NOT=44
    PLUS=45
    MINUS=46
    MULT=47
    DIV=48
    MOD=49
    LPAREN=50
    RPAREN=51
    LBRACE=52
    RBRACE=53
    LBRACK=54
    RBRACK=55
    SEMI=56
    COMMA=57
    DOT=58
    REAL_LITERAL=59
    INT_LITERAL=60
    STRING_LITERAL=61
    ID=62
    LINE_COMMENT=63
    WS=64

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
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8724722348076301230) != 0):
                self.state = 110
                self.topLevelDeclaration()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
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


        def statement(self):
            return self.getTypedRuleContext(JSSParser.StatementContext,0)


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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.classDeclaration()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.functionDeclaration()
                pass
            elif token in [1, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 38, 39, 44, 45, 46, 50, 52, 56, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.statement()
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
            self.state = 123
            self.variableModifier()
            self.state = 124
            self.type_()
            self.state = 125
            self.variableDeclarator()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 126
                self.match(JSSParser.COMMA)
                self.state = 127
                self.variableDeclarator()
                self.state = 132
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
            self.state = 133
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
            self.state = 135
            self.match(JSSParser.ID)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 136
                self.match(JSSParser.ASSIGN)
                self.state = 137
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
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 38, 39, 44, 45, 46, 50, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.expression()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
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
            self.state = 144
            self.match(JSSParser.LBRACK)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 145
                self.expression()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==57:
                    self.state = 146
                    self.match(JSSParser.COMMA)
                    self.state = 147
                    self.expression()
                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 155
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
            self.state = 157
            self.baseType()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 158
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
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.primitiveType()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
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
            self.state = 165
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

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.LBRACK)
            else:
                return self.getToken(JSSParser.LBRACK, i)

        def INT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.INT_LITERAL)
            else:
                return self.getToken(JSSParser.INT_LITERAL, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(JSSParser.RBRACK)
            else:
                return self.getToken(JSSParser.RBRACK, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 167
                self.match(JSSParser.LBRACK)
                self.state = 168
                self.match(JSSParser.INT_LITERAL)
                self.state = 169
                self.match(JSSParser.RBRACK)
                self.state = 172 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==54):
                    break

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
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.type_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
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
            self.state = 178
            self.match(JSSParser.CLASS)
            self.state = 179
            self.match(JSSParser.ID)
            self.state = 180
            self.match(JSSParser.LBRACE)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018443116560) != 0):
                self.state = 181
                self.classMember()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
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
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.fieldDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.constructorDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
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
            self.state = 194
            self.type_()
            self.state = 195
            self.match(JSSParser.ID)
            self.state = 196
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
            self.state = 198
            self.match(JSSParser.ID)
            self.state = 199
            self.match(JSSParser.CONSTRUCTOR)
            self.state = 200
            self.match(JSSParser.LPAREN)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018443116544) != 0):
                self.state = 201
                self.parameterList()


            self.state = 204
            self.match(JSSParser.RPAREN)
            self.state = 205
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
            self.state = 207
            self.returnType()
            self.state = 208
            self.match(JSSParser.ID)
            self.state = 209
            self.match(JSSParser.LPAREN)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018443116544) != 0):
                self.state = 210
                self.parameterList()


            self.state = 213
            self.match(JSSParser.RPAREN)
            self.state = 214
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
            self.state = 216
            self.match(JSSParser.FUNCTION)
            self.state = 217
            self.returnType()
            self.state = 218
            self.match(JSSParser.ID)
            self.state = 219
            self.match(JSSParser.LPAREN)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018443116544) != 0):
                self.state = 220
                self.parameterList()


            self.state = 223
            self.match(JSSParser.RPAREN)
            self.state = 224
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
            self.state = 226
            self.parameter()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 227
                self.match(JSSParser.COMMA)
                self.state = 228
                self.parameter()
                self.state = 233
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
            self.state = 234
            self.type_()
            self.state = 235
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
            self.state = 237
            self.match(JSSParser.LBRACE)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8724722348076301190) != 0):
                self.state = 238
                self.statement()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
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
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.block()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.variableDeclaration()
                self.state = 248
                self.match(JSSParser.SEMI)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                self.ifStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.whileStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                self.forStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 253
                self.breakStatement()
                self.state = 254
                self.match(JSSParser.SEMI)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
                self.returnStatement()
                self.state = 257
                self.match(JSSParser.SEMI)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 259
                self.inputStatement()
                self.state = 260
                self.match(JSSParser.SEMI)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 9)
                self.state = 262
                self.consoleLogStatement()
                self.state = 263
                self.match(JSSParser.SEMI)
                pass
            elif token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 38, 39, 44, 45, 46, 50, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 10)
                self.state = 265
                self.expression()
                self.state = 266
                self.match(JSSParser.SEMI)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 11)
                self.state = 268
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
            self.state = 271
            self.match(JSSParser.IF)
            self.state = 272
            self.match(JSSParser.LPAREN)
            self.state = 273
            self.expression()
            self.state = 274
            self.match(JSSParser.RPAREN)
            self.state = 275
            self.block()
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 276
                    self.elseIfBlock() 
                self.state = 281
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 282
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
            self.state = 285
            self.match(JSSParser.ELSE)
            self.state = 286
            self.match(JSSParser.IF)
            self.state = 287
            self.match(JSSParser.LPAREN)
            self.state = 288
            self.expression()
            self.state = 289
            self.match(JSSParser.RPAREN)
            self.state = 290
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
            self.state = 292
            self.match(JSSParser.ELSE)
            self.state = 293
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
            self.state = 295
            self.match(JSSParser.WHILE)
            self.state = 296
            self.match(JSSParser.LPAREN)
            self.state = 297
            self.expression()
            self.state = 298
            self.match(JSSParser.RPAREN)
            self.state = 299
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


        def forCondition(self):
            return self.getTypedRuleContext(JSSParser.ForConditionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(JSSParser.ForUpdateContext,0)


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
            self.state = 301
            self.match(JSSParser.FOR)
            self.state = 302
            self.match(JSSParser.LPAREN)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185094) != 0):
                self.state = 303
                self.forInit()


            self.state = 306
            self.match(JSSParser.SEMI)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 307
                self.forCondition()


            self.state = 310
            self.match(JSSParser.SEMI)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 311
                self.forUpdate()


            self.state = 314
            self.match(JSSParser.RPAREN)
            self.state = 315
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


        def expressionList(self):
            return self.getTypedRuleContext(JSSParser.ExpressionListContext,0)


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
            self.state = 319
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.variableDeclaration()
                pass
            elif token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 38, 39, 44, 45, 46, 50, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.expressionList()
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


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(JSSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_forCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondition" ):
                listener.enterForCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondition" ):
                listener.exitForCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = JSSParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(JSSParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return JSSParser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = JSSParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.expressionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
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
            return JSSParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = JSSParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.expression()
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 326
                self.match(JSSParser.COMMA)
                self.state = 327
                self.expression()
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 62, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
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
        self.enterRule(localctx, 64, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(JSSParser.RETURN)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 336
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
        self.enterRule(localctx, 66, self.RULE_inputStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(JSSParser.INPUT)
            self.state = 340
            self.match(JSSParser.LPAREN)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648037184474153344) != 0):
                self.state = 341
                self.inputArgumentList()


            self.state = 344
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
        self.enterRule(localctx, 68, self.RULE_inputArgumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.inputArgument()
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 347
                self.match(JSSParser.COMMA)
                self.state = 348
                self.inputArgument()
                self.state = 353
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
        self.enterRule(localctx, 70, self.RULE_inputArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
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
        self.enterRule(localctx, 72, self.RULE_consoleLogStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(JSSParser.CONSOLE_LOG)
            self.state = 357
            self.match(JSSParser.LPAREN)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 358
                self.argumentList()


            self.state = 361
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
        self.enterRule(localctx, 74, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
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
        self.enterRule(localctx, 76, self.RULE_assignmentExpression)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.postfixExpression()
                self.state = 366
                self.assignmentOperator()
                self.state = 367
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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

        def AND_ASSIGN(self):
            return self.getToken(JSSParser.AND_ASSIGN, 0)

        def OR_ASSIGN(self):
            return self.getToken(JSSParser.OR_ASSIGN, 0)

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
        self.enterRule(localctx, 78, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2203301445632) != 0)):
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
        self.enterRule(localctx, 80, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.logicalAndExpression()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 375
                self.match(JSSParser.OR)
                self.state = 376
                self.logicalAndExpression()
                self.state = 381
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
        self.enterRule(localctx, 82, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.equalityExpression()
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 383
                self.match(JSSParser.AND)
                self.state = 384
                self.equalityExpression()
                self.state = 389
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
        self.enterRule(localctx, 84, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.relationalExpression()
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 391
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 392
                self.relationalExpression()
                self.state = 397
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
        self.enterRule(localctx, 86, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.additiveExpression()
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13245679140864) != 0):
                self.state = 399
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13245679140864) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 400
                self.additiveExpression()
                self.state = 405
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
        self.enterRule(localctx, 88, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.multiplicativeExpression()
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45 or _la==46:
                self.state = 407
                _la = self._input.LA(1)
                if not(_la==45 or _la==46):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 408
                self.multiplicativeExpression()
                self.state = 413
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
        self.enterRule(localctx, 90, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.powerExpression()
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0):
                self.state = 415
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 416
                self.powerExpression()
                self.state = 421
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
        self.enterRule(localctx, 92, self.RULE_powerExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.unaryExpression()
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 423
                self.match(JSSParser.POW)
                self.state = 424
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
        self.enterRule(localctx, 94, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38, 39, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 123969936031744) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 428
                self.unaryExpression()
                pass
            elif token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 50, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
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
        self.enterRule(localctx, 96, self.RULE_postfixExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.primaryExpression()
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 307371499201757184) != 0):
                self.state = 433
                self.postfixSuffix()
                self.state = 438
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

        def INC(self):
            return self.getToken(JSSParser.INC, 0)

        def DEC(self):
            return self.getToken(JSSParser.DEC, 0)

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
        self.enterRule(localctx, 98, self.RULE_postfixSuffix)
        self._la = 0 # Token type
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(JSSParser.DOT)
                self.state = 440
                self.match(JSSParser.ID)
                self.state = 441
                self.match(JSSParser.LPAREN)
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                    self.state = 442
                    self.argumentList()


                self.state = 445
                self.match(JSSParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.match(JSSParser.LBRACK)
                self.state = 447
                self.expression()
                self.state = 448
                self.match(JSSParser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 450
                self.match(JSSParser.DOT)
                self.state = 451
                self.match(JSSParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 452
                self.match(JSSParser.LPAREN)
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                    self.state = 453
                    self.argumentList()


                self.state = 456
                self.match(JSSParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 457
                self.match(JSSParser.INC)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 458
                self.match(JSSParser.DEC)
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
        self.enterRule(localctx, 100, self.RULE_primaryExpression)
        try:
            self.state = 470
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 59, 60, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.literal()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.match(JSSParser.ID)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
                self.match(JSSParser.THIS)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 464
                self.newExpression()
                pass
            elif token in [20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 465
                self.castExpression()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 6)
                self.state = 466
                self.match(JSSParser.LPAREN)
                self.state = 467
                self.expression()
                self.state = 468
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
        self.enterRule(localctx, 102, self.RULE_newExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(JSSParser.NEW)
            self.state = 473
            self.match(JSSParser.ID)
            self.state = 474
            self.match(JSSParser.LPAREN)
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 475
                self.argumentList()


            self.state = 478
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
        self.enterRule(localctx, 104, self.RULE_castExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.primitiveType()
            self.state = 481
            self.match(JSSParser.LPAREN)
            self.state = 482
            self.expression()
            self.state = 483
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
        self.enterRule(localctx, 106, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.expression()
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 486
                self.match(JSSParser.COMMA)
                self.state = 487
                self.expression()
                self.state = 492
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
        self.enterRule(localctx, 108, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4035225266124193792) != 0)):
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





