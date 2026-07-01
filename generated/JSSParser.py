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
        4,1,64,478,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,1,0,5,0,106,
        8,0,10,0,12,0,109,9,0,1,0,1,0,1,1,1,1,1,1,3,1,116,8,1,1,2,1,2,1,
        2,1,2,1,2,5,2,123,8,2,10,2,12,2,126,9,2,1,3,1,3,1,4,1,4,1,4,3,4,
        133,8,4,1,5,1,5,3,5,137,8,5,1,6,1,6,1,6,1,6,5,6,143,8,6,10,6,12,
        6,146,9,6,3,6,148,8,6,1,6,1,6,1,7,1,7,3,7,154,8,7,1,8,1,8,3,8,158,
        8,8,1,9,1,9,1,10,1,10,1,10,4,10,165,8,10,11,10,12,10,166,1,11,1,
        11,3,11,171,8,11,1,12,1,12,1,12,1,12,5,12,177,8,12,10,12,12,12,180,
        9,12,1,12,1,12,1,13,1,13,1,13,3,13,187,8,13,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,3,15,197,8,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,3,16,206,8,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,3,17,
        216,8,17,1,17,1,17,1,17,1,18,1,18,1,18,5,18,224,8,18,10,18,12,18,
        227,9,18,1,19,1,19,1,19,1,20,1,20,5,20,234,8,20,10,20,12,20,237,
        9,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,264,8,21,1,22,1,22,1,22,1,22,1,22,1,22,5,22,272,8,22,10,22,
        12,22,275,9,22,1,22,3,22,278,8,22,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        3,26,299,8,26,1,26,1,26,3,26,303,8,26,1,26,1,26,3,26,307,8,26,1,
        26,1,26,1,26,1,27,1,27,3,27,314,8,27,1,28,1,28,1,29,1,29,3,29,320,
        8,29,1,30,1,30,1,30,3,30,325,8,30,1,30,1,30,1,31,1,31,1,31,5,31,
        332,8,31,10,31,12,31,335,9,31,1,32,1,32,1,33,1,33,1,33,3,33,342,
        8,33,1,33,1,33,1,34,1,34,1,35,1,35,1,35,1,35,1,35,3,35,353,8,35,
        1,36,1,36,1,37,1,37,1,37,5,37,360,8,37,10,37,12,37,363,9,37,1,38,
        1,38,1,38,5,38,368,8,38,10,38,12,38,371,9,38,1,39,1,39,1,39,5,39,
        376,8,39,10,39,12,39,379,9,39,1,40,1,40,1,40,5,40,384,8,40,10,40,
        12,40,387,9,40,1,41,1,41,1,41,5,41,392,8,41,10,41,12,41,395,9,41,
        1,42,1,42,1,42,5,42,400,8,42,10,42,12,42,403,9,42,1,43,1,43,1,43,
        3,43,408,8,43,1,44,1,44,1,44,3,44,413,8,44,1,45,1,45,5,45,417,8,
        45,10,45,12,45,420,9,45,1,46,1,46,1,46,1,46,3,46,426,8,46,1,46,1,
        46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,3,46,437,8,46,1,46,1,46,1,
        46,3,46,442,8,46,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,3,
        47,453,8,47,1,48,1,48,1,48,1,48,3,48,459,8,48,1,48,1,48,1,49,1,49,
        1,49,1,49,1,49,1,50,1,50,1,50,5,50,471,8,50,10,50,12,50,474,9,50,
        1,51,1,51,1,51,0,0,52,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,
        76,78,80,82,84,86,88,90,92,94,96,98,100,102,0,9,1,0,1,2,1,0,20,23,
        2,0,24,31,41,41,1,0,32,33,2,0,34,35,42,43,1,0,45,46,1,0,47,49,2,
        0,38,39,44,46,2,0,15,17,59,61,489,0,107,1,0,0,0,2,115,1,0,0,0,4,
        117,1,0,0,0,6,127,1,0,0,0,8,129,1,0,0,0,10,136,1,0,0,0,12,138,1,
        0,0,0,14,151,1,0,0,0,16,157,1,0,0,0,18,159,1,0,0,0,20,164,1,0,0,
        0,22,170,1,0,0,0,24,172,1,0,0,0,26,186,1,0,0,0,28,188,1,0,0,0,30,
        192,1,0,0,0,32,201,1,0,0,0,34,210,1,0,0,0,36,220,1,0,0,0,38,228,
        1,0,0,0,40,231,1,0,0,0,42,263,1,0,0,0,44,265,1,0,0,0,46,279,1,0,
        0,0,48,286,1,0,0,0,50,289,1,0,0,0,52,295,1,0,0,0,54,313,1,0,0,0,
        56,315,1,0,0,0,58,317,1,0,0,0,60,321,1,0,0,0,62,328,1,0,0,0,64,336,
        1,0,0,0,66,338,1,0,0,0,68,345,1,0,0,0,70,352,1,0,0,0,72,354,1,0,
        0,0,74,356,1,0,0,0,76,364,1,0,0,0,78,372,1,0,0,0,80,380,1,0,0,0,
        82,388,1,0,0,0,84,396,1,0,0,0,86,404,1,0,0,0,88,412,1,0,0,0,90,414,
        1,0,0,0,92,441,1,0,0,0,94,452,1,0,0,0,96,454,1,0,0,0,98,462,1,0,
        0,0,100,467,1,0,0,0,102,475,1,0,0,0,104,106,3,2,1,0,105,104,1,0,
        0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,110,1,0,
        0,0,109,107,1,0,0,0,110,111,5,0,0,1,111,1,1,0,0,0,112,116,3,24,12,
        0,113,116,3,34,17,0,114,116,3,42,21,0,115,112,1,0,0,0,115,113,1,
        0,0,0,115,114,1,0,0,0,116,3,1,0,0,0,117,118,3,6,3,0,118,119,3,14,
        7,0,119,124,3,8,4,0,120,121,5,57,0,0,121,123,3,8,4,0,122,120,1,0,
        0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,5,1,0,0,
        0,126,124,1,0,0,0,127,128,7,0,0,0,128,7,1,0,0,0,129,132,5,62,0,0,
        130,131,5,41,0,0,131,133,3,10,5,0,132,130,1,0,0,0,132,133,1,0,0,
        0,133,9,1,0,0,0,134,137,3,68,34,0,135,137,3,12,6,0,136,134,1,0,0,
        0,136,135,1,0,0,0,137,11,1,0,0,0,138,147,5,54,0,0,139,144,3,68,34,
        0,140,141,5,57,0,0,141,143,3,68,34,0,142,140,1,0,0,0,143,146,1,0,
        0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,148,1,0,0,0,146,144,1,0,
        0,0,147,139,1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,55,
        0,0,150,13,1,0,0,0,151,153,3,16,8,0,152,154,3,20,10,0,153,152,1,
        0,0,0,153,154,1,0,0,0,154,15,1,0,0,0,155,158,3,18,9,0,156,158,5,
        62,0,0,157,155,1,0,0,0,157,156,1,0,0,0,158,17,1,0,0,0,159,160,7,
        1,0,0,160,19,1,0,0,0,161,162,5,54,0,0,162,163,5,60,0,0,163,165,5,
        55,0,0,164,161,1,0,0,0,165,166,1,0,0,0,166,164,1,0,0,0,166,167,1,
        0,0,0,167,21,1,0,0,0,168,171,3,14,7,0,169,171,5,4,0,0,170,168,1,
        0,0,0,170,169,1,0,0,0,171,23,1,0,0,0,172,173,5,5,0,0,173,174,5,62,
        0,0,174,178,5,52,0,0,175,177,3,26,13,0,176,175,1,0,0,0,177,180,1,
        0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,178,1,
        0,0,0,181,182,5,53,0,0,182,25,1,0,0,0,183,187,3,28,14,0,184,187,
        3,30,15,0,185,187,3,32,16,0,186,183,1,0,0,0,186,184,1,0,0,0,186,
        185,1,0,0,0,187,27,1,0,0,0,188,189,3,14,7,0,189,190,5,62,0,0,190,
        191,5,56,0,0,191,29,1,0,0,0,192,193,5,62,0,0,193,194,5,6,0,0,194,
        196,5,50,0,0,195,197,3,36,18,0,196,195,1,0,0,0,196,197,1,0,0,0,197,
        198,1,0,0,0,198,199,5,51,0,0,199,200,3,40,20,0,200,31,1,0,0,0,201,
        202,3,22,11,0,202,203,5,62,0,0,203,205,5,50,0,0,204,206,3,36,18,
        0,205,204,1,0,0,0,205,206,1,0,0,0,206,207,1,0,0,0,207,208,5,51,0,
        0,208,209,3,40,20,0,209,33,1,0,0,0,210,211,5,3,0,0,211,212,3,22,
        11,0,212,213,5,62,0,0,213,215,5,50,0,0,214,216,3,36,18,0,215,214,
        1,0,0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,218,5,51,0,0,218,219,
        3,40,20,0,219,35,1,0,0,0,220,225,3,38,19,0,221,222,5,57,0,0,222,
        224,3,38,19,0,223,221,1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,
        226,1,0,0,0,226,37,1,0,0,0,227,225,1,0,0,0,228,229,3,14,7,0,229,
        230,5,62,0,0,230,39,1,0,0,0,231,235,5,52,0,0,232,234,3,42,21,0,233,
        232,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,
        238,1,0,0,0,237,235,1,0,0,0,238,239,5,53,0,0,239,41,1,0,0,0,240,
        264,3,40,20,0,241,242,3,4,2,0,242,243,5,56,0,0,243,264,1,0,0,0,244,
        264,3,44,22,0,245,264,3,50,25,0,246,264,3,52,26,0,247,248,3,56,28,
        0,248,249,5,56,0,0,249,264,1,0,0,0,250,251,3,58,29,0,251,252,5,56,
        0,0,252,264,1,0,0,0,253,254,3,60,30,0,254,255,5,56,0,0,255,264,1,
        0,0,0,256,257,3,66,33,0,257,258,5,56,0,0,258,264,1,0,0,0,259,260,
        3,68,34,0,260,261,5,56,0,0,261,264,1,0,0,0,262,264,5,56,0,0,263,
        240,1,0,0,0,263,241,1,0,0,0,263,244,1,0,0,0,263,245,1,0,0,0,263,
        246,1,0,0,0,263,247,1,0,0,0,263,250,1,0,0,0,263,253,1,0,0,0,263,
        256,1,0,0,0,263,259,1,0,0,0,263,262,1,0,0,0,264,43,1,0,0,0,265,266,
        5,9,0,0,266,267,5,50,0,0,267,268,3,68,34,0,268,269,5,51,0,0,269,
        273,3,40,20,0,270,272,3,46,23,0,271,270,1,0,0,0,272,275,1,0,0,0,
        273,271,1,0,0,0,273,274,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,
        276,278,3,48,24,0,277,276,1,0,0,0,277,278,1,0,0,0,278,45,1,0,0,0,
        279,280,5,10,0,0,280,281,5,9,0,0,281,282,5,50,0,0,282,283,3,68,34,
        0,283,284,5,51,0,0,284,285,3,40,20,0,285,47,1,0,0,0,286,287,5,10,
        0,0,287,288,3,40,20,0,288,49,1,0,0,0,289,290,5,11,0,0,290,291,5,
        50,0,0,291,292,3,68,34,0,292,293,5,51,0,0,293,294,3,40,20,0,294,
        51,1,0,0,0,295,296,5,12,0,0,296,298,5,50,0,0,297,299,3,54,27,0,298,
        297,1,0,0,0,298,299,1,0,0,0,299,300,1,0,0,0,300,302,5,56,0,0,301,
        303,3,68,34,0,302,301,1,0,0,0,302,303,1,0,0,0,303,304,1,0,0,0,304,
        306,5,56,0,0,305,307,3,68,34,0,306,305,1,0,0,0,306,307,1,0,0,0,307,
        308,1,0,0,0,308,309,5,51,0,0,309,310,3,40,20,0,310,53,1,0,0,0,311,
        314,3,4,2,0,312,314,3,68,34,0,313,311,1,0,0,0,313,312,1,0,0,0,314,
        55,1,0,0,0,315,316,5,13,0,0,316,57,1,0,0,0,317,319,5,14,0,0,318,
        320,3,68,34,0,319,318,1,0,0,0,319,320,1,0,0,0,320,59,1,0,0,0,321,
        322,5,18,0,0,322,324,5,50,0,0,323,325,3,62,31,0,324,323,1,0,0,0,
        324,325,1,0,0,0,325,326,1,0,0,0,326,327,5,51,0,0,327,61,1,0,0,0,
        328,333,3,64,32,0,329,330,5,57,0,0,330,332,3,64,32,0,331,329,1,0,
        0,0,332,335,1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,63,1,0,0,
        0,335,333,1,0,0,0,336,337,3,90,45,0,337,65,1,0,0,0,338,339,5,19,
        0,0,339,341,5,50,0,0,340,342,3,100,50,0,341,340,1,0,0,0,341,342,
        1,0,0,0,342,343,1,0,0,0,343,344,5,51,0,0,344,67,1,0,0,0,345,346,
        3,70,35,0,346,69,1,0,0,0,347,348,3,90,45,0,348,349,3,72,36,0,349,
        350,3,70,35,0,350,353,1,0,0,0,351,353,3,74,37,0,352,347,1,0,0,0,
        352,351,1,0,0,0,353,71,1,0,0,0,354,355,7,2,0,0,355,73,1,0,0,0,356,
        361,3,76,38,0,357,358,5,37,0,0,358,360,3,76,38,0,359,357,1,0,0,0,
        360,363,1,0,0,0,361,359,1,0,0,0,361,362,1,0,0,0,362,75,1,0,0,0,363,
        361,1,0,0,0,364,369,3,78,39,0,365,366,5,36,0,0,366,368,3,78,39,0,
        367,365,1,0,0,0,368,371,1,0,0,0,369,367,1,0,0,0,369,370,1,0,0,0,
        370,77,1,0,0,0,371,369,1,0,0,0,372,377,3,80,40,0,373,374,7,3,0,0,
        374,376,3,80,40,0,375,373,1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,
        0,377,378,1,0,0,0,378,79,1,0,0,0,379,377,1,0,0,0,380,385,3,82,41,
        0,381,382,7,4,0,0,382,384,3,82,41,0,383,381,1,0,0,0,384,387,1,0,
        0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,81,1,0,0,0,387,385,1,0,0,
        0,388,393,3,84,42,0,389,390,7,5,0,0,390,392,3,84,42,0,391,389,1,
        0,0,0,392,395,1,0,0,0,393,391,1,0,0,0,393,394,1,0,0,0,394,83,1,0,
        0,0,395,393,1,0,0,0,396,401,3,86,43,0,397,398,7,6,0,0,398,400,3,
        86,43,0,399,397,1,0,0,0,400,403,1,0,0,0,401,399,1,0,0,0,401,402,
        1,0,0,0,402,85,1,0,0,0,403,401,1,0,0,0,404,407,3,88,44,0,405,406,
        5,40,0,0,406,408,3,86,43,0,407,405,1,0,0,0,407,408,1,0,0,0,408,87,
        1,0,0,0,409,410,7,7,0,0,410,413,3,88,44,0,411,413,3,90,45,0,412,
        409,1,0,0,0,412,411,1,0,0,0,413,89,1,0,0,0,414,418,3,94,47,0,415,
        417,3,92,46,0,416,415,1,0,0,0,417,420,1,0,0,0,418,416,1,0,0,0,418,
        419,1,0,0,0,419,91,1,0,0,0,420,418,1,0,0,0,421,422,5,58,0,0,422,
        423,5,62,0,0,423,425,5,50,0,0,424,426,3,100,50,0,425,424,1,0,0,0,
        425,426,1,0,0,0,426,427,1,0,0,0,427,442,5,51,0,0,428,429,5,54,0,
        0,429,430,3,68,34,0,430,431,5,55,0,0,431,442,1,0,0,0,432,433,5,58,
        0,0,433,442,5,62,0,0,434,436,5,50,0,0,435,437,3,100,50,0,436,435,
        1,0,0,0,436,437,1,0,0,0,437,438,1,0,0,0,438,442,5,51,0,0,439,442,
        5,38,0,0,440,442,5,39,0,0,441,421,1,0,0,0,441,428,1,0,0,0,441,432,
        1,0,0,0,441,434,1,0,0,0,441,439,1,0,0,0,441,440,1,0,0,0,442,93,1,
        0,0,0,443,453,3,102,51,0,444,453,5,62,0,0,445,453,5,7,0,0,446,453,
        3,96,48,0,447,453,3,98,49,0,448,449,5,50,0,0,449,450,3,68,34,0,450,
        451,5,51,0,0,451,453,1,0,0,0,452,443,1,0,0,0,452,444,1,0,0,0,452,
        445,1,0,0,0,452,446,1,0,0,0,452,447,1,0,0,0,452,448,1,0,0,0,453,
        95,1,0,0,0,454,455,5,8,0,0,455,456,5,62,0,0,456,458,5,50,0,0,457,
        459,3,100,50,0,458,457,1,0,0,0,458,459,1,0,0,0,459,460,1,0,0,0,460,
        461,5,51,0,0,461,97,1,0,0,0,462,463,3,18,9,0,463,464,5,50,0,0,464,
        465,3,68,34,0,465,466,5,51,0,0,466,99,1,0,0,0,467,472,3,68,34,0,
        468,469,5,57,0,0,469,471,3,68,34,0,470,468,1,0,0,0,471,474,1,0,0,
        0,472,470,1,0,0,0,472,473,1,0,0,0,473,101,1,0,0,0,474,472,1,0,0,
        0,475,476,7,8,0,0,476,103,1,0,0,0,45,107,115,124,132,136,144,147,
        153,157,166,170,178,186,196,205,215,225,235,263,273,277,298,302,
        306,313,319,324,333,341,352,361,369,377,385,393,401,407,412,418,
        425,436,441,452,458,472
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
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8724722348076301230) != 0):
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
            self.state = 115
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
            elif token in [1, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 38, 39, 44, 45, 46, 50, 52, 56, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
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
            self.state = 117
            self.variableModifier()
            self.state = 118
            self.type_()
            self.state = 119
            self.variableDeclarator()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 120
                self.match(JSSParser.COMMA)
                self.state = 121
                self.variableDeclarator()
                self.state = 126
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
            self.state = 127
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
            self.state = 129
            self.match(JSSParser.ID)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 130
                self.match(JSSParser.ASSIGN)
                self.state = 131
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
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 38, 39, 44, 45, 46, 50, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.expression()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
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
            self.state = 138
            self.match(JSSParser.LBRACK)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 139
                self.expression()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==57:
                    self.state = 140
                    self.match(JSSParser.COMMA)
                    self.state = 141
                    self.expression()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 149
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
            self.state = 151
            self.baseType()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 152
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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.primitiveType()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
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
            self.state = 159
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
            self.state = 164 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 161
                self.match(JSSParser.LBRACK)
                self.state = 162
                self.match(JSSParser.INT_LITERAL)
                self.state = 163
                self.match(JSSParser.RBRACK)
                self.state = 166 
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
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.type_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
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
            self.state = 172
            self.match(JSSParser.CLASS)
            self.state = 173
            self.match(JSSParser.ID)
            self.state = 174
            self.match(JSSParser.LBRACE)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018443116560) != 0):
                self.state = 175
                self.classMember()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.fieldDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.constructorDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
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
            self.state = 188
            self.type_()
            self.state = 189
            self.match(JSSParser.ID)
            self.state = 190
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
            self.state = 192
            self.match(JSSParser.ID)
            self.state = 193
            self.match(JSSParser.CONSTRUCTOR)
            self.state = 194
            self.match(JSSParser.LPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018443116544) != 0):
                self.state = 195
                self.parameterList()


            self.state = 198
            self.match(JSSParser.RPAREN)
            self.state = 199
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
            self.state = 201
            self.returnType()
            self.state = 202
            self.match(JSSParser.ID)
            self.state = 203
            self.match(JSSParser.LPAREN)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018443116544) != 0):
                self.state = 204
                self.parameterList()


            self.state = 207
            self.match(JSSParser.RPAREN)
            self.state = 208
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
            self.state = 210
            self.match(JSSParser.FUNCTION)
            self.state = 211
            self.returnType()
            self.state = 212
            self.match(JSSParser.ID)
            self.state = 213
            self.match(JSSParser.LPAREN)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018443116544) != 0):
                self.state = 214
                self.parameterList()


            self.state = 217
            self.match(JSSParser.RPAREN)
            self.state = 218
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
            self.state = 220
            self.parameter()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 221
                self.match(JSSParser.COMMA)
                self.state = 222
                self.parameter()
                self.state = 227
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
            self.state = 228
            self.type_()
            self.state = 229
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
            self.state = 231
            self.match(JSSParser.LBRACE)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8724722348076301190) != 0):
                self.state = 232
                self.statement()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
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
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.block()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.variableDeclaration()
                self.state = 242
                self.match(JSSParser.SEMI)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.ifStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 245
                self.whileStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 246
                self.forStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 247
                self.breakStatement()
                self.state = 248
                self.match(JSSParser.SEMI)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 250
                self.returnStatement()
                self.state = 251
                self.match(JSSParser.SEMI)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 253
                self.inputStatement()
                self.state = 254
                self.match(JSSParser.SEMI)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 9)
                self.state = 256
                self.consoleLogStatement()
                self.state = 257
                self.match(JSSParser.SEMI)
                pass
            elif token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 38, 39, 44, 45, 46, 50, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 10)
                self.state = 259
                self.expression()
                self.state = 260
                self.match(JSSParser.SEMI)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 11)
                self.state = 262
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
            self.state = 265
            self.match(JSSParser.IF)
            self.state = 266
            self.match(JSSParser.LPAREN)
            self.state = 267
            self.expression()
            self.state = 268
            self.match(JSSParser.RPAREN)
            self.state = 269
            self.block()
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 270
                    self.elseIfBlock() 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 276
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
            self.state = 279
            self.match(JSSParser.ELSE)
            self.state = 280
            self.match(JSSParser.IF)
            self.state = 281
            self.match(JSSParser.LPAREN)
            self.state = 282
            self.expression()
            self.state = 283
            self.match(JSSParser.RPAREN)
            self.state = 284
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
            self.state = 286
            self.match(JSSParser.ELSE)
            self.state = 287
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
            self.state = 289
            self.match(JSSParser.WHILE)
            self.state = 290
            self.match(JSSParser.LPAREN)
            self.state = 291
            self.expression()
            self.state = 292
            self.match(JSSParser.RPAREN)
            self.state = 293
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
            self.state = 295
            self.match(JSSParser.FOR)
            self.state = 296
            self.match(JSSParser.LPAREN)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185094) != 0):
                self.state = 297
                self.forInit()


            self.state = 300
            self.match(JSSParser.SEMI)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 301
                self.expression()


            self.state = 304
            self.match(JSSParser.SEMI)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 305
                self.expression()


            self.state = 308
            self.match(JSSParser.RPAREN)
            self.state = 309
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
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.variableDeclaration()
                pass
            elif token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 38, 39, 44, 45, 46, 50, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
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
            self.state = 315
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
            self.state = 317
            self.match(JSSParser.RETURN)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 318
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
            self.state = 321
            self.match(JSSParser.INPUT)
            self.state = 322
            self.match(JSSParser.LPAREN)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648037184474153344) != 0):
                self.state = 323
                self.inputArgumentList()


            self.state = 326
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
            self.state = 328
            self.inputArgument()
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 329
                self.match(JSSParser.COMMA)
                self.state = 330
                self.inputArgument()
                self.state = 335
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
            self.state = 336
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
            self.state = 338
            self.match(JSSParser.CONSOLE_LOG)
            self.state = 339
            self.match(JSSParser.LPAREN)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 340
                self.argumentList()


            self.state = 343
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
            self.state = 345
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
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.postfixExpression()
                self.state = 348
                self.assignmentOperator()
                self.state = 349
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
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
        self.enterRule(localctx, 72, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
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
        self.enterRule(localctx, 74, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.logicalAndExpression()
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 357
                self.match(JSSParser.OR)
                self.state = 358
                self.logicalAndExpression()
                self.state = 363
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
            self.state = 364
            self.equalityExpression()
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 365
                self.match(JSSParser.AND)
                self.state = 366
                self.equalityExpression()
                self.state = 371
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
            self.state = 372
            self.relationalExpression()
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 373
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 374
                self.relationalExpression()
                self.state = 379
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
            self.state = 380
            self.additiveExpression()
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13245679140864) != 0):
                self.state = 381
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13245679140864) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 382
                self.additiveExpression()
                self.state = 387
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
            self.state = 388
            self.multiplicativeExpression()
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45 or _la==46:
                self.state = 389
                _la = self._input.LA(1)
                if not(_la==45 or _la==46):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 390
                self.multiplicativeExpression()
                self.state = 395
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
            self.state = 396
            self.powerExpression()
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0):
                self.state = 397
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 398
                self.powerExpression()
                self.state = 403
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
            self.state = 404
            self.unaryExpression()
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 405
                self.match(JSSParser.POW)
                self.state = 406
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
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38, 39, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 123969936031744) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 410
                self.unaryExpression()
                pass
            elif token in [7, 8, 15, 16, 17, 20, 21, 22, 23, 50, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
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
            self.state = 414
            self.primaryExpression()
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 307371499201757184) != 0):
                self.state = 415
                self.postfixSuffix()
                self.state = 420
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
        self.enterRule(localctx, 92, self.RULE_postfixSuffix)
        self._la = 0 # Token type
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(JSSParser.DOT)
                self.state = 422
                self.match(JSSParser.ID)
                self.state = 423
                self.match(JSSParser.LPAREN)
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                    self.state = 424
                    self.argumentList()


                self.state = 427
                self.match(JSSParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.match(JSSParser.LBRACK)
                self.state = 429
                self.expression()
                self.state = 430
                self.match(JSSParser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.match(JSSParser.DOT)
                self.state = 433
                self.match(JSSParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 434
                self.match(JSSParser.LPAREN)
                self.state = 436
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                    self.state = 435
                    self.argumentList()


                self.state = 438
                self.match(JSSParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 439
                self.match(JSSParser.INC)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 440
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
        self.enterRule(localctx, 94, self.RULE_primaryExpression)
        try:
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 59, 60, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.literal()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.match(JSSParser.ID)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.match(JSSParser.THIS)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 446
                self.newExpression()
                pass
            elif token in [20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 447
                self.castExpression()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 6)
                self.state = 448
                self.match(JSSParser.LPAREN)
                self.state = 449
                self.expression()
                self.state = 450
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
            self.state = 454
            self.match(JSSParser.NEW)
            self.state = 455
            self.match(JSSParser.ID)
            self.state = 456
            self.match(JSSParser.LPAREN)
            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8648161154410185088) != 0):
                self.state = 457
                self.argumentList()


            self.state = 460
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
            self.state = 462
            self.primitiveType()
            self.state = 463
            self.match(JSSParser.LPAREN)
            self.state = 464
            self.expression()
            self.state = 465
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
            self.state = 467
            self.expression()
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 468
                self.match(JSSParser.COMMA)
                self.state = 469
                self.expression()
                self.state = 474
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
            self.state = 475
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





