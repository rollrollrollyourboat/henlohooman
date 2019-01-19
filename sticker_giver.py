import random

class StickerGiver():
  def __init__(self):
    self._stickers = [
    'CAADBQADOgADsV0ZFMreYOeI4Ka6Ag',
    'CAADBQADTAADsV0ZFE2qObHgdgMUAg',
    'CAADAgADCAADNraOCMoRkz7wEy9pAg',
    'CAADAgADCgADNraOCEl_Jsv8JOo9Ag',
    'CAADAgADDAADNraOCEkHin2ya020Ag',
    'CAADAgADDgADNraOCE15_R1lGtHcAg',
    'CAADAgADEAADNraOCKnKFD435pvOAg',
    'CAADAgADGAADNraOCFaAQzhyMG4LAg',
    'CAADAgADFAADNraOCPLD6h0FLiZYAg',
    'CAADAgADHAADNraOCLBipsm-lf2XAg',
    'CAADAgADHgADNraOCE8hiCWKwKWYAg',
    'CAADAgADIAADNraOCMcmRNa491sFAg',
    'CAADAgADIgADNraOCDhUh5WS4N4qAg',
    'CAADAgADJAADNraOCF04b51tkSdSAg',
    'CAADAgADGgADNraOCNIjVxaXrZ_eAg',
    'CAADAgADKAADNraOCCqXlVqUKd4SAg',
    'CAADAgADPAADNraOCEH-JIBlYgrOAg',
    'CAADAgADUQADNraOCLWtL3zC2WyxAg',
    'CAADAgADWwADNraOCFhHT0h1zkuJAg',
    'CAADAgADdQADNraOCC5QsW-QAAFdowI',
    'CAADAgADgAADNraOCMyPxzxRhO2RAg',
    'CAADBQADagEAAi1ybAF-_KGJvPaYowI',
    'CAADBQADfgEAAi1ybAH39zBspZrTwwI',
    'CAADBQADggEAAi1ybAFPqDtliVF_hgI'
    ];

  def pollSticker(self):
    return self._stickers[random.randint(0, len(self._stickers) - 1)];